from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("http://the-internet.herokuapp.com/inputs")

search_field = "input[type='number']"

input_number = driver.find_element(By.CSS_SELECTOR, search_field)

input_number.send_keys("Sky")
input_number.clear()

input_number.send_keys("Pro")

sleep(3)

driver.quit()