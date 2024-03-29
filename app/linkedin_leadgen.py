# import webdriver
from distutils.command.clean import clean
from distutils.log import info
from http.server import executable
from os import link
# from turtle import title
from unicodedata import name
# from tkinter import Y
# from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# import html5lib
import requests
import time
from userinfo import *
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

print("initialising webdriver")
# create webdriver object
# driver = webdriver.Chrome('/Users/rahulmathur/.wdm/drivers/chromedriver/mac64_m1/100.0.4896.60/chromedriver 2', chrome_options=chrome_options)

driver.get("https://www.linkedin.com/")


# id = "xxx@gmail.com"                  #edit login credentials before running script to login into your linkedin account
# pw = "xxxxxx"

# edit login credentials before running script to login into your linkedin account
id = "mathur.rahul.2501@gmail.com"
pw = "youcanthackme"

print("logging into linkedin")
# selects login field and enters credentials
sessionkey = "session_key"
login = driver.find_element(by=By.NAME, value=sessionkey)
login.send_keys(id)

# select pw field and enter pw
password = "session_password"
enterpw = driver.find_element(by=By.NAME, value=password)
enterpw.send_keys(pw + Keys.ENTER)

verificationtxt = '//h1[contains(text(), "Let\'s do a quick verification")]'
verficationelem = driver.find_element(by=By.XPATH, value=verificationtxt)
print(verficationelem.is_displayed())

if str(verficationelem.is_displayed()) == "True":
    print("verification required")
    pin = input("Enter your PIN")
    pininputloc = 'input.form__input--text'
    inputelem = driver.find_element(by=By.CSS_SELECTOR, value=pininputloc)
    inputelem.send_keys(pin + Keys.ENTER)
print("logged into LinkedIn")

driver.get("https://www.linkedin.com/in/rahul-mathur-74161284/")
time.sleep(2)
# firstpostreactions = '//button[contains(@aria-label, "reactions")]'
activityparentdiv = '//span[contains(text(), "Activity")]//ancestor::section//a[contains(@href, "https://www.linkedin.com/feed/update/")]'
posts = driver.find_elements(by=By.XPATH, value=activityparentdiv)
dirtyhrefs = []
# print(posts)
for i in posts:
    dirtyhrefs.append(i.get_attribute("href"))
# print(dirtyhrefs)
cleanlist = []
for i in dirtyhrefs:
    if i not in cleanlist:
        cleanlist.append(i)
print("The clean list is" + str(cleanlist))
names = []
links = []
degrees = []
captions = []

for i in cleanlist:
    driver.get(i)
    time.sleep(2)
    socialcountsselector = 'li.social-details-social-counts__item.social-details-social-counts__reactions.social-details-social-counts__reactions--with-social-proof > button'
    socialcntbtn = driver.find_element(
        by=By.CSS_SELECTOR, value=socialcountsselector)
    time.sleep(2)
    socialcntbtn.click()
    listlength = 'ul'
    listlengthvar = driver.find_element(by=By.CSS_SELECTOR, value=listlength)
    # names = []
    # links = []
    # degrees = []
    # captions = []
    old_height = listlengthvar.rect["height"]
    old_height_str = str(listlengthvar.rect["height"])
    # print("Old height is", old_height)
    time.sleep(5)
    driver.execute_script(
        "document.querySelector('#artdeco-modal-outlet > div > div > div.artdeco-modal__content').scrollTop="+old_height_str)
    time.sleep(3)
    new_height = listlengthvar.rect["height"]
    new_height_str = str(listlengthvar.rect["height"])
    # print("new height is", new_height)
    time.sleep(2)
    nameloc = 'div.artdeco-entity-lockup__content > div.artdeco-entity-lockup__title > span'
    linkloc = 'li.artdeco-list__item > a'
    degreeloc = 'div.artdeco-entity-lockup__content > div.artdeco-entity-lockup__badge > span'
    captionloc = 'div.artdeco-entity-lockup__caption'
    while (new_height > old_height):
        print("old height is", old_height)
        print("new height is", new_height)
        time.sleep(4)
        old_height = new_height
        old_height_str = str(old_height)
        print("old height has now become", old_height)
        driver.execute_script(
            "document.querySelector('#artdeco-modal-outlet > div > div > div.artdeco-modal__content').scrollTop="+old_height_str)
        time.sleep(2)
        print("getting list of names")
        new_height = listlengthvar.rect["height"]
        print("new height is now", new_height)
        time.sleep(2)
    time.sleep(3)
    namelist = driver.find_elements(by=By.CSS_SELECTOR, value=nameloc)
    linklist = driver.find_elements(by=By.CSS_SELECTOR, value=linkloc)
    degreelist = driver.find_elements(by=By.CSS_SELECTOR, value=degreeloc)
    captionlist = driver.find_elements(by=By.CSS_SELECTOR, value=captionloc)
    # print(namelist)
    for i in namelist:
        if "View" not in i.text:
            names.append(i.text)
    print(names)
    print("Count of names is", len(names))
    for i in linklist:
        links.append(i.get_attribute("href"))
    print(links)
    print("Count of links is", len(links))
    for i in degreelist:
        if "·" not in i.text:
            degrees.append(i.text)
    print(degrees)
    print("Count of degrees is ", len(degrees))
    for i in captionlist:
        captions.append(i.text)
    print(captions)
    print("Count of captions is", len(captions))
    print("going to next post")

userInfoDict = {k: Userinfo(a, b, c) for (
    k, a, b, c) in zip(names, links, degrees, captions)}
