import os
import re
import time
from getpass import getuser
from glob import glob

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Find solutions directory
try:
    SOL_DIR = os.path.join(os.path.dirname(__file__), os.pardir, 'solutions')
except NameError:  # Running interactively from repo root
    SOL_DIR = os.path.join(os.getcwd(), 'solutions')


class LeetCodeScraper:
    RANDOM_PROBLEM_URL = (
        "https://leetcode.com/problems/random-one-question/all")
    GECKO_DRIVER_URL = (
        f"C:/Users/{getuser()}/Downloads/geckodriver.exe")
    MAX_TRIES = 5

    def __init__(self):
        pass

    def get_new_problem_url(self):
        """Parse the list page for a dict of problem #'s and urls."""
        driver = webdriver.Firefox(executable_path=self.GECKO_DRIVER_URL)
        already_solved = self.already_solved()
        while True:
            # Fetch random problem
            driver.get(self.RANDOM_PROBLEM_URL)

            # Get question id
            id_ = -1
            for __ in range(self.MAX_TRIES):
                try:
                    element = driver.find_element_by_id(id_='question-title')
                    id_ = re.search(r'[0-9]+', element.text)[0]
                    break
                except NoSuchElementException:
                    time.sleep(1)

            # Return url if not already solved
            if id_ not in already_solved:
                return driver.current_url

    def parse_problem(self, url):
        """Parse a single problem page."""
        pass

    def gen_script(self, url):
        """Write the skeleton Python script for a problem."""
        pass

    @staticmethod
    def already_solved():
        modules = [
            os.path.basename(file)
            for file in glob(os.path.join(SOL_DIR, '*py'))]
        return [re.search(r'(?<=lc_)[0-9]+', s)[0] for s in modules]


if __name__ == '__main__':
    self = LeetCodeScraper()
