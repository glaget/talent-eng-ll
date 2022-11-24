from pytest import mark


@mark.usefixtures("user_fixture", "product_fixture")
class TestDatabaseConnection:
    def test_check_connected(self, database_provider_fixture):
        assert database_provider_fixture.connected and database_provider_fixture.tables is not None

    @mark.xfail
    def test_check_not_connected_while_connected(self, database_provider_fixture):
        # assume you're connected, due to fixture
        print(database_provider_fixture.connected)
        assert not database_provider_fixture.connected and database_provider_fixture.tables is None

    def test_add_user(self, database_provider_fixture, user_fixture):
        database_provider_fixture.tables["users"] += [user_fixture]
        assert user_fixture in database_provider_fixture.tables["users"]

    def test_remove_user(self, database_provider_fixture, user_fixture):
        database_provider_fixture.tables["users"] += [user_fixture]
        database_provider_fixture.tables["users"] = [
            u for u in database_provider_fixture.tables["users"] if not user_fixture
        ]
        assert user_fixture not in database_provider_fixture.tables["users"]

    def test_add_product(self, database_provider_fixture, product_fixture):
        database_provider_fixture.tables["products"] += [product_fixture]
        assert product_fixture in database_provider_fixture.tables["products"]

    def test_remove_product(self, database_provider_fixture, product_fixture):
        database_provider_fixture.tables["products"] += [product_fixture]
        database_provider_fixture.tables["products"] = [
            p for p in database_provider_fixture.tables["products"] if not product_fixture
        ]
        assert product_fixture not in database_provider_fixture.tables["products"]
