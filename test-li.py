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


# create webdriver object
driver = webdriver.Chrome('/Users/rahulmathur/.wdm/drivers/chromedriver/mac64_m1/100.0.4896.60/chromedriver 2')

driver.get("https://www.linkedin.com/")

#enter login credentials before running script
# id = "xxx@xyz.com"
# pw = "qwerty"


# selects login field and enters credentials
sessionkey = "session_key"
login = driver.find_element(by=By.NAME, value=sessionkey)
login.send_keys(id)

#select pw field and enter pw
password = "session_password"
enterpw = driver.find_element(by=By.NAME, value=password)
enterpw.send_keys(pw + Keys.ENTER)

profiles = [
    "https://www.linkedin.com/in/hamir-shekhawat-9a45b311a/",
    "https://www.linkedin.com/in/agneesh-bhadury/",
    "https://www.linkedin.com/in/harshit-tahiliani/",
    "https://www.linkedin.com/in/nshlmd/",
]
for i in profiles:
#once logged in, go to profiles you would like to send messages to.
# driver.get("https://www.linkedin.com/in/hamir-shekhawat-9a45b311a/")
    driver.get(i)
    openmsgfield = "Message"
    time.sleep(1)
    msgelem = driver.find_element(by=By.LINK_TEXT, value=openmsgfield)
    msgopen = msgelem.send_keys(Keys.ENTER)

    time.sleep(1)
    msgelement = "div.msg-form__contenteditable > p"
    inputmsg = driver.find_element(by=By.CSS_SELECTOR, value=msgelement)

    time.sleep(1)
    nameelem = "h2.msg-overlay-bubble-header__title"

    getname = driver.find_element(by=By.CSS_SELECTOR, value=nameelem).text
    firstname = getname.partition(" ")[0]

    outreach_message = "Thanks for connecting with me. I was impressed with your profile as an independent entrepreneur and thought I’d reach out to introduce myself.\n\nI'm the founder at Munch, we’re building a business management platform for solopreneurs/entrepreneurs working independently or in small teams. We assist in non-core tasks such as invoicing, contracts and taxes to make entrepreneurship easier.\n\nI'd really appreciate it if you could try Munch to create your next invoice. I think you might find it useful :)\n\nIf you don’t, I’d be happy to chat further to learn about your challenges and how I could be helpful to you. Hope you’re doing good!\n\nBest,\nRahul\nhttps://munch.money"
    inputmsg.send_keys("Hi" + " " + firstname + "," + "\n" + outreach_message)

    time.sleep(3)
    buttonelem = "button.msg-form__send-button"
    button = driver.find_element(by=By.CSS_SELECTOR, value=buttonelem)
    button.click()

    time.sleep(2)
    exit = "button[data-control-name='overlay.close_conversation_window']"
    exitbutton = driver.find_element(by=By.CSS_SELECTOR, value=exit)
    exitbutton.click()

# WebDriverWait(msgopen, timeout=2).until(msgopen.find_element_by_class_name("msg-convo-wrapper msg-overlay-conversation-bubble msg-overlay-conversation-bubble--default-inactive ml4 msg-overlay-conversation-bubble--is-compose msg-overlay-conversation-bubble--petite"))
# refelem = driver.find_element({By.CLASS_NAME, "msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate"})
# mainhead = driver.find_element_by_class_name('flex-grow-1')

# msgselect = driver.find_element(locate_with(By.TAG_NAME, "p").below(refelem))
# inputmsg = mainhead.find_element_by_xpath(".//p")
# inputmsg.send_keys("hi")

# msg_locator = locate_with(By.TAG_NAME, "p").below({By.CLASS_NAME, ""})






# print(msgselect)
# msgsend = msgselect.send_keys("hi")


# inputmsg = "//p"





# msg_input = "//div[@aria-label='Write a message…'"
# msgsend = driver.find_element(by=By.XPATH, value=msg_input)

# <div class="msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate
#      " contenteditable="true" role="textbox" aria-multiline="true" aria-label="Write a message…"><p><br></p></div>


# <div class="msg-form__msg-content-container
    
#      msg-form__message-texteditor relative flex-grow-1 display-flex">
#   <div class="msg-form__msg-content-container--scrollable scrollable relative">
#     <div class="flex-grow-1">
#   <div class="msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate
#       " contenteditable="true" role="textbox" aria-multiline="true" aria-label="Write a message…"><p><br></p></div>

#     <div aria-hidden="true" class="msg-form__placeholder
#         t-14 t-black--light t-normal" data-placeholder="Write a message…">
#     </div>
# </div>

#       <div class="msg-form__expand-btn-wrapper">
#         <button aria-expanded="true" id="ember1424" class="msg-form__expand-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view" data-control-name="overlay.close_expand" type="button">  <li-icon aria-hidden="true" type="chevron-down-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M1 5l7 4.61L15 5v2.39L8 12 1 7.39z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Minimize compose field
# </span></button>
#       </div>

# <!---->
# <!---->
# <!---->  </div>
# </div>


# submitbtn = "homepage-basic_signin-form_submit-button"
# submit=driver.find_element(by=By.NAME, value=submitbtn).send_keys(Keys.ENTER)

# send keys
# element.send_keys("Arrays")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get('https://www.google.com')
# driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')



# from importlib.machinery import PathFinder
# # from pathlib import Path
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# # s=PathFinder('/Users/rahulmathur/Library/Python/3.8/bin/chromedriver-path')

# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


# # browser = webdriver.Chrome(ChromeDriverManager().install())
# url='https://www.google.com'
# driver.get(url)

## Chat box code that loads on clicking "message" on the profile
# <div id="ember267" tabindex="-1" class="msg-convo-wrapper msg-overlay-conversation-bubble msg-overlay-conversation-bubble--default-inactive ml4
#     msg-overlay-conversation-bubble--is-compose
    
    
#     msg-overlay-conversation-bubble--petite" role="dialog" aria-label="Messaging">
#   <div></div>

#     <header class="msg-overlay-bubble-header msg-overlay-conversation-bubble-header justify-space-between
#     " tabindex="-1">
#   <div class="msg-overlay-bubble-header__badge-container
#       "></div>

#   <div class="align-items-center display-flex">
#     <div class="align-items-center display-flex ">
      
#     <div class="flex-grow-1">
#       <h2 class="msg-overlay-bubble-header__title truncate t-14 t-bold
#           t-black
#           pr1" tabindex="-1">
#             New message
#                         </h2>
#     </div>
  
#     </div>
# </div>

# <!---->
#   <div class="msg-overlay-bubble-header__controls display-flex align-items-center">
# <!---->    <button aria-expanded="false" id="ember269" class="msg-overlay-bubble-header__control msg-overlay-conversation-bubble__expand-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view" data-control-name="overlay.expand_conversation_window">  <li-icon aria-hidden="true" type="arrows-out-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M8 6.59L6.59 8 3 4.41V7H1V1h6v2H4.41zM13 9v2.59L9.41 8 8 9.41 11.59 13H9v2h6V9z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Expand your conversation
# </span></button>

#   <button id="ember270" class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view" data-control-name="overlay.close_conversation_window">  <li-icon aria-hidden="true" type="cancel-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M14 3.41L9.41 8 14 12.59 12.59 14 8 9.41 3.41 14 2 12.59 6.59 8 2 3.41 3.41 2 8 6.59 12.59 2z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Close your draft conversation
# </span></button>
# </div>

# </header>

#   <div class="msg-overlay-conversation-bubble__content-wrapper relative display-flex flex-column
#       ">
        
#   <div class="msg-connections-typeahead__typeahead-delay-remove-container">
#     <div class="msg-connections-typeahead__typeahead-delay-remove-container ">
      
    
# <div class="msg-connections-typeahead relative
#      mbA">
#     <label for="ember288-search-field" class="visually-hidden">Enter message recipients</label>
#   <section class="msg-connections-typeahead__top-fixed-section">
#     <div class="scrollable msg-connections-typeahead__added-recipients display-flex align-items-center pl2 pv1">
#         <button aria-label="Remove Hamir Shekhawat" id="ember289" class="mv1 mr1 artdeco-pill artdeco-pill--slate artdeco-pill--3 artdeco-pill--dismiss artdeco-pill--selected ember-view" type="button"><span class="artdeco-pill__text">
#     Hamir Shekhawat
# </span>

# <li-icon aria-hidden="true" type="cancel-icon" class="artdeco-pill__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M14 3.41L9.41 8 14 12.59 12.59 14 8 9.41 3.41 14 2 12.59 6.59 8 2 3.41 3.41 2 8 6.59 12.59 2z"></path>
# </svg></li-icon>
# </button>

#       <input id="ember288-search-field" class="msg-connections-typeahead__search-field ml1 mv1" role="combobox" aria-autocomplete="list" aria-owns="ember288-suggestions-menu" autocomplete="off" aria-expanded="false" type="text">

#         <button id="ember290" class="msg-connections-typeahead__plus-icon mv2 ml2 artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--primary ember-view">  <li-icon aria-hidden="true" type="plus-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M14 9H9v5H7V9H2V7h5V2h2v5h5z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Show suggested recipients for your message
# </span></button>

#       <div class="msg-connections-typeahead__hidden-field"></div>
#     </div>
#   </section>
#   <div class="msg-connections-typeahead__opacity-transition-out
#       scrollable msg-connections-typeahead__search-results
      
#       msg-connections-typeahead__search-results--expanded">
#     <div class="msg-connections-typeahead__margin-transition-out">
# <!---->
# <!---->    </div>
#   </div>
  
# <!---->    
# </div>
  
#     </div>
# </div>

# <!---->
# <!---->
#   <div>
#   <div class="msg-thread-container msg-thread__thread-actions-tray">
# <!---->
# <!---->
# <!----></div>

# <!---->
#   <div class="msg-s-profile-card msg-s-profile-card-one-to-one pv4 ph3">
#   <div id="ember292" class="break-words artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view">
#       <a href="/in/hamir-shekhawat-9a45b311a/" id="ember293" class="active ember-view">
#         <div id="ember294" class="artdeco-entity-lockup__image artdeco-entity-lockup__image--type-circle ember-view" type="circle">
#           <div class="presence-entity presence-entity--size-4 msg-conversation-card__presence-entity">
#   <img src="https://media-exp1.licdn.com/dms/image/C4D03AQFnXMKIUNMcWg/profile-displayphoto-shrink_100_100/0/1647501594917?e=1656547200&amp;v=beta&amp;t=fglUCt5agK7OWTsqwoNlCbdmS18yEbOQ7xsJjZoRmoE" loading="lazy" alt="Hamir Shekhawat" id="ember295" class="presence-entity__image EntityPhoto-circle-4  lazy-image ember-view">

  
# <div class="presence-entity__indicator presence-entity__indicator--size-4
#        presence-indicator
#     presence-indicator--is-reachable
#     presence-indicator--size-4">
#   <span class="visually-hidden">
#       Status is reachable
#   </span>
# </div>
# </div>
        
# </div>
#       </a>
#     <div id="ember296" class="artdeco-entity-lockup__content ember-view">
#       <div id="ember297" class="artdeco-entity-lockup__title ember-view">
#           <a href="/in/hamir-shekhawat-9a45b311a/" id="ember298" class="active ember-view profile-card-one-to-one__profile-link">
#             Hamir Shekhawat
#           </a>
      
# </div>
        
# <!---->
#         <div id="ember300" class="artdeco-entity-lockup__badge ember-view">    <span class="a11y-text">1st degree connection</span>
#   <span class="artdeco-entity-lockup__degree" aria-hidden="true">
#     ·&nbsp;1st
#   </span>
# <!----><!----></div>
#       <div id="ember299" class="artdeco-entity-lockup__subtitle ember-view">
#         <div title="Co-founder at munch.money">
#           Co-founder at munch.money
#         </div>
#       </div>

# <!---->    </div>
  
# </div>
# </div>

# </div>

#   <div class="msg-compose-container__spacer mtA
#        msg-compose-container__spacer--compose-is-expanded"></div>

#       <form id="msg-form-ember271" class="msg-form--is-fully-expanded msg-form">
    
# <!---->
# <!---->
#           <div class="msg-form__attachment-drag-and-drop">
#   <div class="msg-form__attachment-drag-and-drop-content display-flex flex-column align-items-center justify-center">
#     <div class="msg-form__attachment-drag-and-drop-state-illustration"></div>
#     <div class="msg-form__attachment-drag-and-drop-text display-flex flex-column align-items-center justify-center">
#       <div class="msg-form__attachment-drag-and-drop-state-text t-16 t-bold">
#         Drag your file here.
#       </div>
#       <div class="msg-form__attachment-drag-and-drop-discoverability-text text-align-center">
#         <div class="t-16 t-bold">
#           Select your file
#         </div>
#         <div class="t-14">
#           Or drag &amp; drop next time
#         </div>
#       </div>
#     </div>
#   </div>
# </div>
# <!---->
# <!---->
# <!---->
#         <div class="msg-form__msg-content-container
    
#      msg-form__message-texteditor relative flex-grow-1 display-flex">
#   <div class="msg-form__msg-content-container--scrollable scrollable relative">
#     <div class="flex-grow-1">
#   <div class="msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate
#       " contenteditable="true" role="textbox" aria-multiline="true" aria-label="Write a message…"><p><br></p></div>

#   <div aria-hidden="true" class="msg-form__placeholder
#       t-14 t-black--light t-normal" data-placeholder="Write a message…">
#   </div>

# </div>

#       <div class="msg-form__expand-btn-wrapper">
#         <button aria-expanded="true" id="ember272" class="msg-form__expand-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view" data-control-name="overlay.close_expand" type="button">  <li-icon aria-hidden="true" type="chevron-down-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M1 5l7 4.61L15 5v2.39L8 12 1 7.39z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Minimize compose field
# </span></button>
#       </div>

# <!---->
# <!---->
# <!---->  </div>
# </div>
# <!---->        <footer aria-label="Compose actions for your conversation with " class="msg-form__footer flex-shrink-zero ">
#           <div class="msg-form__left-actions display-flex">
#               <div class="msg-form__upload-attachment inline-block">
#   <input name="persist" value="true" type="hidden">
#   <input name="upload_info" type="hidden">
#   <input id="attachment-input-ember273" class="msg-form__attachment-upload-input hidden" accept="image/*" data-control-name="overlay.image_select" type="file">
#   <button id="attachment-trigger-ember273" class="msg-form__footer-action artdeco-button artdeco-button--tertiary artdeco-button--circle artdeco-button--muted m0 artdeco-button--1" title="Attach an image to your conversation with " aria-label="Attach an image to your conversation with " type="button">
#     <span class="visually-hidden">
#       Attach an image to your conversation with 
#     </span>
#     <li-icon aria-hidden="true" type="image-icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" width="16" height="16" focusable="false">
#   <path d="M14 3H2a1 1 0 00-1 1v8a1 1 0 001 1h12a1 1 0 001-1V4a1 1 0 00-1-1zM3 11l3-2.95L9 11H3zm10 0h-2.77L6.31 7.13a.44.44 0 00-.62 0L3 9.77V5h10v6zm-2.5-2A1.5 1.5 0 109 7.5 1.5 1.5 0 0010.5 9zm0-2.25a.75.75 0 11-.75.75.75.75 0 01.75-.75z"></path>
# </svg></li-icon>
#   </button>
# </div>
#               <div class="msg-form__upload-attachment inline-block">
#   <input name="persist" value="true" type="hidden">
#   <input name="upload_info" type="hidden">
#   <input id="attachment-input-ember274" class="msg-form__attachment-upload-input hidden" accept="image/*,.ai,.psd,.pdf,.doc,.docx,.csv,.zip,.rar,.ppt,.pptx,.pps,.ppsx,.odt,.rtf,.xls,.xlsx,.txt,.pub,.html,.7z,.eml" data-control-name="overlay.file_select" type="file">
#   <button id="attachment-trigger-ember274" class="msg-form__footer-action artdeco-button artdeco-button--tertiary artdeco-button--circle artdeco-button--muted m0 artdeco-button--1" title="Attach a file to your conversation with " aria-label="Attach a file to your conversation with " type="button">
#     <span class="visually-hidden">
#       Attach a file to your conversation with 
#     </span>
#     <li-icon aria-hidden="true" type="paperclip-icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M15 5a4 4 0 01-1.17 2.83l-3.46 3.46A2.5 2.5 0 018.6 12a2.46 2.46 0 01-2.5-2.48 2.55 2.55 0 01.75-1.79L9.61 5 11 6.39 8.25 9.17a.49.49 0 00-.15.35.5.5 0 00.9.36l3.46-3.47a2 2 0 10-2.87-2.82l-6 6A2 2 0 005 13a2 2 0 001.42-.59l.18-.17L8 13.66l-.17.17a4 4 0 01-5.66-5.66l6-6A4 4 0 0115 5z"></path>
# </svg></li-icon>
#   </button>
# </div>
                
#                   <div class="tenor-gif__button relative">
#   <button title="Open GIF Keyboard" aria-label="Open GIF Keyboard" aria-expanded="false" id="ember291" class="msg-form__footer-action artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view" data-control-name="overlay.select_gif" type="button">  <li-icon aria-hidden="true" type="gif-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" width="16" height="16" focusable="false">
#   <path d="M9 12H7V4h2v8zM6 6V4H2a1 1 0 00-1 1v6a1 1 0 001 1h3a1 1 0 001-1V8H4v2H3V6h3zm9 0V4h-4a1 1 0 00-1 1v7h2V9h2V7h-2V6h3z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Open GIF Keyboard
# </span></button>
# </div>
              

# <!---->
              
#                 <div>
#   <span tabindex="-1" id="ember301" class="artdeco-hoverable-trigger artdeco-hoverable-trigger--content-placed-top ember-view">
#     <button title="Open Emoji Keyboard" aria-describedby="artdeco-hoverable-msg_overlay_emoji__emoji-hoverable__content" aria-label="Open Emoji Keyboard" aria-expanded="false" aria-controls="artdeco-hoverable-msg_overlay_emoji__emoji-hoverable__content" id="ember302" class="msg-form__footer-action emoji-hoverable-trigger artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view" type="button">  <li-icon aria-hidden="true" type="emoji-face-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" width="16" height="16" focusable="false">
#   <path d="M4.84 6A1.16 1.16 0 116 7.17 1.17 1.17 0 014.84 6zM8 9.38a3.51 3.51 0 01-2.3-.81l-.83 1.29a4.87 4.87 0 006.25 0l-.82-1.28a3.51 3.51 0 01-2.3.8zm2-4.55A1.17 1.17 0 1011.16 6 1.17 1.17 0 0010 4.83zM8 2.88A5.12 5.12 0 112.88 8 5.12 5.12 0 018 2.88M8 1a7 7 0 107 7 7 7 0 00-7-7z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Open Emoji Keyboard
# </span></button>
      
#   </span>

#     <div id="msg_overlay_emoji__emoji-hoverable__content" class="ember-view"><div id="ember304" class="ember-view"></div></div>
# </div>
            

#           </div>
#           <div class="msg-form__right-actions display-flex align-items-center">
            
# <div>
#     <button class="msg-form__send-button artdeco-button artdeco-button--1" disabled="" type="submit">
#       Send
#     </button>
# </div>
            
# <div class="msg-form__hovercard-container ml2 relative">
#   <span tabindex="-1" id="ember276" class="artdeco-hoverable-trigger artdeco-hoverable-trigger--content-placed-top ember-view">
#     <button aria-describedby="artdeco-hoverable-artdeco-gen-43" aria-expanded="false" aria-controls="artdeco-hoverable-artdeco-gen-43" id="ember277" class="msg-form__send-toggle artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view" type="button">  <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
#   <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
# </svg></li-icon>

# <span class="artdeco-button__text">
#     Open send options
# </span></button>
#     <div id="artdeco-gen-43" class="ember-view"><div id="ember279" class="ember-view"></div></div>
#   </span>
# </div>
#           </div>
#         </footer>
        
# <!---->
# <div id="ember281" class="ember-view"><div id="ember282" class="ember-view"><!----></div></div>
      
# </form>

        
# <!---->
# <div id="ember284" class="ember-view"><div id="ember285" class="ember-view"><!----></div></div>
      
# <!---->
# <!---->
# <!---->

#             </div>

#   <div id="ember286" class="ember-view"><div id="ember287" class="ember-view"><!----></div></div>
# </div>