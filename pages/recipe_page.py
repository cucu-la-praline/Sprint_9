import time

from selenium.webdriver.support import expected_conditions as EC

import allure
from pathlib import Path
import os
from data.data import Files
from pages.base_page import BasePage
from locators.locators import RecipeLocators


class RecipePage(BasePage):

    @allure.step("Заполнение формы создания рецепта")
    def create_recipe(self, name, description, ingredient, mass, cooking_time, filename):
        self.fill_recipe_basic_info(name, description, cooking_time)
        self.add_ingredient(ingredient, mass)
        self.upload_image(filename)
        self.click_element(RecipeLocators.SUBMIT_BUTTON)

    @allure.step("Невалидное заполнение формы создания рецепта")
    def create_recipe_whithout_ingredient(self, name, description, cooking_time, filename):
        self.fill_recipe_basic_info(name, description, cooking_time)
        self.upload_image(filename)

    @allure.step("Невалидное заполнение формы создания рецепта")
    def create_recipe_whithout_name(self, description, ingredient, mass, cooking_time, filename):
        self.send_keys(RecipeLocators.DESCRIPTION_INPUT, description)
        self.send_keys(RecipeLocators.COOKING_TIME_INPUT, cooking_time)
        self.add_ingredient(ingredient, mass)
        self.upload_image(filename)

    @allure.step("Заполнение основной информации о рецепте")
    def fill_recipe_basic_info(self, name, description, cooking_time):
        self.send_keys(RecipeLocators.NAME_INPUT, name)
        self.send_keys(RecipeLocators.DESCRIPTION_INPUT, description)
        self.send_keys(RecipeLocators.COOKING_TIME_INPUT, cooking_time)

    @allure.step("Добавление ингредиента и его массы")
    def add_ingredient(self, ingredient, mass):
        self.send_keys(RecipeLocators.INGREDIENT_INPUT, ingredient)
        self.click_element(RecipeLocators.ingredient_in_grid(ingredient))
        self.send_keys(RecipeLocators.INGREDIENT_MASS_INPUT, mass)
        self.click_element(RecipeLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Загрузка изображения")
    def upload_image(self, filename):
        file_path = Files().get_file(filename)
        self.send_keys_without_clear(RecipeLocators.IMAGE_INPUT, file_path)

    @allure.step("Ожидание загрузки страницы рецепта")
    def wait_for_recipe_page(self):
        self.is_element_visible(RecipeLocators.SINGLE_RECIPE_CARD)
        self.is_element_visible(RecipeLocators.SINGLE_RECIPE_IMAGE)

    @allure.step("Получение названия созданного рецепта")
    def is_recipe_card_page_open(self):
        self.is_element_visible(RecipeLocators.SINGLE_RECIPE_CARD)
        return self.check_exists(RecipeLocators.SINGLE_RECIPE_CARD)

    @allure.step("Получение данных об активности кнопки Создать рецепт")
    def is_create_recipe_disabled(self):
        disabled_attr = self.get_attribute(RecipeLocators.SUBMIT_BUTTON, "disabled")
        return disabled_attr

    @allure.step("Получение названия созданного рецепта")
    def is_recipe_card_title(self):
        return self.get_text(RecipeLocators.SINGLE_CARD_TITLE)
