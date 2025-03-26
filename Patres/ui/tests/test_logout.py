from pages.login_page import LoginPage
from pages.page_store import LogoutPage


class TestLogout:
    def test_successful_logout(self, driver):
        login_page = LoginPage(driver)
        logout_page = LogoutPage(driver)

        # Логин
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Выход
        logout_page.open_menu()
        logout_page.logout()

        # Проверки
        assert driver.current_url == "https://www.saucedemo.com/", \
            "После выхода URL должен вернуться на страницу входа"
