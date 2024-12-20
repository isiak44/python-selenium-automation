from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def clear(self, *locator):
        self.driver.find_element(*locator).clear()

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

    def verify_partial_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected Partial Url {expected_url} not found in current url {actual_url}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected Url {expected_url} does not match current url {actual_url}'

    def wait_until_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message= f'Element by {locator} not visible'
        )

    def wait_until_visible_and_click(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message= f'Element by {locator} not visible'
        ).click()

    def wait_until_not_visible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element(locator),
            message= f'Element by {locator} should not be visible'
        )

    def wait_until_clickable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message= f'Element by {locator} not clickable'
        )

    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message= f'Element by {locator} not clickable'
        ).click()



