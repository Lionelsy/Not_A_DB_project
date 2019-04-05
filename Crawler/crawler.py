#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
from selenium.common import exceptions

def find(brower):
    element = brower.find_elements_by_tag_name("a")
    if element:
        return element
    else:
        return False

url = 'https://exmail.qq.com'
brower = webdriver.Firefox()

brower.get(url)
time.sleep(2)

login = brower.find_element_by_xpath("//a[@class='index_topbar_btn index_topbar_btn_login']")
login.click()

time.sleep(1.1)
input_info=brower.find_element_by_xpath("//a[@class= 'js_show_pwd_panel']")
input_info.click()

brower.find_element_by_name('inputuin').send_keys('Your Email Address')
brower.find_element_by_name('pp').send_keys("Your Email Password")
brower.find_element_by_name("btlogin").click()
time.sleep(1.1)

# Start to find the address list

address_list = brower.find_element_by_xpath("//li[@class='addrpart fs']")
address_list.click()

brower.switch_to.frame("mainFrame")
brower.implicitly_wait(5)

links = brower.find_elements_by_tag_name("a")
data_url = None
import_link = None
for i in range(0, 22):
   try:
        links = brower.find_elements_by_tag_name("a")
        for link in links:
            if "show_party_list" in link.get_attribute("href"):
                data_url = link.get_attribute("href")
                import_link = link
   except exceptions.StaleElementReferenceException:
       pass

import_link.click()

brower.implicitly_wait(0.5)
for i in range(0, 10):
   try:
       brower.switch_to.default_content()
   except exceptions.NoSuchFrameException:
       pass

brower.switch_to.frame("mainFrame")


# > Open your favirate webbrowser, and the program will open the page where there contain a lots of people infomation

# In[2]:


tree_nodes=brower.find_elements_by_xpath("//li[@class= 'tree_node close']")


# In[3]:


x = None
for node in tree_nodes:
    if node.get_attribute('node_id') == 'nid10003':
        x = node
        print(x.get_attribute('node_id'))


# > test whether I did right or not

# In[4]:


x.click()
tree_nodes=brower.find_elements_by_xpath("//li[@class= 'tree_node close']")


# > find all the grade

# In[5]:


needed_nodes = []
for i in range(0, 22):
    try:
        for node in tree_nodes:
            if node.get_attribute('node_id') == 'nid10064':
                needed_nodes.append(node)
            if node.get_attribute('node_id') == 'nid10065':
                needed_nodes.append(node)
            if node.get_attribute('node_id') == 'nid10066':
                needed_nodes.append(node)
            if node.get_attribute('node_id') == 'nid10067':
                needed_nodes.append(node)
    except exceptions.StaleElementReferenceException:
        pass  
    
needed_nodes=list(set(needed_nodes))


# > locate all the classes

# In[6]:


for node in needed_nodes:
    print(node.get_attribute('node_id'))


# > print them on the screen

# In[7]:


for node in needed_nodes:
    node.click()


# > show all the classes from 2015 grade to 2018 grade

# In[8]:


import re
class_list= []
for i in range(0, 22):
    try:
        class_list = brower.find_elements_by_xpath( "//li[@class= 'tree_node close']" )
    except exceptions.StaleElementReferenceException:
        pass  
class_list= list(set(class_list))


# > find all the class append them int the class_list

# In[11]:


real_list= []
for i in range(0, 22):
    try:
        for cl in class_list:
            nid = cl.get_attribute('node_id')
            if re.match('nid10+(1[1-9][1-9]|2[0-3][0-9])',nid):
                real_list.append(cl)
    except exceptions.StaleElementReferenceException:
        pass
real_list= list(set(real_list))


# In[12]:


for rl in real_list:
    print(rl.get_attribute('node_id'))
    


# > Test whether I did right or not

# In[14]:


for rl in real_list:
    rl.click()
    brower.implicitly_wait(1)


# In[19]:


person_list= []
for i in range(0, 22):
    try:
        person_list = brower.find_elements_by_xpath( "//li[@class= 'tree_node ']" )
    except exceptions.StaleElementReferenceException:
        pass  
person_list= list(set(person_list))


# In[20]:


for person in person_list:
    print(person.get_attribute('node_id'))


# In[33]:


sorted_person=[]
sorted_person = sorted(person_list, key = lambda x: x.get_attribute('node_id'))


# In[34]:


for person in sorted_person:
    print(person.get_attribute('node_id'))


# > Get all the persons' tags

# In[35]:


import csv


# In[36]:


head = ['id', 'name']


# In[37]:


person_string= []
for person in sorted_person:
    person_dict = dict()
    person_dict[head[0]] = person.get_attribute('node_alias')[0:8]
    person_dict[head[-1]] =person.text
    person_string.append(person_dict)


# In[39]:


with open('../data/students_info.csv', 'a', newline='') as csvfile:
    #The file path may be different on windows machine
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for person in person_string :
        writer.writerow(person)


# Write the data into a csv file

# In[ ]:




