import json
import os
import re
import textwrap
import time
from getpass import getuser
from glob import glob

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException, ElementClickInterceptedException)
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Find directories and files
try:
    REPO_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
except NameError:  # Running interactively from repo root
    REPO_DIR = os.path.join(os.getcwd())
SOL_DIR = os.path.join(REPO_DIR, 'solutions')
TEMPLATE_PATH = os.path.join(REPO_DIR, 'scrape', 'template.txt')


class LeetCodeScraper:
    RANDOM_PROBLEM_URL = (
        "https://leetcode.com/problems/random-one-question/all")
    GECKO_DRIVER_PATH = (
        f"C:/Users/{getuser()}/Downloads/geckodriver.exe")
    MAX_TRIES = 5

    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path=self.GECKO_DRIVER_PATH)

    def goto_new_problem_url(self, driver):
        """Get the URL of a problem we haven't solved yet."""
        already_solved = self.already_solved()
        while True:
            # Fetch random problem
            driver.get(self.RANDOM_PROBLEM_URL)

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

            # Return if not already solved
            if id_ not in already_solved:
                return

    def parse_new_problem(self):
        """Parse a single problem page into a file."""
        driver = self.driver
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
                xpath = '/html/body/div[5]/div/div/div/ul/li[4]'  # Python 3
                driver.find_element(By.XPATH, xpath).click()
                elements = driver.find_elements_by_class_name('CodeMirror-line')
                break
            except (ElementClickInterceptedException, NoSuchElementException):
                time.sleep(1)

        code_skeleton = '\n'.join([e.text for e in elements])

        # Write file
        lcp = LeetCodeProblem(
            id_, name, driver.current_url, description, code_skeleton)
        out_path = lcp.write_file()

        # Close browser
        driver.close()

        return out_path

    @staticmethod
    def already_solved():
        """Gets a list of problems we've already solved."""
        modules = [
            os.path.basename(file)
            for file in glob(os.path.join(SOL_DIR, '*py'))]
        return [re.search(r'(?<=lc_)[0-9]+', s)[0] for s in modules]


class LeetCodeProblem:
    def __init__(self, id_, name, url, description, code_skeleton):
        self.id = id_
        self.name = self.process_name(name)
        self.url = url
        self.description = self.parse_description(description)
        self.code_skeleton = code_skeleton

        # Calculated
        self.method_name = self.method_name()
        self.test_cases = self.test_cases()

    def method_name(self):
        """Parse the method name from the code skeleton."""
        p = r'def ([^ ^_]+)\('
        try:
            return re.search(p, self.code_skeleton)[1]
        except (TypeError, IndexError):
            return 'unknownmethodname'

    def test_cases(self):
        """Parse test cases from the description."""
        test_cases = []
        found_input = False
        for line in self.description.split('\n'):
            if line.strip().startswith('Input'):
                test_cases.append([self.parse_io(line)])
            elif line.strip().startswith('Output'):
                try:
                    test_cases[-1].append(self.parse_io(line))
                except IndexError:
                    pass
        s = ',\n        '.join(str(tuple(pair)) for pair in test_cases)
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
        filename = f'lc_{self.id}_{self.name}.py'
        with open(TEMPLATE_PATH) as f:
            template = f.read()

        # Format text
        text = template.format(**self.__dict__)
        text = re.sub(r"'(dict\([^)]*\))'", r"\1", text)

        out_path = os.path.join(SOL_DIR, filename)
        with open(out_path, 'w') as f:
            f.write(text)

        return out_path


if __name__ == '__main__':
    self = LeetCodeScraper()
    path = self.parse_new_problem()
    os.startfile(path)
