import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password, expected_title", [
        ("student", "Password123", "Logged In Successfully"),
        ("invalidUser", "invalidPass", "Test Login")
    ])
    def test_login_scenarios(self, username, password, expected_title):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        assert expected_title in self.driver.page_source