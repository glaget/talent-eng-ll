import pytest


@pytest.mark.usefixtures("github_api")
class TestGitHub:
    def test_user_info_check_if_returned(self, github_api):
        res = github_api.user_info()
        assert len(res) > 0

    def test_list_repositories(self, github_api):
        res = github_api.list_repositories_per_user()
        assert len(res) > 0

    def test_find_repository_by_repo_name(self, github_api, repo_name):
        res = github_api.find_repository_by_repo_name(repo_name)
        assert res["total_count"] > 0

    def test_remove_repository(self, github_api, repo_name):
        res_before = github_api.list_repositories_per_user()
        github_api.remove_repository(repo_name)
        res_after = github_api.list_repositories_per_user()

        assert (len(res_before) - len(res_after)) == 1

    def test_create_repository(self, github_api, repo_name):
        github_api.create_repository(repo_name + "t", "")
        res = github_api.list_repositories_per_user()
        github_api.remove_repository(repo_name + "t")

        filtered_results = [i for i in res if i["name"] == repo_name + "t"]
        assert len(filtered_results) > 0
