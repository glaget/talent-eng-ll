from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseUIApp:
    def __init__(self):
        self.service_obj = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service_obj)
        self.driver.maximize_window()
        pass

    def get_element(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value)

    def click(self, locator_type, locator_value):
        el = self.get_element(locator_type, locator_value)
        el.click()

    def enter_text(self, locator_type, locator_value, text):
        el = self.get_element(locator_type, locator_value)
        el.send_keys(text)

    def get_title(self):
        return self.driver.title

    def open_page(self, url):
        self.driver.get(url)
