from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.python.org")
sleep(10)
driver.close()
