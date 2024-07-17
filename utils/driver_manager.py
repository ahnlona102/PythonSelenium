import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


class DriverManager:
    driver = threading.local()
    wait = threading.local()
    Hub_URL = "http://localhost:4444"

    def init_remote_webdiver(self, browser):
        if browser.lower() == "chrome":
            chromeOptions = ChromeOptions()
            chromeOptions.set_capability("browserName", "chrome")
            chromeOptions.add_argument("--verbose")
            self.driver.instance = webdriver.Remote(command_executor=self.Hub_URL, options=chromeOptions)
        elif browser.lower() == "firefox":
            firefoxOptions = FirefoxOptions()
            firefoxOptions.set_capability("browserName", "firefox")
            firefoxOptions.add_argument("--verbose")
            self.driver.instance = webdriver.Remote(command_executor=self.Hub_URL, options=firefoxOptions)
        elif browser.lower() == "edge":
            edgeOptions = EdgeOptions()
            edgeOptions.set_capability("browserName", "edge")
            edgeOptions.add_argument("--verbose")
            self.driver.instance = webdriver.Remote(command_executor=self.Hub_URL, options=edgeOptions)

        self.wait.instance = WebDriverWait(self.driver.instance, 30)

    def init_local_webdiver(self, browser):
        if browser.lower() == "chrome":
            self.driver.instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser.lower() == "firefox":
            self.driver.instance = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
        elif browser.lower() == "edge":
            self.driver.instance = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager.install()))
        self.wait.instance = WebDriverWait(self.driver.instance, 30)

    def getDriver(self):
        return self.driver.instance

    def getWait(self):
        return self.wait.instance

    def quitDriver(self):
        driver_instance = self.driver.instance
        if driver_instance:
            driver_instance.quit()
            self.driver.instance = None
            self.wait.instance = None

