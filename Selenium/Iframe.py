from Selenium.Click import  *
import time

def GoFrameByClickXpath(nav, tempo, xpath, name):
    time.sleep(tempo)
    janela1 = nav.window_handles[0]
    janela2 = nav.window_handles[1]
    nav.switch_to.window(janela2)
    nav.find_element("xpath", xpath).click()
    #FECHAR IFRAME
    time.sleep(0.5)
    ClickInputName(nav, name)
    nav.switch_to.window(janela1) 

def GoFrameTryClickInputButton(nav, tempo, name):
    try:
        time.sleep(tempo)
        janela1 = nav.window_handles[0]
        janela2 = nav.window_handles[1]
        nav.switch_to.window(janela2)
        #FECHAR IFRAME
        time.sleep(0.5)
        ClickInputName(nav, name)
        nav.switch_to.window(janela1) 
        return 1
    except:
        return 0