#!/usr/bin/env python
# coding: utf-8

# In[1]:

from selenium import webdriver
import wait

import time
user_name=input("Enter user name : " )


# In[4]:
wd=webdriver.Chrome('chromedriver')
wd.get("https://www.instagram.com/")
#wd.maximize_window()

# In[9]:
#login
#time.sleep(6)
wait.wait("Loading",6)
wd.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF     "]').click()

# In[10]:
emailf = input("Enter FB email/phone : ")
passwordf = input("Enter password : ")

email=wd.find_element_by_id('email')
email.send_keys(emailf)

password=wd.find_element_by_id('pass')
password.send_keys(passwordf)
#time.sleep(15)

wd.find_element_by_id('loginbutton').click()
wd.implicitly_wait(10)

# In[12]:
try:
    wd.find_element_by_xpath('//*[contains(text(),"Not Now")]').click()

# In[15]:
except:
    time.sleep(5)
    wd.find_element_by_xpath('//*[contains(text(),"Not Now")]').click()


wd.find_element_by_xpath('//span[@class="_2dbep qNELH"]').click()

# In[16]:
wd.find_element_by_xpath('//*[contains(text(),"Profile")]').click()


# In[17]:
#for the followers
print("Getting followers' list")
wd.find_element_by_xpath('//a[@href="/'+user_name+'/followers/"]').click()


# ### the purpose of this scrollbox code is to load all the profiles in the scroll box by automatically scrolling to the end. in the end, this scrollbox contains the links of all the profiles that are loaded.

# In[18]:
wd.implicitly_wait(10)
time.sleep(5)
scroll_box = wd.find_element_by_xpath('//div[@class="isgrP"]')
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht

    time.sleep(1)
    ht = wd.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)


# In[20]:
links = scroll_box.find_elements_by_tag_name('a')
followers = [name.text for name in links if name.text != '']

# In[25]:
wd.find_elements_by_xpath('//div[@class="QBdPU "]')[1].click()

# In[26]:

wd.implicitly_wait(10)
#for following
print("Getting following people's list")
wd.find_element_by_xpath('//a[@href="/'+user_name+'/following/"]').click()

# In[37]:
wd.implicitly_wait(10)
time.sleep(5)
scroll_box = wd.find_element_by_xpath('//div[@class="isgrP"]')
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    time.sleep(1)
    ht = wd.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)



# In[28]:
profile_links = scroll_box.find_elements_by_tag_name('a')

# In[29]:
#print(profile_links)
# In[30]:
following = [name.text for name in profile_links if name.text != '']

# In[31]:
#print(names)

# In[32]:
# to compare the lists of names
non_followers=[x for x in following if x not in followers]
u_dont_followback=[x for x in followers if x not in following]
print("------RESULT------")
print("Total specimens who don't follow back : ",len(non_followers))
print("Specimens who don't follow back  : ",)
for i in non_followers:
    print(i)
print("About you : ")
print("Specimens you don't follow back : ",len(u_dont_followback))


wd.close()

