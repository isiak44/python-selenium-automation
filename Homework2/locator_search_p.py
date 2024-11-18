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

#Open the URL
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

#Creating locators and search strategy for amazon login page

driver.find_element(By.XPATH, "//i[@role='img']") #Element for amazon logo
driver.find_element(By.ID, 'ap_email') #Elemend for email field
driver.find_element(By.ID, 'continue') #Continue button
driver.find_element(By.XPATH, "//*[contains(@href, 'condition_of_use')]") #Condition of use button
driver.find_element(By.XPATH, "//*[contains(@href, 'notification_p')]") #Privacy Notice
driver.find_element(By.XPATH, "//*[@class='a-expander-prompt']") #Need help link
driver.find_element(By.XPATH, "//a[contains(@href, 'forgotpassword')]") #Forgot password link
driver.find_element(By.ID, 'ap-other-signin-issues-link')#Other signin issues link
driver.find_element(By.ID, 'createAccountSubmit') #Create account link


sleep(3)

