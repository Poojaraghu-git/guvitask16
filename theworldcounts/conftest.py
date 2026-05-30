import base64

import pytest
import pytest_html

from drivers.driver_factory import DriverFactory
from utilities.json_helper import JsonHelper
from utilities.logger_helper import LoggerHelper

logger = LoggerHelper.get_logger()

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="test",
                     help="environment to run")


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    logger.info(f"Running the test in {env} environment")
    return JsonHelper.get_config(env)

@pytest.fixture(scope="session")
def browser(config):
    browser = config["browser"]
    return browser


@pytest.fixture(scope="function")
def driver(browser, config):
    logger.info(f"Launching the {browser} browser")
    driver = DriverFactory.get_driver(browser)
    url = config["base_url"]
    driver.get(url)
    logger.info(f"Launching the {url} url")
    yield driver
    DriverFactory.quit_driver()