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

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="course_catalogue"]/div[2]/div[2]'))
)

QA_Categories = driver.find_element(By.XPATH, '//*[@id="course_catalogue"]/div[2]/div[2]')
QA_Categories.click()

elements_with_class = driver.find_elements(By.CSS_SELECTOR, 'tr.course_item a.course_title')

element_texts = []

for element in elements_with_class:
    element_text = element.text.strip()
    element_texts.append(element_text)

print(element_texts)

time.sleep(4)

driver.quit()