from selenium import webdriver
from selenium.webdriver.common.keys import Keys






driver = webdriver.Chrome('/home/fonsi/Descargas/chromedriver') 
#driver = webdriver.Firefox()
driver.get("https://www.google.com")
val = 10 # in seconds
driver.implicitly_wait(val)
elem = driver.find_element_by_name("input")
print(elem)
elem.send_keys(Keys.RETURN)
driver.close()
