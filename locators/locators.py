from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
    USER_NAME_INPUT = (By.XPATH, "//input[@name='username']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")


class LoginLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class MainLocators:
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выход')]")
    CREATE_RECIPE_TAB = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")
    RECIPES_TAB = (By.XPATH, "//a[contains(text(), 'Рецепты')]")


class RecipeLocators:
    NAME_INPUT = (By.XPATH, "//div[text()='Название рецепта']/parent::label/input")
    DESCRIPTION_INPUT = (By.XPATH, "//div[text()='Описание рецепта']/parent::label/textarea")
    INGREDIENT_INPUT = (By.XPATH, "//div[text()='Ингредиенты']/parent::label/input")
    INGREDIENT_MASS_INPUT = (By.XPATH, "//div[contains(@class, 'ingredientsAmountInputContainer')]/div/label/input")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/parent::label/input")
    IMAGE_INPUT = (By.XPATH, "//input[@type='file']")

    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]")

    SINGLE_RECIPE_CARD = (By.XPATH, "(//div[contains(@class, 'single-card')])[1]")
    SINGLE_RECIPE_IMAGE = (By.XPATH, "//img[contains(@class, 'single-card__image')]")
    SINGLE_CARD_TITLE = (By.XPATH, "//h1[contains(@class, 'single-card__title')]")

    @staticmethod
    def ingredient_in_grid(text):
        return By.XPATH, f"//div[text()='{text}']"
