import argparse
import json
import os
import re
import textwrap
import time
import yaml
from glob import glob

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException, ElementClickInterceptedException,
    ElementNotInteractableException)
from selenium.webdriver.common.by import By

# Find directories and files
try:
    REPO_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
except NameError:  # Running interactively from repo root
    REPO_DIR = os.path.join(os.getcwd())
SOL_DIR = os.path.join(REPO_DIR, 'solutions')
TEMPLATE_DIR = os.path.join(REPO_DIR, 'scrape', 'templates')
CONF_PATH = os.path.join(REPO_DIR, 'scrape', 'conf.yaml')

# Handle conf
with open(CONF_PATH) as conf:
    GECKO_DRIVER_PATH = yaml.safe_load(conf).get('GECKO_DRIVER_PATH')

# Order of languages
LANGUAGES = (
    'C++', 'Java', 'Python', 'Python3', 'C', 'C#', 'JavaScript',
    'Ruby', 'Swift', 'Go', 'Scala', 'Kotlin', 'Rust', 'PHP')
EXTENSIONS = (
    'c', 'java', 'py', 'py', 'c', 'cs', 'js',
    'rb', 'swift', 'go', 'scala', 'kt', 'rs', 'php')
FUNCTION_SIGS = (
    '', '',
    r'def ([^ ^_]+)\(',
    r'def ([^ ^_]+)\(',
    '', '',
    r'var ([^ ^_]+) = function',
    '', '', '', '', '', '', ''
)


class LeetCodeScraper:
    RANDOM_PROBLEM_URL = (
        "https://leetcode.com/problems/random-one-question/all")
    MAX_TRIES = 5

    def __init__(self, lang='Python3', url=None):
        self.driver = webdriver.Firefox(
            executable_path=GECKO_DRIVER_PATH)
        if lang not in LANGUAGES:
            raise ValueError(f"Invalid language: {lang}")
        self.lang = lang
        self.url = url

    @property
    def lang_ix(self):
        return LANGUAGES.index(self.lang)

    def goto_new_problem_url(self, driver):
        """Get the URL of a problem we haven't solved yet."""
        already_solved = self.already_solved()
        while True:
            # Fetch random problem
            driver.get(self.url or self.RANDOM_PROBLEM_URL)

            # Get question id
            id_ = -1
            for __ in range(self.MAX_TRIES):
                try:
                    element = driver.find_element_by_id(
                        id_='question-title')
                    id_ = re.search(r'[0-9]+', element.text)[0]
                    break
                except NoSuchElementException:
                    time.sleep(1)

            # Return if URL was specified or random and not already solved
            if self.url or (id_ not in already_solved):
                return

    def parse_new_problem(self):
        """Parse a single problem page into a file."""
        driver = self.driver

        try:
            self.goto_new_problem_url(driver)

            # Get number and name
            element = driver.find_element_by_id('question-title')
            id_, name = element.text.split('.')

            # Get description
            element = driver.find_element_by_class_name('content__u3I1')
            description = element.text

            # Get code skeleton
            elements = []
            for __ in range(self.MAX_TRIES):
                try:
                    driver.find_element_by_css_selector(  # Open lang list
                        '#lang-select .ant-select-selection__rendered').click()
                    xpath = f'/html/body/div[5]/div/div/div/ul/li[{self.lang_ix + 1}]'
                    driver.find_element(By.XPATH, xpath).click()
                    elements = driver.find_elements_by_class_name('CodeMirror-line')
                    break
                except (ElementClickInterceptedException, NoSuchElementException,
                        ElementNotInteractableException):
                    time.sleep(1)

            code_skeleton = '\n'.join([e.text for e in elements])

            # Write file
            lcp = LeetCodeProblem(
                id_, name, driver.current_url, description, code_skeleton,
                lang=self.lang)
            out_path = lcp.write_file()

        finally:
            # Close browser
            driver.close()

        return out_path

    @staticmethod
    def already_solved():
        """Gets a list of problems we've already solved."""
        modules = [
            os.path.basename(file)
            for file in glob(os.path.join(SOL_DIR, '*py'))]
        matches = [re.search(r'(?<=lc_)[0-9]+', s) for s in modules]
        return [match[0] for match in matches if match]


class LeetCodeProblem:
    def __init__(self, id_, name, url, description, code_skeleton,
                 lang='Python3'):
        self.id = id_
        self.name = self.process_name(name)
        self.url = url
        self.raw_description = description
        self.description = self.parse_description(description)
        self.code_skeleton = code_skeleton
        self.lang = lang

        # Calculated
        self.method_name = self.method_name()
        self.test_cases = self.test_cases()

    def method_name(self):
        """Parse the method name from the code skeleton."""
        p = dict(zip(LANGUAGES, FUNCTION_SIGS)).get(self.lang)
        try:
            return re.search(p, self.code_skeleton)[1]
        except (TypeError, IndexError):
            return 'unknownmethodname'

    def test_cases(self):
        """Parse test cases from the description."""
        test_cases = []
        for line in self.raw_description.split('\n'):
            if line.strip().startswith('Input'):
                test_cases.append([self.parse_io(line)])
            elif line.strip().startswith('Output'):
                try:
                    test_cases[-1].append(self.parse_io(line))
                except IndexError:
                    pass
        s = ',\n        '.join(str(pair) for pair in test_cases)
        return s

    @staticmethod
    def parse_description(description):
        # Wrap text
        lines = description.split('\n')
        chunks = ['\n'.join(textwrap.wrap(line, width=72)) for line in lines]
        text = '\n\n'.join(chunks)

        # Cap to two line breaks
        text = re.sub(r'\n{3,}', '\n\n', text)

        # Cap to one line break inside examples
        for flag in ('Input', 'Output', 'Explanation'):
            text = text.replace(f'\n\n{flag}', f'\n{flag}')

        # Fix funky indentation
        for flag in ('Example', 'Note'):
            text = re.sub(f'\n[ ]+{flag}', f'\n{flag}', text)

        return text

    @staticmethod
    def parse_io(line):
        line = line.replace('Input:', '').replace('Output:', '').strip()
        try:
            return json.loads(line)
        except json.decoder.JSONDecodeError:
            pass
        if '=' in line:
            return f'dict({line})'  # Usually in dict format
        else:
            return line

    @staticmethod
    def process_name(name):
        return name.strip().lower().replace(' ', '_').replace('-', '_')

    def write_file(self):
        ext = dict(zip(LANGUAGES, EXTENSIONS)).get(self.lang)
        filename = f'lc_{self.id}_{self.name}.{ext}'
        template_path = os.path.join(TEMPLATE_DIR, self.lang)
        with open(template_path) as f:
            template = f.read()

        # Format text
        text = template.format(**self.__dict__)
        text = re.sub(r"'(dict\([^)]*\))'", r"\1", text)

        out_path = os.path.join(SOL_DIR, filename)
        with open(out_path, 'w') as f:
            f.write(text)

        return out_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', '-l', type=str, default='Python3',
                        help='the desired solution language, case-insensitive')
    parser.add_argument('--url', '-u', type=str, default=None,
                        help='the desired problem URL, default random')
    args = parser.parse_args()
    language = LANGUAGES[
        [l.lower() for l in LANGUAGES].index(args.language.lower())]

    self = LeetCodeScraper(lang=language, url=args.url)
    path = self.parse_new_problem()
    print(path)


if __name__ == '__main__':
    main()
