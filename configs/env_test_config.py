import os
from attr import dataclass
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

# Звгрузка из .env
load_dotenv()

@dataclass
class EnvTestConfig:
    """Переменные для тествого окружения"""
    BY_MAP = {
        "css": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "id": By.ID,
    }

    MAIN_PAGE_URL = os.getenv("MAIN_PAGE_URL")
    BY_LOCATOR = BY_MAP[os.getenv("BY_LOCATOR")]
    ABOUT_LINK = os.getenv("ABOUT_LINK")
    MORE_INFO_LINK = os.getenv("MORE_INFO_LINK")
    CONTACTS_LINK = os.getenv("CONTACTS_LINK")
    CASES_LINK = os.getenv("CASES_LINK")
    REVIEWS_LINK = os.getenv("REVIEWS_LINK")
    MAIN_LINK = os.getenv("MAIN_LINK")
    SPECIALISTS_LINK = os.getenv("SPECIALISTS_LINK")
    POPUP_NDA_HOOK = os.getenv("POPUP_NDA_HOOK")
    POPUP_MAGNIT_HOOK = os.getenv("POPUP_MAGNIT_HOOK")
    POPUP_SPYCLUB_HOOK = os.getenv("POPUP_SPYCLUB_HOOK")
    POPUP_MYFORM_HOOK = os.getenv("POPUP_MYFORM_HOOK")
    PRIVACY_LINK = os.getenv("PRIVACY_LINK")
    ASSISTANT_LINK = os.getenv("ASSISTANT_LINK")
    TELEGRAM_LINK = os.getenv("TELEGRAM_LINK")
    MAIL_TO_LINK = os.getenv("MAIL_TO_LINK")

config = EnvTestConfig()
