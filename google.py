from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.google.com")
input_element = driver.find_element_by_name("q")
input_element.send_keys("filetype:txt intext:@gmail.com intext:Facebook intext:password")
input_element.submit()

