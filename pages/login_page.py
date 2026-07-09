import allure
from pages.base_page import BasePage
from locators.locators import LoginLocators, RegistrationLocators, MainLocators


class LoginPage(BasePage):

    @allure.step("Заполнение формы авторизации")
    def login(self, user_name, password):
        self.send_keys(RegistrationLocators.EMAIL_INPUT, user_name)
        self.send_keys(RegistrationLocators.PASSWORD_INPUT, password)
        self.click_element(LoginLocators.LOGIN_BUTTON)
        self.wait_for_main_page()
        self.is_element_visible(MainLocators.RECIPES_TAB)

    @allure.step("Клик по ссылке 'Войти'")
    def click_login_link(self):
        self.click_element(LoginLocators.LOGIN_LINK)

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_main_page(self):
        """Ожидание, что главная страница полностью загружена"""
        self.is_element_visible(MainLocators.LOGOUT_BUTTON)

    @allure.step("Проверка отображения кнопки 'Выход'")
    def is_logout_button_visible(self):
        return self.is_element_visible(MainLocators.LOGOUT_BUTTON)
