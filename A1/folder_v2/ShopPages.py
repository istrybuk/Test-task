from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from BaseApp import BasePage
import locators as loc
import random
import time


def search_value_in_elements(lst=None, param=None):
    if not lst or not param:
        print("\n В функцию search_value_in_elements() не передаются параметры поиска")
        return None
    for string in lst:
        if param in string.text:
            return string
    print(f"\n Искомый элемент: \"{param}\" функцией search_value_in_elements() не найден.")
    return None


class ShopPage(BasePage):

    def click_btn_close_cookie(self):
        """Закрыть окно с сообщением о cookie"""
        self.browser.find_element(*loc.ShopPageLocators.BTN_CLOSE_COOKIE).click()

    def selection_random_phone(self):
        """Выбрать случайный телефон"""
        btn_go_to_purchase = self.browser.find_elements(*loc.ShopPageLocators.BTN_GO_PURCHASE)
        random_btn_go_to_purchase = random.choice(btn_go_to_purchase[:])
        return random_btn_go_to_purchase

    def click_btn_go_purchase(self):
        """Нажать кнопку 'Перейти к покупке'"""
        action = ActionChains(self.browser)
        random_btn_go_to_purchase = self.selection_random_phone()
        action.move_to_element(random_btn_go_to_purchase).click(random_btn_go_to_purchase).perform()

    def initialization_block_payment(self):
        """Отображение блока"""
        start_time = time.time()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(loc.ShopPageLocators.BLOCK_SELECT_INFO))
        end_time = time.time()
        # Вычисление времени
        duration = end_time - start_time
        print(f"\n Время от клика до появления формы: {duration} секунд")

    def terms_choice_of_payment(self):
        """Выбор оплаты по условию"""
        self.browser.find_element(*loc.ShopPageLocators.BLOCK_SELECT_INFO).click()
        select_payment_list = self.browser.find_elements(*loc.ShopPageLocators.PAYMENT_OPTIONS)
        search_value_in_elements(select_payment_list, loc.ValidDataConfig.TEXT_PAYMENT_TERMS).click()

    def name_title(self):
        """Информация о телефоне и оплате"""
        name_phone_h1 = self.browser.find_element(*loc.ShopPageLocators.PHONE_PAGE_HEADER).text
        name_payment_list = self.browser.find_element(*loc.ShopPageLocators.NAME_SELECTED_PAYMENT).text
        print(f"\n Например: «Выбран {name_phone_h1}, вариант оплаты: {name_payment_list}»")

    def click_login_and_buy(self):
        """Нажать кнопку 'Войти и купить'"""
        button_login_and_buy = self.browser.find_elements(*loc.ShopPageLocators.BTN_LOGIN_TO_BUY)
        search_value_in_elements(button_login_and_buy, loc.ValidDataConfig.TEXT_BTN_LOGIN_AND_BUY).click()
