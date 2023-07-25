from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

def SelectNameByVisibleText(nav, name, elemento):
    
    try:
        time.sleep(1)
        Select(WebDriverWait(nav, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[name="'+name+'"]')))).select_by_visible_text(elemento)
    except:
        None

def SelectNameByValue(nav, name, elemento):
    try:
        Select(WebDriverWait(nav, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[name="'+name+'"]')))).select_by_value(elemento)
    except:
        None
    