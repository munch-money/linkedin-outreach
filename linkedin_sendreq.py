# import webdriver
from http.server import executable
# from typing import KeysView
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
# from selenium.webdriver.support.ui import WebDriverWait
import time
# import html5lib
# import requests
from contactsheet import addtospreadsheet
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException
from contactsheet import addtospreadsheet


# opts = ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("window-size=1200x600")
# driver = Chrome(chrome_options=opts)


op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

print("initialising webdriver")
# create webdriver object


# chrome_options = Options().chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(options=opts, service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome('/Users/rahulmathur/.wdm/drivers/chromedriver/mac64_m1/100.0.4896.60/chromedriver 2')
# driver.set_window_size(1600,1600)
driver.get("https://www.linkedin.com/")


# id = "xxx@gmail.com"                  #edit login credentials before running script to login into your linkedin account
# pw = "xxxxxx"

# edit login credentials before running script to login into your linkedin account


print("logging into linkedin")
# selects login field and enters credentials
sessionkey = "session_key"
login = driver.find_element(by=By.NAME, value=sessionkey)
login.send_keys(id)

# select pw field and enter pw
password = "session_password"
enterpw = driver.find_element(by=By.NAME, value=password)
enterpw.send_keys(pw + Keys.ENTER)

print("logged into LinkedIn")

profiles = [
    "https://www.linkedin.com/in/ACwAACkw1DYB4TAnpJIbp1TrsUt7qS3FIB7R-X8/",
]
print('fetching profiles')

for i in profiles:
    print("opening profile")
    driver.get(i)
    print("sending request")
    time.sleep(2)
    nameelem = "h1.text-heading-xlarge"
    fullname = driver.find_element(by=By.CSS_SELECTOR, value=nameelem).text
    firstname = fullname.partition(" ")[0]
    dispchecklink = '//span[text() = "Connect"]/ancestor::div[@role="button"]'
    try:
        dispcheck = driver.find_element(by=By.XPATH, value=dispchecklink)
        driver.execute_script("arguments[0].click();", dispcheck)
        sendreqbtnloc = '//button[@aria-label = "Send now"]'
        sendreqbtn = driver.find_element(by=By.XPATH, value=sendreqbtnloc)
        sendreqbtn.click()
    except NoSuchElementException as Exception:
        print("Follow button does not show")
        try:
            connectpath = '//span[text() = "Connect"]/parent::div'
            connectbtn = driver.find_element(by=By.XPATH, value=connectpath)
            driver.execute_script("arguments[0].click();", connectbtn)
            try:
                sendreqbtnloc = '//button[@aria-label = "Send now"]'
                sendreqbtn = driver.find_element(by=By.XPATH, value=sendreqbtnloc)
                sendreqbtn.click()
            except NoSuchElementException as Exception:
                howyouknowbtnloc = '//button[contains(@aria-label, "We don\'t know each other")]'
                howyouknowbtn = driver.find_element(by=By.XPATH, value=howyouknowbtnloc)
                howyouknowbtn.click()
                connectbtnloc = '//button[contains(@aria-label, "Connect")]'
                connectbtn = driver.find_element(by=By.XPATH, value=connectbtnloc)
                connectbtn.click()
                time.sleep(3)
                connectbtnloc = '//button[contains(@aria-label, "Connect")]'
                connectbtn = driver.find_element(by=By.XPATH, value=connectbtnloc)
                driver.execute_script("arguments[0].click();", connectbtn)
        except NoSuchElementException as Exception:
            connectbtnloc = 'div.pvs-profile-actions > button'
            connectbtn = driver.find_element(by=By.CSS_SELECTOR, value=connectbtnloc)
            driver.execute_script("arguments[0].click();", connectbtn)
        sendreqbtnloc = '//button[@aria-label = "Send now"]'
        sendreqbtn = driver.find_element(by=By.XPATH, value=sendreqbtnloc)
        sendreqbtn.click()
    addtospreadsheet('LinkedIn', 'RM', fullname, 'sent request')
    # btnpath = '//div[@class = "pvs-profile-actions "]//*[@aria-label = "More actions"]'
    # msgelem = driver.find_element(by=By.XPATH, value=btnpath)
    # # msgelem = driver.locate_with(By.TAG_NAME, "button").above(By.TAG_NAME, "span")
    # print(msgelem.get_attribute("outerHTML"))
    # time.sleep(5)
    # msgelem.click()
    # time.sleep(5)
    # connectbuttonloc = '//span[text() = "Connect"]/ancestor::div[@role="button"]'
    # # connectbuttonloc = '//div[@class= "artdeco-dropdown__content-inner"]//*[@role = "button" and @class = "display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]'
    # # connectbuttonloc = driver.find_elements(locate_with(By.TAG_NAME, "div").above({By.LINK_TEXT, "Connect"}))
    # connectbuttonclck = driver.find_element(by=By.XPATH, value=connectbuttonloc)
    # time.sleep(2)
    # print(connectbuttonclck.get_attribute("outerHTML"))
    # print(connectbuttonclck.get_dom_attribute("role"))
    # print(str(connectbuttonclck.is_displayed()))
    # # connectbuttonclck.send_keys(Keys.ENTER)
    # driver.execute_script("arguments[0].click();", connectbuttonclck)
    # sendreqbtnloc = '//button[@aria-label = "Send now"]'
    # sendreqbtn = driver.find_element(by=By.XPATH, value=sendreqbtnloc)
    # sendreqbtn.click()
