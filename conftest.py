import pytest

from src.config.config import config
from src.models.product import Product
from src.models.tag import Tag
from src.models.user import User
from src.providers.providers import DummyDatabase


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
