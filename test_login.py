import pytest


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

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    if expected:
        assert "inventory" in page.url

    else:
        assert page.locator("[data-test='error']").is_visible()