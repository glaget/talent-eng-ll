from .github_urls import Urls
from src.config.config import config
from urllib.parse import urljoin
import json
import requests


class GitHubApi:
    def __init__(self):
        self.base_url = config["GITHUB_BASE_URL"]
        self._session = requests.Session()
        # set default headers here
        self._session.headers.update({"Accept": "application/vnd.github+json"})
        # no need to login, since we have the token, pass it into session
        self._session.auth = (config["GITHUB_USERNAME"], config["GITHUB_TOKEN"])
        self.current_user = config["GITHUB_USERNAME"]

    def _create_url(self, stem):
        return urljoin(self.base_url, stem)

    def _get_and_return_dict(self, *args, **kwargs):
        res = self._session.get(*args, **kwargs)
        res.raise_for_status()
        return res.json() if len(res.text) > 0 else {}

    def _post_and_return_dict(self, *args, **kwargs):
        res = self._session.post(*args, **kwargs)
        res.raise_for_status()
        return res.json() if len(res.text) > 0 else {}

    def _delete_and_return_dict(self, *args, **kwargs):
        res = self._session.delete(*args, **kwargs)
        res.raise_for_status()
        return res.json() if len(res.text) > 0 else {}

    def user_info(self):
        return self._get_and_return_dict(url=self._create_url(Urls.user))

    def create_repository(self, repo_name: str, description: str):
        return self._post_and_return_dict(url=self._create_url(Urls.create_repository),
                                          data=json.dumps({"name": repo_name,
                                                           "description": description,
                                                           "private": False}))
    
    def list_repositories_per_user(self, username=None):
        if username is None:
            username = self.current_user
        formatted_url = Urls.list_repositories_per_user.format_map({"username": username})
        return self._get_and_return_dict(url=self._create_url(formatted_url))

    def remove_repository(self, repo_name: str, username=None):
        # if no username provided, assume current user
        if username is None:
            username = self.current_user
        formatted_url = Urls.remove_repository.format_map({"username": username, "repo_name": repo_name})
        return self._delete_and_return_dict(url=self._create_url(formatted_url))

    def find_repository_by_repo_name(self, repo_name: str):
        return self._get_and_return_dict(url=self._create_url(Urls.search_repositories),
                                         params={"q": repo_name})
