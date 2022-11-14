# from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import LiveServerTestCase
from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path=r"C:\Users\aiden\chromedriver_win32")


class TitleTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.assertIn("Travel Wishlist", self.selenium.title)
