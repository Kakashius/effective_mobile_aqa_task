from selenium.common import TimeoutException
from configs.env_test_config import config
from pages.main_page import MainPage

import pytest
import allure

@allure.suite('Главная страница')
class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)

    @allure.feature("Открытие главной страницы")
    def test_open_main_page(self):
        self.main_page.open()
        assert self.main_page.get_current_url() == config.MAIN_PAGE_URL, \
            f"Должна быть открыта страница {config.MAIN_PAGE_URL}"

    @allure.feature("Шапка страницы")
    class TestMainPageHeader:

        @pytest.fixture(autouse=True)
        def setup(self, browser):
            self.main_page = MainPage(browser)

        @allure.title("Переход на главную страницу")
        def test_click_on_main_in_header(self):
            self.main_page.open()
            self.main_page.click_on_main_in_header()

        @allure.title("Переход в блок 'О нас'")
        def test_click_on_about_us_in_header(self):
            self.main_page.open()
            self.main_page.click_on_about_us_in_header()

        @allure.title("Переход в блок 'Услуги'")
        def test_click_on_more_info_in_header(self):
            self.main_page.open()
            self.main_page.click_on_more_info_in_header()

        @allure.title("Переход в блок 'Проекты'")
        def test_click_on_cases_in_header(self):
            self.main_page.open()
            self.main_page.click_on_cases_in_header()

        @allure.title("Переход в блок 'Отзывы'")
        def test_click_on_reviews_in_header(self):
            self.main_page.open()
            self.main_page.click_on_reviews_in_header()

        @allure.title("Переход в блок 'Контакты'")
        def test_click_on_contacts_in_header(self):
            self.main_page.open()
            self.main_page.click_on_contacts_in_header()

        @allure.title("Переход в блок 'Наш стек и подберем для вас'")
        def test_click_on_specialists_in_header(self):
            self.main_page.open()
            self.main_page.click_on_specialists_in_header()

    @allure.feature("Футер страницы")
    class TestMainPageFooter:

        @pytest.fixture(autouse=True)
        def setup(self, browser):
            self.main_page = MainPage(browser)

        @allure.title("Переход на главную страницу")
        def test_click_on_main_in_footer(self):
            self.main_page.open()
            self.main_page.click_on_main_in_footer()

        @allure.title("Переход на страницу политики конфиденциальности")
        def test_click_on_privacy_link_in_footer(self):
            self.main_page.open()
            self.main_page.click_on_privacy_link_in_footer()

    @allure.feature("Контент главной страницы")
    class TestMainPageContent:

        @pytest.fixture(autouse=True)
        def setup(self, browser):
            self.main_page = MainPage(browser)

        @allure.title("Переход в блок 'Услуги'")
        def test_click_on_more_info_in_content(self):
            self.main_page.open()
            self.main_page.click_on_more_info_in_content()

        @allure.title("Переход в блок 'Контакты'")
        def test_click_on_contacts_in_content(self):
            self.main_page.open()
            self.main_page.click_on_contacts_in_content()

        @allure.title("Переход на страницу политики конфиденциальности")
        def test_click_on_privacy_link_in_content(self):
            self.main_page.open()
            self.main_page.click_on_privacy_link_in_content()

        @allure.title("Открытие модального окна 'Остались вопросы?'")
        def test_click_on_my_form_in_content(self):
            self.main_page.open()
            self.main_page.click_on_my_form_in_content()

        @allure.title("Переход на ТГ поддержку")
        def test_click_on_assistant_in_content(self):
            self.main_page.open()
            self.main_page.click_on_assistant_in_content()

        @allure.title("Переход на Телеграм профиль")
        def test_click_on_telegram_link_in_content(self):
            self.main_page.open()
            self.main_page.click_on_telegram_link_in_content()

        @allure.title("Переход на страницу отправки письма на почту")
        def test_click_on_mail_to_link_in_content(self):
            self.main_page.open()
            self.main_page.click_on_mail_to_link_in_content()

        @allure.title("Открытие модального окна проекта Магнит")
        def test_click_on_magnit_case_popup_in_cases(self):
            self.main_page.open()
            for _ in range(10):
                try:
                    self.main_page.click_on_magnit_case_popup_in_cases()
                    return
                except TimeoutException:
                    self.main_page.click_on_next_slide_in_cases()
            raise AssertionError("Элемент не найден после 10 попыток")

        @allure.title("Открытие модального окна проекта Пятерочка")
        def test_click_on_spyclub_case_popup_in_cases(self):
            self.main_page.open()
            for _ in range(10):
                try:
                    self.main_page.click_on_spyclub_case_popup_in_cases()
                    return
                except TimeoutException:
                    self.main_page.click_on_next_slide_in_cases()
            raise AssertionError("Элемент не найден после 10 попыток")

        @allure.title("Открытие модального окна проекта NDA")
        def test_click_on_nda_case_popup_in_cases(self):
            self.main_page.open()
            for _ in range(10):
                try:
                    self.main_page.click_on_nda_case_popup_in_cases()
                    return
                except TimeoutException:
                    self.main_page.click_on_next_slide_in_cases()
            raise AssertionError("Элемент не найден после 10 попыток")
