from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://yandex.com/search/?text=test")


class Yandex:
    def __init__(self, query):
        self.driver = webdriver.Firefox()
        self.query = query

    def exec_query(self):
        self.driver.get(self.query)
        print("Query executed on yandex")