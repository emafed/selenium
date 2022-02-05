from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from pyotp import *

postDescription = """
🤩🤩
"""

ser = Service(executable_path="chromedriver")
option = webdriver.ChromeOptions()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=ser, options=option)
wait = WebDriverWait(driver,10)
driver.get("--url--")

def acceptCookie():
  driver.find_element(By.CSS_SELECTOR, 'button[data-testid="cookie-policy-dialog-accept-button"]').click()

###Login To The Account
def login(id,password):
  email = driver.find_element_by_id("email")
  email.send_keys(id)
  Password = driver.find_element_by_id("pass")
  Password.send_keys(password)
  driver.find_element(By.ID, 'loginbutton').click()

  # inizio 2FA
  authField = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="approvals_code"]')))
  totp = TOTP("--otp code--")
  token = totp.now()
  authField.send_keys(token)
  driver.find_element(By.CSS_SELECTOR, 'button[name="submit[Continue]"]').click()
  but = wait.until(EC.presence_of_element_located((By.ID, 'checkpointSubmitButton')))
  but.click()
  pass

  
acceptCookie()
login("--mail--","--pwd--")

# apro CREA POST
bt = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="https://static.xx.fbcdn.net/rsrc.php/v3/yd/r/15bRQ3NEuws.png"]')))
bt.click()
l=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="facebook"]/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[6]/div[1]/div')))
l.click()

time.sleep(15)

actions= ActionChains(driver)
actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)

el = driver.switch_to.active_element
driver.execute_script("arguments[0].innerHTML = '{}'".format(postDescription),el)
actions.send_keys('.')
actions.send_keys(Keys.BACKSPACE)
#actions.send_keys(postDescription)
actions.send_keys(Keys.TAB * 17)
actions.perform()

'''
for g in l: 
  if g==driver.find_element_by_xpath("//input[@type='file'][@class='_n _5f0v']"): 
      g.send_keys("dsds") 
      print('image loaded')
'''