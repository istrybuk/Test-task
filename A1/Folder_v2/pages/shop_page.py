from .base_page import BasePage
from selenium.webdriver import ActionChains
import random


def search_value_in_elements(lst=None, param=None):
    if lst is None:
        return print("Параметры поиска не заданы")
    else:
        for string in lst:
            if param in string.text:
                return string
        else:
            print(f"Искомый элемент: \"{param}\" функции search_value_in_elements, не найден.")


class ShopPageLocators:
    BTN_CLOSE_COOKIE = ("xpath", '//button[@class="button button--primary cookie-panel-button"]')
    BTN_GO_PURCHASE = ("xpath", "//a[contains(@class, 'button--centered')]")
    BLOCK_SELECT = ("class name", "select2-selection__arrow")
    PAYMENT_OPTIONS = ("class name", "select2-results__option")
    PHONE_PAGE_HEADER = ("xpath", "//h1[contains(@class, 'h--1')]")
    NAME_SELECTED_PAYMENT = ("xpath", "//span[@class='select2-selection__rendered']")
    BTN_LOGIN_TO_BUY = ("xpath", "//button[contains(@class, 'primary button--large')]")


class ValidDataConfig:
    SHOP_PAGE_LINK = "https://www.a1.by/ru/shop/c/phones"
    TEXT_PAYMENT_TERMS = "6 мес"
    TEXT_BTN_LOGIN_AND_BUY = "Войти и купить"


class ShopPage(BasePage):
    def close_btn_cookie(self):
        """Закрыть окно с сообщением о cookie"""
        self.browser.find_element(*ShopPageLocators.BTN_CLOSE_COOKIE).click()

    def select_random_purchase_on_shop(self):
        """Выбрать случайный телефон, нажать на кнопку 'Перейти к покупке'"""
        action = ActionChains(self.browser)
        btn_go_to_purchase = self.browser.find_elements(*ShopPageLocators.BTN_GO_PURCHASE)
        random_btn_go_to_purchase = random.choice(btn_go_to_purchase[:])
        action.move_to_element(random_btn_go_to_purchase).click(random_btn_go_to_purchase).perform()

    def choice_payment_option(self):
        """Выбрать в блоке вариант оплаты"""
        self.browser.find_element(*ShopPageLocators.BLOCK_SELECT).click()
        select_payment_list = self.browser.find_elements(*ShopPageLocators.PAYMENT_OPTIONS)
        search_value_in_elements(select_payment_list, ValidDataConfig.TEXT_PAYMENT_TERMS).click()

        name_phone_h1 = self.browser.find_element(*ShopPageLocators.PHONE_PAGE_HEADER).text
        name_payment_list = self.browser.find_element(*ShopPageLocators.NAME_SELECTED_PAYMENT).text
        print(f"\n Например: «Выбран {name_phone_h1}, вариант оплаты: {name_payment_list}»")

    def click_login_and_buy(self):
        """Нажать кнопку 'Войти и купить'"""
        button_login_and_buy = self.browser.find_elements(*ShopPageLocators.BTN_LOGIN_TO_BUY)
        search_value_in_elements(button_login_and_buy, ValidDataConfig.TEXT_BTN_LOGIN_AND_BUY).click()
