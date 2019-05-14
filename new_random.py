import os
import shlex
import subprocess
import sys

if __name__ == '__main__':
    scrape_path = os.path.join(
        os.path.dirname(__file__),
        'scrape',
        'lc_scraper.py')
    cmd = shlex.split(f'"{sys.executable}" "{scrape_path}"')
    subprocess.call(cmd)
