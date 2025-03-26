from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()

    def is_inventory_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.INVENTORY_CONTAINER)).is_displayed()
