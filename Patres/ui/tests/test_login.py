import pytest
from pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
    def test_valid_login(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()


        # Проверка успешного входа через URL
        assert driver.current_url == "https://www.saucedemo.com/inventory.html", \
            "После входа URL должен измениться на страницу товаров"

        # Проверка через видимость элемента (дополнительная)
        assert login_page.is_inventory_displayed(), "Страница товаров не загрузилась"
