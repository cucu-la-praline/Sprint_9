import allure

from data.data import generate_recipe_data
from pages.main_page import MainPage
from pages.recipe_page import RecipePage


@allure.feature("Создание рецепта")
class TestRecipe:

    @allure.title("Успешное создание рецепта")
    def test_create_recipe_success(self, browser, base_url, login_user, asset_path):
        browser.get(base_url)
        main_page = MainPage(browser)
        recipe_page = RecipePage(browser)
        _ = login_user
        recipe_data = generate_recipe_data()

        with allure.step("Переход на страницу создания рецепта"):
            main_page.go_to_create_recipe()

        with allure.step("Заполнение формы создания рецепта"):
            recipe_page.create_recipe(
                name=recipe_data["name"],
                description=recipe_data["description"],
                ingredient=recipe_data["ingredient"],
                mass=recipe_data["mass"],
                cooking_time=recipe_data["cooking_time"],
                filename="test_image.jpg"
            )

        assert recipe_page.is_recipe_card_page_open(), "Рецепт не отображается"

        assert recipe_data["name"] == recipe_page.is_recipe_card_title(), "Название рецепта не совпадает"

    @allure.title("Создание рецепта без названия")
    def test_create_recipe_without_name_error(self, browser, base_url, login_user, asset_path):
        browser.get(base_url)
        main_page = MainPage(browser)
        recipe_page = RecipePage(browser)
        recipe_data = generate_recipe_data()
        recipe_data["name"] = ""

        main_page.go_to_create_recipe()
        recipe_page.create_recipe_whithout_name(
            description=recipe_data["description"],
            ingredient=recipe_data["ingredient"],
            mass=recipe_data["mass"],
            cooking_time=recipe_data["cooking_time"],
            filename="test_image.jpg"
        )

        # Проверяем, что остались на странице создания
        assert "recipes/create" in browser.current_url
        assert 'true' == recipe_page.is_create_recipe_disabled()

    @allure.title("Создание рецепта без ингредиентов")
    def test_create_recipe_without_ingredients_error(self, browser, base_url, login_user, asset_path):
        browser.get(base_url)
        main_page = MainPage(browser)
        recipe_page = RecipePage(browser)
        recipe_data = generate_recipe_data()

        main_page.go_to_create_recipe()
        recipe_page.create_recipe_whithout_ingredient(
            name=recipe_data["name"],
            description=recipe_data["description"],
            cooking_time=recipe_data["cooking_time"],
            filename="test_image.jpg"
        )

        assert "recipes/create" in browser.current_url
        assert 'true' == recipe_page.is_create_recipe_disabled()
