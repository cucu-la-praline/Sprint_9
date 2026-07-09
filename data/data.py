import random

from pathlib import Path
from faker import Faker

fake = Faker()
ingredients = ['сахар', 'мука', 'соль', 'карамель', 'сода']


def generate_user_data():
    return {
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "user_name": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
    }


def generate_recipe_data():
    return {
        "name": f"Тестовый рецепт {fake.word()}",
        "description": fake.text(max_nb_chars=200),
        "ingredient": str(random.choice(ingredients)),
        "mass": 10,
        "cooking_time": fake.random_int(min=10, max=120)
    }


def get_ingredient_from_list():
    """Возвращает ингредиент из списка для добавления"""
    return "Соль"


class Files:

    def __init__(self):
        # Корень проекта (папка, где находятся тесты)
        # Если файл utils находится в корне проекта
        self.project_root = Path(__file__).parent.parent
        self.assets_dir = self.project_root / "assets"

    def get_file(self, filename):
        """
        Получение пути к файлу из папки assets
        :param filename: имя файла (например, "test_image.png")
        :return: абсолютный путь к файлу
        """
        if filename is None:
            raise ValueError("Имя файла не может быть None")

        # Проверяем, что папка assets существует
        if not self.assets_dir.exists():
            raise FileNotFoundError(f"Папка assets не найдена: {self.assets_dir}")

        # Полный путь к файлу
        file_path = self.assets_dir / filename

        # Проверяем, что файл существует
        if not file_path.exists():
            # Выводим список доступных файлов для отладки
            available_files = list(self.assets_dir.glob("*"))
            raise FileNotFoundError(
                f"Файл '{filename}' не найден в {self.assets_dir}\n"
                f"Доступные файлы: {[f.name for f in available_files]}"
            )

        return str(file_path.absolute())