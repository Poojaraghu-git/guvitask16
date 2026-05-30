from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import logger


class BasePage:
    def __init__(self, driver):
        self.__driver = driver
    def get_web_driver_wait(self):
        return WebDriverWait(self.__driver, 10)

    def get_population_count(self, locator):
        element = self.get_web_driver_wait().until(EC.presence_of_element_located(locator))
        return element.text
