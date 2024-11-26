from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

sleep(1)
driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name").send_keys('Ray')
driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys('Ray@gmail.com')
driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys('abcd12345')
driver.find_element(By.CSS_SELECTOR, "#ap_password_context_message_section")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys('abcd12345')
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy']")
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

sleep(2)