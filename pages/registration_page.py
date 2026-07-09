import allure
from pages.base_page import BasePage
from locators.locators import RegistrationLocators, LoginLocators


class RegistrationPage(BasePage):

    @allure.step("Заполнение формы регистрации")
    def register(self, name, last_name, user_name, email, password):
        self.send_keys(RegistrationLocators.NAME_INPUT, name)
        self.send_keys(RegistrationLocators.LAST_NAME_INPUT, last_name,)
        self.send_keys(RegistrationLocators.USER_NAME_INPUT, user_name)
        self.send_keys(RegistrationLocators.EMAIL_INPUT, email)
        self.send_keys(RegistrationLocators.PASSWORD_INPUT, password)
        self.click_element(RegistrationLocators.REGISTER_BUTTON)

    @allure.step("Заполнение формы регистрации и проверка неактивности кнопки Создать аккаунт")
    def invalid_register(self, name, last_name, user_name, email, password):
        self.send_keys(RegistrationLocators.NAME_INPUT, name)
        self.send_keys(RegistrationLocators.LAST_NAME_INPUT, last_name,)
        self.send_keys(RegistrationLocators.USER_NAME_INPUT, user_name)
        self.send_keys(RegistrationLocators.EMAIL_INPUT, email)
        self.send_keys(RegistrationLocators.PASSWORD_INPUT, password)
        disabled_attr = self.get_attribute(RegistrationLocators.REGISTER_BUTTON, "disabled")
        return disabled_attr

    @allure.step("Клик по ссылке 'Создать аккаунт'")
    def click_register_link(self):
        self.click_element(RegistrationLocators.REGISTER_LINK)

    @allure.step("Проверка отображения формы авторизации")
    def is_login_form_visible(self):
        return self.is_element_visible(LoginLocators.LOGIN_BUTTON)
