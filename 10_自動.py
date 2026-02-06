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

    name = "google"
    if not os.path.exists(name):
        os.makedirs(name)

    driver = uc.Chrome(version_main=144, use_subprocess=False)
    driver.get('https://www.google.com/')
    driver.maximize_window()

    # find_element/find_elements
    # 輸入搜尋文字並且enter
    e = driver.find_element(By.CLASS_NAME, "gLFyf")
    # click()/send_keys()
    e.send_keys("吉伊卡哇")
    e.send_keys(Keys.ENTER)
    time.sleep(3)
    # 點上面三個小按鈕 "圖片"
    driver.find_elements(By.CLASS_NAME, "C6AK7c")[2].click()
    time.sleep(3)
    # 找到每一個縮圖
    es = driver.find_elements(By.CLASS_NAME, "F0uyec")
    for e in es:
        # 點完以後休息三秒以後把旁邊跳出的大圖做下載
        e.click()
        time.sleep(3)
        # time.sleep(200)
        try:
            img = driver.find_element(By.CLASS_NAME, "iPVvYb")
            # get_attribute("href")/text
            src = img.get_attribute("src")
            print(src)
            h = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",

            }
            r = req.Request(src, headers=h)
            resp = req.urlopen(r)
            fp = name + "/" + str(time.time()) + ".jpg"
            f = open(fp, "wb")
            f.write(resp.read())
            f.close()
        except:
            print("放棄")

    time.sleep(5)
    driver.quit()
