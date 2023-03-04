from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://awesomeqa.com/ui/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "input-email"))).send_keys("jhonydeep@gmail9900.com")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "input-password"))).send_keys("1234")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/input"))).click()
#Select Category:
driver.find_element(By.XPATH, "/html/body/div[1]/nav/div[2]/ul/li[7]/a").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div").click()
#Add Wish list:
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/button[2]"))).click()
#Check Wishlist:
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div[2]/ul/li[3]/a"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/table/tbody/tr/td[6]/button"))).click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/table/tbody/tr/td[6]/button").click()

time.sleep(5)
