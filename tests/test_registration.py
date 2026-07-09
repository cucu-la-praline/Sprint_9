import allure
import pytest

from pages.registration_page import RegistrationPage
from data.data import generate_user_data


@allure.feature("Регистрация")
class TestRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_successful_registration(self, browser, base_url):
        user_data = generate_user_data()
        browser.get(base_url)
        register_page = RegistrationPage(browser)

        with allure.step("Переход на страницу регистрации"):
            register_page.click_register_link()

        with allure.step("Заполнение формы регистрации"):
            register_page.register(
                user_data["name"],
                user_data["last_name"],
                user_data["user_name"],
                user_data["email"],
                user_data["password"]
            )

        with allure.step("Проверка перехода на страницу авторизации"):
            register_page.wait_for_url_contains("signin")
            assert "signin" in browser.current_url

        with allure.step("Проверка отображения формы авторизации"):
            assert register_page.is_login_form_visible(), "Форма авторизации не отображается"

    @allure.title("Регистрация с пустым полем имени")
    def test_registration_empty_name_error(self, browser, base_url):
        browser.get(base_url)
        register_page = RegistrationPage(browser)
        user_data = generate_user_data()
        user_data["name"] = ""

        register_page.click_register_link()
        disabled_attr = register_page.invalid_register(
            user_data["name"],
            user_data["last_name"],
            user_data["user_name"],
            user_data["email"],
            user_data["password"]
        )

        with allure.step("Проверка сообщения об ошибке"):
            assert disabled_attr == 'true'

    @allure.title("Регистрация с пустым полем email")
    def test_registration_empty_email_error(self, browser, base_url):
        browser.get(base_url)
        register_page = RegistrationPage(browser)
        user_data = generate_user_data()
        user_data["email"] = ""

        register_page.click_register_link()
        disabled_attr = register_page.invalid_register(
            user_data["name"],
            user_data["last_name"],
            user_data["user_name"],
            user_data["email"],
            user_data["password"]
        )

        with allure.step("Проверка сообщения об ошибке"):
            assert disabled_attr == 'true'

    @allure.title("Регистрация с пустым полем пароля")
    def test_registration_empty_password_error(self, browser, base_url):
        browser.get(base_url)
        register_page = RegistrationPage(browser)
        user_data = generate_user_data()
        user_data["password"] = ""

        register_page.click_register_link()
        disabled_attr = register_page.invalid_register(
            user_data["name"],
            user_data["last_name"],
            user_data["user_name"],
            user_data["email"],
            user_data["password"]
        )

        with allure.step("Проверка сообщения об ошибке"):
            assert disabled_attr == 'true'
