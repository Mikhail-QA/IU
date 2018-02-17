from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox
driver.get("http:ya.ru")
driver.implicitly_wait(30)
inputField = driver.find_element_by_name("text")
inputField.send_keys("Selenium")
inputField.send_keys(Keys.RETURN)
driver.close()