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

#open target url
driver.get('https://www.target.com/')

#find search box and input 'Tree'
search = driver.find_element(By.ID, 'search')
search.clear()
search.send_keys('Tree')

driver.find_element(By.XPATH, "//button[@aria-label='search']").click()
sleep(2)

ex_result = 'Tree'
act_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

assert ex_result in act_result, f'Expected text {ex_result} not in {act_result}'
print('Test passed')

quit()