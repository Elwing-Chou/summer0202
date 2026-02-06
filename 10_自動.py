# no module named distutils: pip install --upgrade setuptools
import undetected_chromedriver as uc
import time
import re
import os
import urllib.request as req
import urllib.parse as parse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    driver = uc.Chrome(version_main=144, use_subprocess=False)
    driver.get('https://www.google.com/')
    driver.maximize_window()

    time.sleep(5)
    driver.quit()


    time.sleep(5)
    driver.quit()