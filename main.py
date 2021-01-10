
'''
CHAD LIM JIN JIE
DBS/POSB IB login on Firefox using Selenium written in Python to retrieve bank account balance.
I DO NOT ENDORSE ANY MISUSE OF MY WORK.
'''

from selenium import webdriver

userid_field = '//*[@id="UID"]'
pin_field = '//*[@id="PIN"]'
login_btn = '/html/body/form[1]/div/div[7]/button[1]'

user_id = input('User ID: ')
pin = input('PIN: ')

firefox = webdriver.Firefox()

firefox.get('https://internet-banking.dbs.com.sg/IB/Welcome') # https://internet-banking.dbs.com.sg/IB/Welcome (DBS/POSB)

firefox.find_element_by_xpath(userid_field).send_keys(user_id)
firefox.find_element_by_xpath(pin_field).send_keys(pin)
firefox.find_element_by_xpath(login_btn).click()

firefox.implicitly_wait(10)
# firefox.execute_script('return document.querySelectorAll("frame")[1]')

# Handle the error gracefully
try:
  firefox.switch_to.frame('user_area')
  firefox.switch_to.frame('iframe1')
  balance = firefox.execute_script('return document.querySelectorAll("span")[18].innerText') 
  # return document.querySelectorAll("span")[18].innerText / return document.querySelectorAll("tspan")[1].innerHTML (Cash & Investments bar)
  # 18 (DBS), 20 (POSB)
  print(balance)
except Exception as e:
  print(e)
  print('Invalid User ID or PIN')


firefox.close() # Close Firefox
