#!/usr/bin/env python
# coding: utf-8

# #### Vamos supor que queremos inserir dados de uma planilha e inserir em um sistema desktop.
# ### Para simular usaremos o google sheets.
# ### Tiraremos informações de uma planilha e vamos coloca-la no sistema.
Importe a biblioteca e depois faça uma leitura do arquivo.
Para fazer isso e necessario passar o endereço do arquivo.
# In[10]:


import pandas as pd
arquivo = pd.read_excel('C:/Users/User/Desktop/arquivo.xlsx')


# In[11]:


arquivo.head()


# In[12]:


import pyautogui
pyautogui.alert("O código vai começar. Não mexa no PC")
pyautogui.hotkey('win','r')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.sleep(0.5)
pyautogui.write('https://docs.google.com/spreadsheets/d/1vmzLUawZgrTXDSLhyZ1iPXxZWcW8q4TwafujWTB_esw/edit#gid=0')
pyautogui.press('enter')
pyautogui.sleep(1)
for i in range(11):
    pyautogui.sleep(1)
    pyautogui.typewrite(arquivo["Codigo"][i])
    pyautogui.press('right')
    # Se a coluna não for do tipo texto deve converter a coluna em STRING(STR)
    pyautogui.typewrite(str(arquivo["QTD"][i]))
    pyautogui.press('right')
    pyautogui.typewrite(str(arquivo["Data"][i]))
    pyautogui.press('right')
    pyautogui.typewrite(str(arquivo["Obs"][i]))
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.typewrite(str(arquivo["C.C"][i]))
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','left')


# In[ ]:


Para descobrir a quantidade de linhas que tem no arquivo para colocar no cod for i in range(11):


# In[5]:


linhas = arquivo.shape[0]
print(arquivo)

