import allure

from data.test_data import generate_user_data
from pages.login_page import LoginPage


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешная авторизация")
    def test_successful_login(self, browser, base_url, registered_user):
        browser.get(base_url)
        login_page = LoginPage(browser)
        user_data = registered_user

        with allure.step("Переход на страницу авторизации"):
            login_page.click_login_link()

        with allure.step("Заполнение формы авторизации"):
            login_page.login(user_data["user_name"], user_data["password"])

        with allure.step("Проверка перехода на главную страницу"):
            assert "recipes" in browser.current_url, "Переход на главную страницу выполнен"

        with allure.step("Проверка отображения кнопки 'Выход'"):
            assert login_page.is_logout_button_visible(), "Кнопка 'Выход' отображается"

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password_error(self, browser, base_url, registered_user):
        browser.get(base_url)
        login_page = LoginPage(browser)
        user_data = registered_user
        user_data["password"] = "wrong_password"

        login_page.click_login_link()
        login_page.login(user_data["email"], user_data["password"])

        assert "signin" in browser.current_url, "Осталась открыта страница авторизации"

    @allure.title("Авторизация с несуществующим пользователем")
    def test_login_nonexistent_user_error(self, browser, base_url):
        browser.get(base_url)
        login_page = LoginPage(browser)
        user_data = generate_user_data()

        login_page.click_login_link()
        login_page.login(user_data["email"], user_data["password"])

        assert "signin" in browser.current_url, "Осталась открыта страница авторизации"
