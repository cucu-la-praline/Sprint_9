import os
import socket
import pytest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from data.test_data import generate_user_data, generate_recipe_data
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def base_url():
    """Базовый URL сервиса"""
    default_url = "https://foodgram-frontend-1.foodgram.education-services.ru/signin"
    return os.getenv("BASE_URL", default_url)


@pytest.fixture
def selenium_url():
    """URL для Selenoid"""
    return os.getenv("SELENOID_URL", "http://selenoid:4444/wd/hub")


def is_selenoid_running():
    """Проверяет, запущен ли Selenoid"""
    try:
        socket.create_connection(("localhost", 4444), timeout=1)
        return True
    except:
        return False


@pytest.fixture(scope="function")
def browser():
    """Фикстура браузера"""
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")  # Headless режим для CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")

    # Автоматически скачивает совместимую версию ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@pytest.fixture
def registered_user(browser, base_url):
    """Фикстура создания пользователя с автоудалением"""
    user_data = generate_user_data()
    browser.get(base_url)
    register_page = RegistrationPage(browser)
    register_page.click_register_link()
    register_page.register(
        user_data["name"],
        user_data["last_name"],
        user_data["user_name"],
        user_data["email"],
        user_data["password"]
    )

    register_page.wait_for_url_contains("signin")

    return user_data


@pytest.fixture
def login_user(browser, base_url, registered_user):
    """Фикстура авторизованного пользователя"""
    user_data = registered_user

    browser.get(base_url)
    login_page = LoginPage(browser)
    login_page.click_login_link()
    login_page.login(user_data["user_name"], user_data["password"])
    login_page.wait_for_main_page()
    return user_data


@pytest.fixture
def asset_path():
    """Путь к файлу изображения для тестов"""
    return Path(__file__).parent.parent / "assets" / "test_image.jpg"


@pytest.fixture
def recipe_data():
    """Данные для создания рецепта"""
    return generate_recipe_data()
