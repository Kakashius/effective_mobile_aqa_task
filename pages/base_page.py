from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure

from configs.env_test_config import config

class BasePage(object):

    # Общие локаторы
    MAIN_LOCATOR = 'a[href="#main"]'
    ABOUT_US_LOCATOR = 'a[href="#about"]'
    MORE_INFO_LOCATOR = 'a[href="#moreinfo"]'
    CASES_LOCATOR = 'a[href="#cases"]'
    REVIEWS_LOCATOR = 'a[href="#Reviews"]'
    CONTACTS_LOCATOR = 'a[href="#contacts"]'
    SPECIALISTS_LOCATOR = 'a[href="#specialists"]'
    PRIVACY_LOCATOR = f'a[href="{config.PRIVACY_LINK}"]'


    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step(f"Открыть страницу {config.MAIN_PAGE_URL}")
    def open(self):
        self.driver.get(config.MAIN_PAGE_URL)

    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Блок отображается на экране пользователя")
    def is_element_presented(self, target_selector: str) -> bool:
        target_element = WebDriverWait(self.driver,10).until(
            ec.visibility_of_element_located((config.BY_LOCATOR, target_selector))
        )
        return target_element.is_displayed()

    @allure.step("Нажать на лого Effective mobile в шапке страницы")
    def click_on_main_in_header(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec573054532 {self.MAIN_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.MAIN_LINK)), \
            f"URL должен быть {config.MAIN_LINK}"
        assert self.is_element_presented("#rec571993583"), "На экране пользователя не отображается блок о компании"

    @allure.step("Нажать на 'О нас' в шапке страницы")
    def click_on_about_us_in_header(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec573054532 {self.ABOUT_US_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.ABOUT_LINK)), \
            f"URL должен быть {config.ABOUT_LINK}"
        assert self.is_element_presented("#rec572359627"), "На экране пользователя не отображается блок 'О нас'"

    @allure.step("Нажать на 'Услуги' в шапке страницы")
    def click_on_more_info_in_header(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec573054532 {self.MORE_INFO_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.MORE_INFO_LINK)), \
            f"URL должен быть {config.MORE_INFO_LINK}"
        assert self.is_element_presented("#rec572392832"), "На экране пользователя не отображается блок 'Услуги'"

    @allure.step("Нажать на 'Проекты' в шапке страницы")
    def click_on_cases_in_header(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec573054532 {self.CASES_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.CASES_LINK)), \
            f"URL должен быть {config.CASES_LINK}"
        assert self.is_element_presented("#rec572838727"), "На экране пользователя не отображается блок 'Проекты'"

    @allure.step("Нажать на 'Отзывы' в шапке страницы")
    def click_on_reviews_in_header(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec573054532 {self.REVIEWS_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.REVIEWS_LINK)), \
            f"URL должен быть {config.REVIEWS_LINK}"
        assert self.is_element_presented("#rec699930013"), "На экране пользователя не отображается блок 'Отзывы'"

    @allure.step("Нажать на 'Контакты' в шапке страницы")
    def click_on_contacts_in_header(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec573054532 {self.CONTACTS_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.CONTACTS_LINK)), \
            f"URL должен быть {config.CONTACTS_LINK}"
        assert self.is_element_presented("#rec572455122"), "На экране пользователя не отображается блок 'Контакты'"

    @allure.step("Нажать на кнопку 'Выбрать специалиста' в шапке страницы")
    def click_on_specialists_in_header(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec573054532 {self.SPECIALISTS_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.SPECIALISTS_LINK)), \
            f"URL должен быть {config.SPECIALISTS_LINK}"
        assert self.is_element_presented("#rec660927810"), "На экране пользователя не отображается блок 'Наш стек'"

    @allure.step("Нажать на название компании в футере страницы")
    def click_on_main_in_footer(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec572471347 {self.MAIN_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.MAIN_LINK)), \
            f"URL должен быть {config.MAIN_LINK}"
        assert self.is_element_presented("#rec571993583"), "На экране пользователя не отображается блок о компании"

    @allure.step("Нажать на ссылку политики конфиденциальности в футере страницы")
    def click_on_privacy_link_in_footer(self):
        el = self.driver.find_element(config.BY_LOCATOR, f"#rec572471347 {self.PRIVACY_LOCATOR}")
        el.click()
        assert el.get_attribute("href") == config.PRIVACY_LINK, \
            f"Должна быть открыта страница {config.PRIVACY_LINK}"

