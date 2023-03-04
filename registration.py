from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://awesomeqa.com/ui/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/a"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a"))).click()
driver.find_element(By.ID, "input-firstname").send_keys("Jhony")
driver.find_element(By.ID, "input-lastname").send_keys("Deep")
driver.find_element(By.ID, "input-email").send_keys("jhonydeep" + str(random.randint(1, 999)) + "@gmail.com")
driver.find_element(By.ID, "input-telephone").send_keys("73889765656")
driver.find_element(By.ID, "input-password").send_keys("1234")
driver.find_element(By.ID, "input-confirm").send_keys("1234")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div/div/input[1]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div/div/input[2]").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/a"))).click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/aside/div/a[13]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/a").click()

time.sleep(3)
