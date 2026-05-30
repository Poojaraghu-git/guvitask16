from selenium.webdriver.common.by import By

from conftest import logger
from page_object.base_page import BasePage


class TestPopulation:

    def test_population_count(self, driver):
        base_page = BasePage(driver)
        self.population = (By.XPATH, "//div[@class ='counter-ticker is-size-2-mobile']")
        try:
            while True:
                population_count = base_page.get_population_count(self.population)
                logger.info(f"(The world population count is:  {population_count})")
        except KeyboardInterrupt:
            print("\nStopped by user clicks (CTRL+C).")
            driver.quit()



