import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://qatest.schoox.com/login")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/form/div[1]/input'))
)

username = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/div[1]/input')
username.send_keys("admin@schoox.com")

password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/input')
password.send_keys("123456" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Training"))
)

link = driver.find_element(By.LINK_TEXT, "Training")
link.click()

course_title = driver.find_element(By.LINK_TEXT, "Μάθημα για automation")
course_title.click()

Enroll = driver.find_element(By.XPATH, '//*[@id="top_course"]/div[2]/div')
Enroll.click()

Python_Complete = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div/div[2]/div[1]/div[2]/div/b')
Python_Complete.click()

driver.switch_to.alert.accept()

Ruby_Complete = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[2]/div')
Ruby_Complete.click()

driver.switch_to.alert.accept()

Java_Complete = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div/div[2]/div[3]/div[2]/div/b')
Java_Complete.click()

driver.switch_to.alert.accept()

Selenium_Complete = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div/div[2]/div[4]/div[2]/div')
Selenium_Complete.click()

driver.switch_to.alert.accept()

progress_element = driver.find_element(By.XPATH, '//*[@id="top_course"]/div[2]/div')
progress_text = progress_element.text

try:
    assert progress_text == 'Course Progress: 100.00%', f"Expected 100.00% but found: {progress_text}"
    print("Progress is 100% as expected!")
except AssertionError as e:
    print(f"Assertion error: {e}")

time.sleep(4)

driver.quit()