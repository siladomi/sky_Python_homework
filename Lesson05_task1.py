from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("http://uitestingplayground.com/classattr")
button_click = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

button_click.click()

sleep(10)