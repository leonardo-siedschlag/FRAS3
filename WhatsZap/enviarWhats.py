import time
from Selenium.Click import ClickByEnter
from Selenium.Wait import  WaitByXpath
from selenium.webdriver.common.by import By

def EnviarWhats(nav, valorNegociacao, open, msn):

    #WHATS ABERTO
    if open == 0:
        nav.execute_script("window.open('https://web.whatsapp.com/', '_blank')")

    #VAI PARA ABA WHATS
    nav.switch_to.window(nav.window_handles[1])  
    WaitByXpath(nav, 45, '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button/div[2]/span')
    
    #CLICK PESQUISAR(lupa)          
    nav.find_element("xpath", '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button/div[2]/span').click()
    
    #INSERE NOME NA PESQUISA
    time.sleep(1.5)
    nav.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys('leonardo siedschlag')
    time.sleep(1.5)
    ClickByEnter(nav)

    #DIGITA VALOR
    time.sleep(1)
    nav.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/div[1]/p').send_keys(msn+str(valorNegociacao))
    
    #ENTER
    ClickByEnter(nav)
    
    #RETORNA DA ABA WHATS
    time.sleep(2)
    nav.switch_to.window(nav.window_handles[0]) 