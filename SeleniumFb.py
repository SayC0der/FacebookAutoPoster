from selenium import webdriver
import os
import time
from Auth import username, password

#Browser Options
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")  # Hide the Browser
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
    })
chrome = webdriver.Chrome(options=chrome_options)

#Authentication
chrome.get("https://facebook.com/login")
data = chrome.find_element_by_id("email")
data.send_keys(username)
data = chrome.find_element_by_id("pass")
data.send_keys(password)
time.sleep(3)
data.submit()
time.sleep(6)

#Groups to Post in
static_url = "https://www.facebook.com/groups/"
targets = ['group1', 'group2', 'group3', '', '', '', '', '', '', '', '', '', '', '', '']


#Start posting in every group
for i in targets :
    # Browse the target Page
    link = static_url + str(i)
    chrome.get(link)
    time.sleep(8)
    #Group Infos
    grp_name = chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/h2/span')
    grp_fans = chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/span/div/div[3]')
    print(str(i), " : " ,grp_name.text, ' : ' , grp_fans.text) 

    # Click on the Post Zone
    post_box=chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span')
    post_box.click()
    time.sleep(5)

    #Post the message       
    message = "your msg or link or both, <Important : leave the blank space at the end> "
    text_area = chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
    text_area.send_keys(str(message))
    time.sleep(5)
    print("published")

    post_button = chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div')
    post_button.click()
    time.sleep(10)

    
