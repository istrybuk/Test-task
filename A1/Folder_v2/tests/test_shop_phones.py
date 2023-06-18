from folder_v2.pages.shop_page import *


def test_buy_phone_payment_6_months(browser):
    link = ValidDataConfig.SHOP_PAGE_LINK
    page = ShopPage(browser, link)
    page.open()
    page.close_btn_cookie()
    page.select_random_purchase_on_shop()
    page.choice_payment_option()
    page.click_login_and_buy()
