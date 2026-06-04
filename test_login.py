import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("standard_user", "secret_sauce", True),
        ("visual_user", "secret_sauce", True),
        ("error_user", "secret_sauce", True),
        ("performance_glitch_user", "secret_sauce", True),
        ("problem_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("standard_user", "secretsauce", False)
    ]
)
def test_login(page, username, password, expected):

    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login(username, password)

    if expected:
        assert "inventory" in page.url

    else:
        assert page.locator("[data-test='error']").is_visible()
