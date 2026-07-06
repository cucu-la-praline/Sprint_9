import allure
from pages.base_page import BasePage
from locators.locators import MainLocators


class MainPage(BasePage):

    @allure.step("Переход на страницу создания рецепта")
    def go_to_create_recipe(self):
        self.click_element(MainLocators.CREATE_RECIPE_TAB)
        self.wait_for_url_contains("recipes/create")
