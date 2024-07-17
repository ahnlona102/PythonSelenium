import unittest
from utils.driver_manager import DriverManager
class BaseTest(unittest.TestCase):
    driver_manager = None

    @classmethod
    def setUpClass(self):
        self.driver_manager = DriverManager()
        self.driver_manager.init_local_webdiver("chrome")
        self.driver = self.driver_manager.getDriver()

    @classmethod
    def tearDownClass(self):
        self.driver_manager.quitDriver()

    def test_example(self):
        self.driver.get("https://www.selenium.dev/documentation/")
        self.assertIn("The Selenium Browser Automation Project", self.driver.title)

if __name__ == "__main__":
    unittest.main()
