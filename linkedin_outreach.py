# import webdriver
from http.server import executable
# from tkinter import Y
# from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
# from selenium.webdriver.support.ui import WebDriverWait
import time

from contactsheet import addtospreadsheet
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

print("initialising webdriver")
# create webdriver object
# driver = webdriver.Chrome('/Users/rahulmathur/.wdm/drivers/chromedriver/mac64_m1/100.0.4896.60/chromedriver 2')

driver.get("https://www.linkedin.com/")


# id = "xxx@gmail.com"                  #edit login credentials before running script to login into your linkedin account
# pw = "xxxxxx"


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
  'https://www.linkedin.com/in/siddhant-patni/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BmVJ%2BC08zQwi1JuQ9mXKoMA%3D%3D',
  'https://www.linkedin.com/in/sarita-aggarwal-b068a31b8/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BmVJ%2BC08zQwi1JuQ9mXKoMA%3D%3D',
  'https://www.linkedin.com/in/shreya-shrivastava-2607/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BmVJ%2BC08zQwi1JuQ9mXKoMA%3D%3D',
  'https://www.linkedin.com/in/kedar-kanekar-360709154/',
  'https://www.linkedin.com/in/aakritinath/',
  'https://www.linkedin.com/in/vigneshwaran-anandaraj-788881117/',
  'https://www.linkedin.com/in/karthik-daroor-9193a6a/',
  'https://www.linkedin.com/in/madhulika-tyagi-17821426/',
  'https://www.linkedin.com/in/gaurav-tiwari-49ab03135/',
  'https://www.linkedin.com/in/waseemibnyousefcm/',
  'https://www.linkedin.com/in/kirti-mendirata-aab44a143/',
  'https://www.linkedin.com/in/dr-mayank-patel-847741157/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BMVLrdTVETGGqoJox3UCLrA%3D%3D',
  'https://www.linkedin.com/in/shrutty-she-her-395b12157/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BMVLrdTVETGGqoJox3UCLrA%3D%3D',
  'https://www.linkedin.com/in/pravina-jadhav-29374412a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3Byg36vB6JTbalecorFdym8g%3D%3D',
  'https://www.linkedin.com/in/anshuman-neralla-23892b20/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3Byg36vB6JTbalecorFdym8g%3D%3D',
  'https://www.linkedin.com/in/nandhinianand/',
  'https://www.linkedin.com/in/anisha-kashwani-61005116/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BEhFzy1jhTlStUOrJ%2F%2FGXLA%3D%3D',
  'https://www.linkedin.com/in/kajal-jain04/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BEhFzy1jhTlStUOrJ%2F%2FGXLA%3D%3D',
  'https://www.linkedin.com/in/editor-harshyadav/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BEhFzy1jhTlStUOrJ%2F%2FGXLA%3D%3D',
  'https://www.linkedin.com/in/deepi-dhiman-705802190/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BEhFzy1jhTlStUOrJ%2F%2FGXLA%3D%3D',
  'https://www.linkedin.com/in/twisha-ahuja-a5a80243/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BEhFzy1jhTlStUOrJ%2F%2FGXLA%3D%3D',
  'https://www.linkedin.com/in/humaida-khan/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BEhFzy1jhTlStUOrJ%2F%2FGXLA%3D%3D',
]
print("fetching profiles")

for i in profiles:                  #this for loop iterates over all the profiles and sends them messages
    driver.get(i)
    print("Opened profile")
    openmsgfield = "Message"
    time.sleep(3)
    msgelem = driver.find_element(by=By.LINK_TEXT, value=openmsgfield)
    msgelem.send_keys(Keys.ENTER)
    time.sleep(2)
    chatexpand = '//button[@data-control-name = "overlay.expand_conversation_window"]'
    chatexpandbtn = driver.find_element(by=By.XPATH, value=chatexpand)
    chatexpandbtn.click()
    time.sleep(1)
    msgelement = "div.msg-form__contenteditable > p"
    inputmsg = driver.find_element(by=By.CSS_SELECTOR, value=msgelement)
    time.sleep(1)
    nameelem = "h1.text-heading-xlarge"
    fullname = driver.find_element(by=By.CSS_SELECTOR, value=nameelem).text
    firstname = fullname.partition(" ")[0]
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

    # savetodb = ['LinkedIn', 'RM', fullname, 'Y' ]

    addtospreadsheet('LinkedIn', 'RM', fullname, 'Y')
    print("added to spreadsheet")
print("shutting down")
driver.close()              #shuts down browser
