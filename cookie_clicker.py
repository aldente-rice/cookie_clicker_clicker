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

time.sleep(2)  # wait for cookie to load to start clicking
cookie = driver.find_element(By.ID, "bigCookie")

i = 0
while i < 100000:
    cookie.click()

    num_of_upgrades = 20
    for i in range(0, num_of_upgrades):  # looks through available upgrades, upgrades if enough cookies

        upgrade = driver.find_element(By.ID, f"product{i}")
        test_var_1 = driver.find_element(By.ID, f"productPrice{i}").text
        upgrade_price = int(driver.find_element(By.ID, f"productPrice{i}").text.replace(",", ""))

        try:
            match upgrade.get_attribute("class"):  # look to see if upgrade is available or not, using class name
                case "product locked disabled toggledOff" | "product locked disabled":
                    break  # skips the upgrades since they are locked or can't afford
                case "product unlocked enabled":
                    upgrade.click()
        except AttributeError:
            break

        i += 1

    # get_cookie_score = driver.find_element(By.ID, "cookies").text.split()
    # cookie_score = int(get_cookie_score[0])

    # cookie_score += 1
    # num_of_upgrades = 20
    # for i in range(0, num_of_upgrades):  # looks through available upgrades, upgrades if enough cookies
    #     upgrade = driver.find_element(By.ID, f"product{i}")
    #     test_var_1 = driver.find_element(By.ID, f"productPrice{i}").text
    #     print(test_var_1 + "1")
    #     upgrade_price = int(driver.find_element(By.ID, f"productPrice{i}").text)
    #
    #     match upgrade.__getattribute__("class"):  # look to see if upgrade is available or not, using class name
    #         case "product locked disabled toggledOff":
    #             break
    #         case "product locked disabled":
    #             continue
    #         case "product unlocked enabled":
    #             upgrade.click()
    #
    #     # get_cookie_score = driver.find_element(By.ID, "cookies").text.split()
    #     #
    #     # if upgrade_price <= cookie_score:
    #     #     upgrade.click()
    #     i += 1

    i += 1


time.sleep(5)
driver.quit()

