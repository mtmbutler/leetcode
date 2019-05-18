"""An entry point script for the problem scraper."""

import argparse
import os
import subprocess
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    __, unknown = parser.parse_known_args()
    scrape_path = os.path.join(
        os.path.dirname(__file__), 'scrape', 'lc_scraper.py')
    cmd = subprocess.run([sys.executable, scrape_path, *unknown])
