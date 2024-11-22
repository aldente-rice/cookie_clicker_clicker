from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie_id = "bigCookie"

WebDriverWait(driver, 5).until(
    # waits for the language select to pop-up, then clicks on English language
    EC.presence_of_element_located((By.CSS_SELECTOR, '#langSelect-EN'))
)

language = driver.find_element(By.CSS_SELECTOR, '#langSelect-EN')
language.click()

WebDriverWait(driver, 5).until(
    # wait until the cookie element appears
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")

time.sleep(1)  # wait for it to load to start clicking
get_cookie_score = driver.find_element(By.ID, "cookies").text.split()
cookie_score = int(get_cookie_score[0])
while cookie_score < 10000:
    cookie.click()
    cookie_score += 1


time.sleep(10)
driver.quit()
