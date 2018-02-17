import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\selenium\\chromedriver.exe")
driver.get("https://web-dev01.interneturok.ru/")
driver.maximize_window()
time.sleep(2)
actions = ActionChains(driver)
time.sleep(3)
actions.move_by_offset(443, 445).perform()
actions.click().perform()