import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выберите браузер: chrome, firefox")

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument(f"--window-size={DEFAULT_WIDTH},{DEFAULT_HEIGHT}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(executable_path="/usr/local/bin/chromedriver")
        browser = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument(f"--window-size={DEFAULT_WIDTH},{DEFAULT_HEIGHT}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = GeckoService(executable_path="/usr/local/bin/geckodriver")
        browser = webdriver.Firefox(options=options, service=service)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
