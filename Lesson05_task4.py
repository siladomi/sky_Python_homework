from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("http://the-internet.herokuapp.com/login")

user_field = "username"
pass_field = "password"

input_user = driver.find_element(By.ID, user_field)
input_user.send_keys("tomsmith")

input_pas = driver.find_element(By.ID, pass_field)
input_pas.send_keys("SuperSecretPassword!")

button_click = driver.find_element(By.CSS_SELECTOR, "button.radius" )
button_click.click()
login_element = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-sign-in')]")

print("Текст плашки:", login_element.text)

sleep(3)

driver.quit()