import pytest
import requests

from src.config.config import config
from src.models.product import Product
from src.models.tag import Tag
from src.models.user import User
from src.providers.dummy_providers import DummyDatabase
from src.applications.github_api import GitHubApi


@pytest.fixture(scope="class")
def user_fixture():
    user = User(config["SHARED_USER_NAME"], config["SHARED_EMAIL"])
    yield user
    del user


@pytest.fixture(scope="class")
def product_fixture():
    product = Product(
        "XBlock", 20, tags={Tag(config["DEFAULT_TAG_NAME"]), Tag("CONSOLE")}
    )
    yield product
    del product


@pytest.fixture(scope="session")
def database_provider_fixture():
    db = DummyDatabase(path=config["SQL_CONNECTION_STRING"])
    db.connect()
    yield db
    # dummy database clear
    db.tables = {"products": [], "users": []}
    db.disconnect()

@pytest.fixture(scope="class")
def repo_name():
    yield "test-repo-123123"


@pytest.fixture(scope="class")
def github_api(repo_name):
    github_api_instance = GitHubApi()
    github_api_instance.create_repository(repo_name, "")
    yield github_api_instance
    try:
        github_api_instance.remove_repository(repo_name)
    except requests.exceptions.HTTPError:
        pass
    del github_api_instance
