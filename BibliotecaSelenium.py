#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Selenium controla o navegador faz automações web
#Controla a plataforma
#Webdriver permite que o selenium controle o navegador
# Para aprender, vamos usar o Python para preemcher um formulário na internet
#Para o código funcioncar deve-se baixar
# chrome -> chromedriver
# firefox -> geckodriver
# fazer o doanwload do driver referente a versão que está sendo usada
# o chrome driver ou o geckodriver eles param de funcionar caso tenha alguma atualização
# para isso deve ser automizado o código vai identificar a versao do seu navegador
# e fazer a atualização de acordo com a sua atualização


# In[21]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)


# In[22]:


navegador.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M')


# In[23]:


navegador.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Gustavo')


# In[24]:


navegador.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('175010')

navegador.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()