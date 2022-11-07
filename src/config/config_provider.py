import json
import pathlib
import os
from typing import Any


class BaseProviderClass:
    """
    Abstract provider class.
    """
    @staticmethod
    def get(item_name: str) -> Any:
        """Abstract get method. Provides value from configuration source.
        When not implemented will raise NotImplementedError.

        Args:
            item_name (str): Item to get from configuration.

        Raises:
            NotImplementedError: Raises when the method is not implemented.

        Returns:
            Any: Value from the configuration.
        """
        raise NotImplementedError("get method is not implemented")


class OSConfigProvider(BaseProviderClass):
    """
    OS enviroment variable configuration provider
    """
    @staticmethod
    def get(item_name: str) -> Any:
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
    cached_files = {}

    @classmethod
    def _read_config(self, config_path: pathlib.Path) -> dict:
        """Reads configuration file.

        Args:
            config_path (pathlib.Path): Path to JSON configuration file.

        Returns:
            dict: Dictionary containing all the key-value pairs from
                  configuration.
        """
        config_path_stats = config_path.lstat()
        # check if cached file is available
        if str(config_path) in self.cached_files:
            config_file = self.cached_files[str(config_path)]
            # check if modification time (ns) is lower or equal,
            # if yes, we can access the cache
            if config_path_stats.st_mtime <= config_file["mtime"]:
                return config_file["data"]
        # cache is unavailable - read the file
        with open(config_path) as json_file:
            # update the cached files dict with most up to date info
            self.cached_files.update({str(config_path): {
                "mtime": config_path_stats.st_mtime,
                "data": json.load(json_file)
            }})
            return self.cached_files[str(config_path)]["data"]

    @staticmethod
    def get(item_name: str) -> Any:
        """Provides value from configuration source based on the item_name.

        Args:
            item_name (str): Item to get from configuration.

        Returns:
            Any: Value from the configuration.
        """
        root_path = pathlib.Path(".").parent.parent.parent
        path = root_path/"envs_configs"/"devs.json"
        value = JSONConfigProvider._read_config(path)
        return value.get(item_name)


class DummyConfigProvider(BaseProviderClass):
    """
    Dummy configuration provider. Values provided by this provider
    are hardcoded.
    """
    @staticmethod
    def get(item_name: str) -> Any:
        """Provides value from configuration source based on the item_name.

        Args:
            item_name (str): Item to get from configuration.

        Returns:
            Any: Value from the configuration.
        """
        values = {
            "KEY": "12kfm33md#!@k123"
        }
        return values.get(item_name)
