from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from enums.railway_tab import RailwayTab
from utils.config_loader import ConfigLoader
from utils.driver_manager import DriverManager


class BasePage:
    def __init__(self):
        self.current_tab_index = 0
        self.driver_manager = DriverManager()
        self.config_loader = ConfigLoader()
        self.tab_locator = "//a[.='%s']"
        self.hyperlink_locator = "//a[contains(text(),'%s')]"
        self.title_locator = (By.XPATH, "//h1[@align='center']")

    def navigate_to_url(self, url):
        get_url = ConfigLoader().get_property('DEFAULT', url)
        self.driver_manager.getDriver().get(get_url)

    def switch_to_previous_tab(self):
        if self.current_tab_index > 0:
            previous_tab_index = self.current_tab_index - 1
            self.driver_manager.getDriver().switch_to.window(
                self.driver_manager.getDriver().window_handles[previous_tab_index])
            self.current_tab_index = previous_tab_index
            return True
        return False

    def switch_to_next_tab(self):
        if self.current_tab_index < len(self.driver_manager.getDriver().window_handles) - 1:
            next_tab_index = self.current_tab_index + 1
            self.driver_manager.getDriver().switch_to.window(
                self.driver_manager.getDriver().window_handles[next_tab_index])
            self.current_tab_index = next_tab_index
            return True
        return False

    def refresh_page(self):
        self.driver_manager.getDriver().refresh()

    def find(self, element):
        return self.driver_manager.getDriver().find_element(*element)

    def click(self, element):
        self.driver_manager.getDriver().find_element(*element).click()

    def enter(self, element, text):
        self.driver_manager.getDriver().find_element(*element).send_keys(text)

    def scroll(self, element):
        elements = self.driver_manager.getDriver().find_element(*element)
        self.driver_manager.getDriver().execute_script("arguments[0].scrollIntoView(true);", elements)

    def get_wait(self, time: int):
        return WebDriverWait(self.driver_manager.getDriver(), time)

    def wait_for_element_visibility(self, element):
        self.get_wait(20).until(EC.visibility_of_element_located(element))

    def wait_for_element_visibility_of(self, element):
        self.get_wait(20).until(EC.visibility_of(element))

    def wait_for_element_clickable(self, element):
        return self.get_wait(20).until(EC.element_to_be_clickable(element))

    def wait_for_element_invisibility(self, element):
        self.get_wait(20).until(EC.invisibility_of_element_located(element))

    def get_text(self, locator):
        element = self.driver_manager.getDriver().find_element(*locator)
        return element.text

    def is_displayed(self, element):
        try:
            self.driver_manager.getDriver().find_element(element)
            self.wait_for_element_visibility(element)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def select_by_value(self, element, value):
        web_element = self.find(element)
        self.wait_for_element_visibility_of(web_element)
        select = Select(web_element)
        select.select_by_value(value)

    def select_by_visible_text(self, element, text):
        web_element = self.find(element)
        self.wait_for_element_visibility_of(element)
        select = Select(web_element)
        select.select_by_visible_text(text)

    def clear_field(self, element):
        self.find(element).clear()

    def click_if_clickable(self, element):
        self.wait_for_element_visibility(element)
        return self.wait_for_element_clickable(element).click()

    def is_disappear(self, element):
        try:
            self.wait_for_element_invisibility(element)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def accept_alert(self):
        alert = self.driver_manager.getDriver().switch_to.alert
        alert.accept()

    def switch_to_new_tab(self):
        self.driver_manager.getDriver().switch_to.new_window('tab')

    def click_tab(self, tab_name: RailwayTab):
        locator_tab = (By.XPATH, self.tab_locator % tab_name.value)
        self.driver_manager.getDriver().find_element(*locator_tab).click()

    def is_title_display(self):
        title = self.get_text(self.title_locator)
        return title

    def click_hyperlink_by_name(self, name_hyperlink):
        link_locator = (By.XPATH, self.hyperlink_locator % name_hyperlink.value)
        self.driver_manager.getDriver().find_element(*link_locator).click()

    def is_tab_displayed(self, tab_name) -> bool:
        try:
            element = (By.LINK_TEXT, tab_name.value)
            return self.find(element).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def does_tab_exist(self, tab_name) -> bool:
        try:
            element = (By.LINK_TEXT, tab_name.value)
            self.get_wait(20)
            exist = self.is_disappear(element)
            return exist
        except (NoSuchElementException, TimeoutException):
            return False
