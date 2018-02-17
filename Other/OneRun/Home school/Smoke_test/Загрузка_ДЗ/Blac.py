import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
    driver.wait = WebDriverWait(driver, 5)
    return driver


def HTTP_GET(driver):
    driver.get("https://web-dev01.interneturok.ru/school_landing")




if __name__ == "__main__":
    driver = init_driver()
    HTTP_GET(driver, "Selenium")
    time.sleep(5)
    driver.quit()