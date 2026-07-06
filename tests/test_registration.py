import allure
import pytest

from pages.registration_page import RegistrationPage
from data.test_data import generate_user_data


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

    @allure.title("Регистрация с незаполненными полями")
    @pytest.mark.parametrize("field_to_skip", ["name", "email", "password"])
    def test_registration_empty_fields_error(self, browser, base_url, field_to_skip):
        browser.get(base_url)
        register_page = RegistrationPage(browser)
        user_data = generate_user_data()

        if field_to_skip == "name":
            user_data["name"] = ""
        elif field_to_skip == "email":
            user_data["email"] = ""
        else:
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
