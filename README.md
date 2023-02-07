# linkedin-outreach
A simple python script to automate sending messages on LinkedIn. 

This is a python script built using selenium to automatically send messages to users on LinkedIn. I built this when I had to do cold outreach to potential users while working on my previous startup. 

How to use this script to do mass outreach: 

1. In the "linkedin_outreach.py" file, enter your credentials in the variables "id" and "pw". 
2. Enter the links of the profiles you want to reach out to in the "profiles" array. Mind you, these profiles must be in your network and you should be able to send a message to them.
3. Enter the message you'd like to send to all the profiles in the outreach_message variable. This message will be sent to each of the profiles in the "profiles" array.
4. This version of the script also keeps a record of all the profiles you've reached out to in a google sheet. To use this, you'll have to enter your google credentials and the ID of the worksheet you'd like to use in the "contactsheet.py" file.

