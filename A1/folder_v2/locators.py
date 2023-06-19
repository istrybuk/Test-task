class ShopPageLocators:
    BTN_CLOSE_COOKIE = ("xpath", "//button[@class='button button--primary cookie-panel-button']")
    BTN_GO_PURCHASE = ("xpath", "//a[contains(@class, 'button--centered')]")
    BLOCK_SELECT_INFO = ("class name", "select2-selection__rendered")

    PAYMENT_OPTIONS = ("class name", "select2-results__option")
    PHONE_PAGE_HEADER = ("xpath", "//h1[contains(@class, 'h--1')]")
    NAME_SELECTED_PAYMENT = ("xpath", "//span[@class='select2-selection__rendered']")
    BTN_LOGIN_TO_BUY = ("xpath", "//button[contains(@class, 'primary button--large')]")


class ValidDataConfig:
    SHOP_PAGE_LINK = "https://www.a1.by/ru/shop/c/phones"
    TEXT_PAYMENT_TERMS = "6 мес"
    TEXT_BTN_LOGIN_AND_BUY = "Войти и купить"
