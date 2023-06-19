import pytest
from ShopPages import ShopPage
from locators import ValidDataConfig


@pytest.mark.parametrize("test", [f"test-{i}" for i in range(1, 2)])
def test_buy_phone_payment_6_months(browser, test):
    browser = browser
    link = ValidDataConfig.SHOP_PAGE_LINK
    shop_page_a1 = ShopPage(browser, link)
    shop_page_a1.open()
    shop_page_a1.click_btn_close_cookie()
    shop_page_a1.selection_random_phone()
    shop_page_a1.click_btn_go_purchase()
    shop_page_a1.initialization_block_payment()
    shop_page_a1.terms_choice_of_payment()
    shop_page_a1.name_title()
    shop_page_a1.click_login_and_buy()
