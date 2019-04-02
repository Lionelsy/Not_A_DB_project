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

brower.find_element_by_name('inputuin').send_keys("Your mail address") # school email
brower.find_element_by_name('pp').send_keys("Your password") # school email password
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

brower.switch_to.frame("mainFrame")




