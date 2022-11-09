import json
import os
import pathlib
from typing import Any


class BaseProviderClass:
    """
    Abstract provider class.
    """

    def __getitem__(self, item_name: str) -> Any:
        """Abstract get method. Provides value from configuration source.
        When not implemented will raise NotImplementedError.

        Args:
            item_name (str): Item to get from configuration.

        Raises:
            NotImplementedError: Raises when the method is not implemented.

        Returns:
            Any: Value from the configuration.
        """
        raise NotImplementedError("__getitem__ method is not implemented")


class OSConfigProvider(BaseProviderClass):
    """
    OS enviroment variable configuration provider
    """

    def __getitem__(self, item_name: str) -> Any:
        """Provides value from configuration source based on the item_name.

        Args:
            item_name (str): Item to get from configuration.

        Returns:
            Any: Value from the configuration.
        """
        value = os.getenv(item_name)
        return value


class JSONConfigProvider(BaseProviderClass):
    """
    JSON configuration provider. Implements simple file caching mechanism.
    """

    def __init__(self, config_path: pathlib.Path):
        """Constructor for JSONConfigProvider. Automatically loads the
           configuration.

        Args:
            config_path (pathlib.Path): Path to JSON configuration file.
        """
        self.loaded_config_file = self._read_config(config_path)

    def _read_config(self, config_path) -> dict:
        """Reads configuration file.

        Args:
            config_path (pathlib.Path): Path to JSON configuration file.

        Returns:
            dict: Dictionary containing all the key-value pairs from
                  configuration.
        """
        with open(config_path) as json_file:
            return json.load(json_file)

    def __getitem__(self, item_name: str) -> Any:
        """Provides value from configuration source based on the item_name.

        Args:
            item_name (str): Item to get from configuration.

        Returns:
            Any: Value from the configuration.
        """
        value = self.loaded_config_file.get(item_name)
        return value


class DummyConfigProvider(BaseProviderClass):
    """
    Dummy configuration provider. Values provided by this provider
    are hardcoded.
    """

    def __getitem__(self, item_name: str) -> Any:
        """Provides value from configuration source based on the item_name.

        Args:
            item_name (str): Item to get from configuration.

        Returns:
            Any: Value from the configuration.
        """
        values = {"KEY": "12kfm33md#!@k123"}
        return values.get(item_name)
