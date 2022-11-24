from src.config.config import config


def test_github_ui_go_to_login_page(github_ui_app):
    github_ui_app.goto_login_page()
    assert github_ui_app.get_title() == "Sign in to GitHub · GitHub"


def test_github_ui_login(github_ui_app):
    github_ui_app.goto_login_page()
    github_ui_app.login(config["GITHUB_UI_SHARED_USERNAME"], config["GITHUB_UI_SHARED_PASSWORD"])
    # if we stay on the same page, means the login did not work
    assert github_ui_app.get_title() == "GitHub"
