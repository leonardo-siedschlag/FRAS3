import time
from selenium.webdriver.common.by import By
from Selenium.Click import  *

def ImputName(nav, name, elemento):
    
    try:
        time.sleep(1.5)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').clear()
        time.sleep(1)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').send_keys(elemento)
    except:
        None

def ImputNameNotClear(nav, name, elemento):
    
    try:
        time.sleep(1)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').send_keys(elemento)
    except:
        None
        
def ImputNameWithTab(nav, name, elemento):
    try:
        time.sleep(1)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').send_keys(elemento)
        ClickByTab(nav)
    except:
        None

