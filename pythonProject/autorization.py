from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/Chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://qa.neapro.site/login')
driver.find_element(By.CSS_SELECTOR,".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR,".fieldset:nth-child(1) input").send_keys("sav105@yandex.ru")
driver.find_element(By.CSS_SELECTOR,".fieldset:nth-child(2) input").click()
driver.find_element(By.CSS_SELECTOR,".fieldset:nth-child(2) input").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR,".btn").click()