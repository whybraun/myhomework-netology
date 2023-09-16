from unittest import TestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestYandexAuth(TestCase):

    def setUp(self):
        chrome_driver_path = ChromeDriverManager().install()
        browser_service = Service(executable_path=chrome_driver_path)
        self.browser = Chrome(service=browser_service)
        self.browser.get('https://passport.yandex.ru/auth/')

    def tearDown(self):
        self.browser.quit()

    def test_successful_auth(self):
        login = 'your_email@example.com'
        password = 'your_password'

        email_input = self.browser.find_element(By.NAME, 'login')
        email_input.send_keys(login)

        button_element = self.browser.find_element(By.CSS_SELECTOR, '.Button2.Button2_size_xxl.Button2_view_action.Button2_type_submit')
        button_element.click()

        WebDriverWait(self.browser, 10).until(EC.url_contains('https://passport.yandex.ru/auth/multiotp'))

        password_input = self.browser.find_element(By.NAME, 'passwd')
        password_input.send_keys(password)

        button_element = self.browser.find_element(By.CSS_SELECTOR, '.Button2.Button2_size_xxl.Button2_view_action.Button2_type_submit')
        button_element.click()

        WebDriverWait(self.browser, 10).until(EC.url_contains('https://passport.yandex.ru/auth/2fa'))
