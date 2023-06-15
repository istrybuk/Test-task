from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random


def search_value_in_elements(lst=None, param=None):
    if lst is None:
        return print("Введите параметр и строку")
    else:
        for string in lst:
            if param in string.text:
                return string
        else:
            print(f"Искомый элемент: \"{param}\" функции search_value_in_elements, не найден.")


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

text_btn_purchase = "Перейти к покупке"
text_payment_selection_condition = "6 мес"
text_btn_login_and_buy = "Войти и купить"


driver.get("https://www.a1.by/ru/shop/c/phones")

block_phones = driver.find_elements("class name", "product-listing-item-link")
random_phones = random.choice(block_phones[:]).click()
# buttons_go_to_purchase = driver.find_elements("xpath", "//a[contains(@class, 'button--centered')]")
# random_btn_go_to_purchase = random.choice(buttons_go_to_purchase[:])
# click_random_btn_purchase = search_value_in_elements(random_btn_go_to_purchase).click()

driver.find_element("class name", "select2-selection__arrow").click()  # block_select =
select_payment_list = driver.find_elements("class name", "select2-results__option")
choice_payment = search_value_in_elements(select_payment_list, text_payment_selection_condition).click()
"""Нужно закрыть окно с cookies или не нажмет """
driver.find_element("xpath", '//button[@class="button button--primary cookie-panel-button"]').click()
button_login_and_buy = driver.find_elements("xpath", "//button[contains(@class, 'primary button--large')]")
search_value_in_elements(button_login_and_buy, text_btn_login_and_buy).click()
time.sleep(5)
