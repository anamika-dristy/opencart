from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
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
#Search product:
driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").click()
driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").send_keys("iphone")
driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/span").click()
#Select product:
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div").click()
#Add to cart:
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div/button"))).click()
#Shopping Cart:
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span"))).click()
#CheckOut:
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div[2]/a"))).click()

#Billing address:
driver.find_element(By.ID, "input-payment-firstname").send_keys("Jhony")
driver.find_element(By.ID, "input-payment-lastname").send_keys("Deep")
driver.find_element(By.ID, "input-payment-address-1").send_keys("House-133, Dhaka-1230")
driver.find_element(By.ID, "input-payment-city").send_keys("Dhaka")
driver.find_element(By.ID, "input-payment-postcode").send_keys("1230")
#driver.find_element(By.ID, "input-confirm").send_keys("1234")
time.sleep(2)
#Select Country:
Select(driver.find_element(By.ID, "input-payment-country")).select_by_value("18")
Select(driver.find_element(By.ID, "input-payment-zone")).select_by_value("322")
driver.find_element(By.ID, "button-payment-address").click()
time.sleep(5)

#Confirm Order
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "button-payment-address"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "button-shipping-address"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "button-shipping-method"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[5]/div[2]/div/div[2]/div/input[1]"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "button-payment-method"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "button-confirm"))).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/a"))).click()

time.sleep(5)
