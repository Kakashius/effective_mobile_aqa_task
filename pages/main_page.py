from pages.base_page import BasePage
from configs.env_test_config import config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure

class MainPage(BasePage):

    # Уникальные локаторы страницы
    MY_FORM_LOCATOR = f'#sbs-572441941-1680515472080 a[href="{config.POPUP_MYFORM_HOOK}"]'
    ASSISTANT_LOCATOR = f'#sbs-572455122-1680667373456 a[href="{config.ASSISTANT_LINK}"]'
    TELEGRAM_LOCATOR = f'#sbs-572455122-1680681258647 a[href="{config.TELEGRAM_LINK}"]'
    MAIL_TO_LOCATOR = f'#sbs-572455122-1680667673466 a[href="{config.MAIL_TO_LINK}"]'
    NEXT_SLIDE_CASES_LOCATOR = '#rec572838727 button[aria-label="Следующий слайд"]'
    MAGNIT_POPUP_LOCATOR = f'a[href="{config.POPUP_MAGNIT_HOOK}"][tabindex="0"]'
    SPYCLUB_POPUP_LOCATOR = f'a[href="{config.POPUP_SPYCLUB_HOOK}"][tabindex="0"]'
    NDA_POPUP_LOCATOR = f'a[href="{config.POPUP_NDA_HOOK}"][tabindex="0"]'

    @allure.step("Нажать на 'Подробнее' на главной странице")
    def click_on_more_info_in_content(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec571993583 {self.MORE_INFO_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.MORE_INFO_LINK)), \
            f"URL должен быть {config.MORE_INFO_LINK}"
        assert self.is_element_presented("#rec572392832"), "На экране пользователя не отображается блок 'Услуги'"

    @allure.step("Нажать на 'Оставить заявку на сотрудничество' на главной странице")
    def click_on_contacts_in_content(self):
        self.driver.find_element(config.BY_LOCATOR, f"#rec572374517 {self.CONTACTS_LOCATOR}").click()
        assert WebDriverWait(self.driver, 10).until(ec.url_to_be(config.CONTACTS_LINK)), \
            f"URL должен быть {config.CONTACTS_LINK}"
        assert self.is_element_presented("#rec572455122"), "На экране пользователя не отображается блок 'Контакты'"

    @allure.step("Нажать на ссылку политики конфиденциальности на главной странице")
    def click_on_privacy_link_in_content(self):
        el = self.driver.find_element(config.BY_LOCATOR, f"#rec572455122 {self.PRIVACY_LOCATOR}")
        el.click()
        assert el.get_attribute("href") == config.PRIVACY_LINK, \
            f"Должна быть открыта страница {config.PRIVACY_LINK}"

    @allure.step("Нажать на 'Оставить заявку на консультацию' на главной странице")
    def click_on_my_form_in_content(self):
        self.driver.find_element(config.BY_LOCATOR, self.MY_FORM_LOCATOR).click()
        assert self.is_element_presented(F'div[data-tooltip-hook="{config.POPUP_MYFORM_HOOK}"]'), \
            "Должно быть открыто модальное окно 'Остались вопросы?'"

    @allure.step("Нажать на ссылку ТГ поддержки на главной странице")
    def click_on_assistant_in_content(self):
        el = self.driver.find_element(config.BY_LOCATOR, self.ASSISTANT_LOCATOR)
        el.click()
        assert el.get_attribute("href") == config.ASSISTANT_LINK, \
            f"Должен осуществиться переход по ссылке {config.ASSISTANT_LINK}"

    @allure.step("Нажать на ссылку контакта в Telegram на главной странице")
    def click_on_telegram_link_in_content(self):
        el = self.driver.find_element(config.BY_LOCATOR, self.TELEGRAM_LOCATOR)
        el.click()
        assert el.get_attribute("href") == config.TELEGRAM_LINK, \
            f"Должен осуществиться переход по ссылке {config.TELEGRAM_LINK}"

    @allure.step("Нажать на ссылку отправки письма на почту компании на главной странице")
    def click_on_mail_to_link_in_content(self):
        el = self.driver.find_element(config.BY_LOCATOR, self.MAIL_TO_LOCATOR)
        el.click()
        assert el.get_attribute("href") == config.MAIL_TO_LINK, \
            f"Должен осуществиться переход по ссылке {config.MAIL_TO_LINK}"

    @allure.step("Переключить на следующий слайд проектов в разделе 'проекты' на главной странице")
    def click_on_next_slide_in_cases(self):
        self.driver.find_element(config.BY_LOCATOR, self.NEXT_SLIDE_CASES_LOCATOR).click()

    @allure.step("Нажать на 'Подробнее' у проекта Магнит")
    def click_on_magnit_case_popup_in_cases(self):
        element = WebDriverWait(self.driver, 2).until(
            ec.visibility_of_element_located((config.BY_LOCATOR, self.MAGNIT_POPUP_LOCATOR))
        )
        element.click()
        assert self.is_element_presented(f'div[data-tooltip-hook="{config.POPUP_MAGNIT_HOOK}"]'), \
            "Должно быть открыто модальное окно проекта Магнит"

    @allure.step("Нажать на 'Подробнее' у проекта Пятерочка")
    def click_on_spyclub_case_popup_in_cases(self):
        element = WebDriverWait(self.driver, 2).until(
            ec.visibility_of_element_located((config.BY_LOCATOR, self.SPYCLUB_POPUP_LOCATOR))
        )
        element.click()
        assert self.is_element_presented(f'div[data-tooltip-hook="{config.POPUP_SPYCLUB_HOOK}"]'), \
            "Должно быть открыто модальное окно проекта Пятерочка"

    @allure.step("Нажать на 'Подробнее' у NDA проекта")
    def click_on_nda_case_popup_in_cases(self):
        element = WebDriverWait(self.driver, 2).until(
                    ec.visibility_of_element_located((config.BY_LOCATOR, self.NDA_POPUP_LOCATOR))
                )
        element.click()
        assert self.is_element_presented(f'div[data-tooltip-hook="{config.POPUP_NDA_HOOK}"]'), \
            "Должно быть открыто модальное окно NDA проекта"
