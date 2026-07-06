from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import allure


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self._default_wait_time = timeout
        self.wait = WebDriverWait(driver, timeout)

    def _get_implicit_wait_time(self) -> int:
        """
        Получение текущего значения неявного ожидания
        """
        return self._default_wait_time

    def click_element(self, locator, timeout=10):
        with allure.step(f"Клик по элементу: {locator}"):
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", element)
            try:
                element.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text, timeout=10):
        with allure.step(f"Ввод текста '{text}' в поле: {locator}"):
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)

    def send_keys_without_clear(self, selector: tuple, text: str, allure_text="Вводим текст"):
        """
        Ввести текст в поле для ввода без очистки
        :param selector: Селекторы в виде кортежа (By.*, "селектор")
        :param text: Вводимый текст
        :param allure_text: Текст для отчета (По умолчанию выводится 'Ввести текст: text')
        """
        with allure.step(f"{allure_text}: {text}"):
            self.driver.find_element(*selector).send_keys(text)

    def check_exists(self, selector: tuple, time=1) -> bool:
        """
        Проверка на присутствие элемента на странице
        :param selector: селектора объекта в виде кортежа (By.*, "селектор")
        :param time: Время ожидания отсутствия элемента
        :return: False - если элемент отсутствует и True - если элемент присутствует
        """
        current_wait = self._get_implicit_wait_time()

        try:
            self.driver.implicitly_wait(time)
            self.driver.find_element(*selector)
            return True
        except NoSuchElementException:
            return False
        finally:
            # Восстанавливаем стандартное ожидание
            self.driver.implicitly_wait(current_wait)

    def get_text(self, locator, timeout=10):
        with allure.step(f"Получение текста из элемента: {locator}"):
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.text

    def is_element_visible(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_url_contains(self, url_part, timeout=10):
        with allure.step(f"Ожидание URL содержащего: {url_part}"):
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.url_contains(url_part))

    def get_attribute(self, locator, value: str):
        return self.driver.find_element(*locator).get_attribute(value)
