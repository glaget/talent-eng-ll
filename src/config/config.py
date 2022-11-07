from typing import Any, List
from config_provider import OSConfigProvider, JSONConfigProvider
from config_provider import BaseProviderClass, DummyConfigProvider


class Config:
    """
    Holds all the settings of your framework
    """
    def __init__(self, config_providers: List[BaseProviderClass]) -> None:
        """Initializes the configuration file. Registers configuration item
           names here via _register method.

        Args:
            config_providers (List[BaseProviderClass]): List of configuration
            providers, in order of precedence.
        """
        self.config_providers = config_providers

        self.conf_dict = {}
        self._register("BASE_URL")
        self._register("SQL_CONNECTION_STRING")
        self._register("KEY")
        # self._register("NOSQL_CONNECTION_STRING")

    def get(self, item_name: str) -> Any:
        """Get previously registered item_name from configuration providers.

        Args:
            item_name (str): Item to get from configuration providers.

        Returns:
            Any: Value from the configuration provider.
        """
        return self.conf_dict[item_name]

    def _register(self, item_name: str) -> None:
        """Register item_name to later get the value. The function will verify
           if any of the configuration providers have the item, in order that
           was specified when instancing the class.

        Args:
            item_name (str): Item to register and verify from configuration
                             providers.

        Raises:
            KeyError: Raised when no configuration provider has the item_name
                      available
        """
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return
        raise KeyError(f"Key {item_name} "
                       "not found in any of the configuration providers")


if __name__ == "__main__":
    config = Config([OSConfigProvider, JSONConfigProvider, DummyConfigProvider])
    print(config.get("BASE_URL"))
    print(config.get("KEY"))
    # print(config.get("NOSQL_CONNECTION_STRING"))