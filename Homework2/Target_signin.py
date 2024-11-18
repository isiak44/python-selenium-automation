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

#Open Target Url
driver.get('https://www.target.com/')

#click on sign button to open navigation
driver.find_element(By.ID, 'account-sign-in').click()
sleep(.5)
driver.find_element(By.XPATH, "//*[@data-test= 'accountNav-signIn']").click()
sleep(2)
#Verify sign in page
target_h1 = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign into')]").text
signin_button = driver.find_element(By.XPATH, "//button[@type= 'submit' or @id='login']")

if target_h1:
    print('Test Case Passed')
if signin_button:
    print('Sign in button exist')

quit()