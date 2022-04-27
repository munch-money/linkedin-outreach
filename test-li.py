# import webdriver
from http.server import executable
# from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
import time
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

print("initialising webdriver")
# create webdriver object
# driver = webdriver.Chrome('/Users/rahulmathur/.wdm/drivers/chromedriver/mac64_m1/100.0.4896.60/chromedriver 2')

driver.get("https://www.linkedin.com/")


id = "xxx@gmail.com"                  #edit login credentials before running script to login into your linkedin account
pw = "xxxxxx"



print("logging into linkedin")
# selects login field and enters credentials
sessionkey = "session_key"
login = driver.find_element(by=By.NAME, value=sessionkey)
login.send_keys(id)

#select pw field and enter pw
password = "session_password"
enterpw = driver.find_element(by=By.NAME, value=password)
enterpw.send_keys(pw + Keys.ENTER)

print("logged into LinkedIn")

profiles = [                                                #paste url of linkedin profiles you'd like to send messages to in this array
    "https://www.linkedin.com/in/hamir-shekhawat-9a45b311a/",
    # "https://www.linkedin.com/in/agneesh-bhadury/",
    # "https://www.linkedin.com/in/nshlmd/",
    # "https://www.linkedin.com/in/harshit-tahiliani/",
]
print("fetching profiles")

for i in profiles:                  #this for loop iterates over all the profiles and sends them messages
    driver.get(i)
    print("Opened profile")
    openmsgfield = "Message"
    time.sleep(1)
    msgelem = driver.find_element(by=By.LINK_TEXT, value=openmsgfield)
    msgelem.send_keys(Keys.ENTER)

    time.sleep(1)
    msgelement = "div.msg-form__contenteditable > p"
    inputmsg = driver.find_element(by=By.CSS_SELECTOR, value=msgelement)

    time.sleep(1)
    nameelem = "h1.text-heading-xlarge"
    getname = driver.find_element(by=By.CSS_SELECTOR, value=nameelem).text
    firstname = getname.partition(" ")[0]
    print("messaging" + " " + firstname)
    outreach_message = "Thanks for connecting with me. I was impressed with your profile as a freelance professional and thought I’d reach out to introduce myself.\n\nI'm the founder at Munch, we’re building a business management platform for solopreneurs/entrepreneurs working independently or in small teams. We assist in non-core tasks such as invoicing, contracts and taxes to make entrepreneurship easier.\n\nI'd really appreciate it if you could try Munch to create your next invoice. I think you might find it useful :)\n\nIf you don’t, I’d be happy to chat further to learn about your challenges and how I could be helpful to you. Hope you’re doing good!\n\nBest,\nRahul\nhttps://munch.money"
    inputmsg.send_keys("Hi" + " " + firstname + "," + "\n\n" + outreach_message)
    print("inserting msg into chatbox")
    time.sleep(3)
    buttonelem = "button.msg-form__send-button"
    button = driver.find_element(by=By.CSS_SELECTOR, value=buttonelem)
    button.click()
    print("message sent successfully to" + " "+ firstname)

    time.sleep(2)
    exit = "button[data-control-name='overlay.close_conversation_window']"
    exitbutton = driver.find_element(by=By.CSS_SELECTOR, value=exit)
    exitbutton.click()
    print("shut chat with" + " " + firstname)

