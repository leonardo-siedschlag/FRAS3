from selenium import webdriver
from Selenium.getText import getTextByXpath
import time
from WhatsZap.enviarWhats import EnviarWhats
#ANALISE BOLSA FRAS3

nav = webdriver.Chrome('/home/leo/Imagens/chromedriver')

def ClearElement(element):
    e = element.replace('R$', '')
    e2 = e.replace(',', '.')
    ef  = float(e2)
    return ef

def mainStart():
    
    #PAGE CORRETORA
    nav.get('https://www.google.com/finance/quote/FRAS3:BVMF?sa=X&ved=2ahUKEwjFiNK3tZiAAxWHHrkGHesOCmsQ3ecFegQIKBAf')
                                        
    #GET VALUE                          
    textoValue  =  getTextByXpath(nav, 'YMlKec.fxKbKc')
                    
    valorNegociacao = ClearElement(textoValue)
    print(valorNegociacao)
    if valorNegociacao == 13.09:
        EnviarWhats(nav, valorNegociacao, 1, 'Negociação Próxima do Valor! R$ ')
        try:
            nav.get('https://www.youtube.com/watch?v=JrN8NpsvfEk')
            time.sleep(5)
        except Exception as e:
            print(e)
        
i = 0
EnviarWhats(nav, 0.0, 0, 'Abertura do Whats Zapp! R$ ')
while i < 10:
    mainStart()
    time.sleep(30)
     
