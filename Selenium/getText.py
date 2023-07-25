from Selenium.Wait import WaitByClassName
from selenium.webdriver.common.by import By


def getTextByXpath(nav, classe):
    textoValue = ''
    try:
        WaitByClassName(nav, 5, classe)
        textoValue = nav.find_element(By.CLASS_NAME, classe).text
        return  textoValue
    except Exception as e:
        print(e)
        return textoValue
    
    
    #driver.find_element_by_class_name("current-stage").text