import time
from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from src.applications.base_ui_app import BaseUIApp
from src.config.config import config


class GitHubUI(BaseUIApp):
    def __init__(self):
        super().__init__()
        pass

    def open_base_page(self):
        self.open_page(config["GITHUB_UI_URL"])

    def goto_login_page(self):
        url = urljoin(config["GITHUB_UI_URL"], "/login")
        self.open_page(url)
        time.sleep(2)

    def login(self, username, password):
        self.enter_text(By.ID, "login_field", username)
        self.enter_text(By.ID, "password", password)
        self.click(By.NAME, "commit")
        time.sleep(2)

    def logout(self):
        pass
