import requests
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
from urllib.request import urlopen
from datetime import datetime
import json

plt.style.use('classic')
sb.set(rc={'figure.figsize':(15,8)})

#----------------------------------------------------------------------
# IMPORTA OS DADOS DAS ESTEIRAS EM UM DICT JSON
#----------------------------------------------------------------------
def Carrega_Esteira():
    # url = "https://dry-plateau-13546.herokuapp.com/esteira"
    # response = urlopen(url)
    # dict_json = json.loads(response)
    # response.close()
    r = requests.get('https://dry-plateau-13546.herokuapp.com/esteira')
    dict_json = r.json()
    return dict_json['rows']

#----------------------------------------------------------------------
# FILTRA A ESTEIRA DESEJADA
#----------------------------------------------------------------------
def Obter_esteira(list_json,num_esteira):
    esteira = list_json[num_esteira-1]
    return esteira

#----------------------------------------------------------------------
# IMPRIME OS DADOS MESTRE DA ESTEIRA DESEJADA
#----------------------------------------------------------------------
def Imprime_Esteira(esteira):
    print('-----------------------------------------------')
    print('DADOS DA ESTEIRA N. ' + str(esteira['id']))
    print('-----------------------------------------------')
    print('Velocidade | Velocidade | Horario de registro  ')
    print(' do  rolo  | da esteira |                      ')
    print('-----------------------------------------------')

    v_rolo = esteira['velocidade_rolo']
    v_esteira = esteira['velocidade_esteira']
    data = datetime.strptime(esteira['timestamp'][0:10], '%Y-%m-%d').date()
    hora = datetime.strptime(esteira['timestamp'][11:19], '%H:%M:%S').time()
    print(f'{v_rolo: >10.2f} | {v_esteira: >10.2f} | {data: %d/%m/%Y} {hora: %H:%M:%S}')
    #print("--------------------------------------------------------------")
    #print(dict_json['detalhes'][1]['velocidade_rolo'])

#----------------------------------------------------------------------
# IMPRIME OS DADOS DOS DETALHES DA ESTEIRA DESEJADA
#----------------------------------------------------------------------
def Imprime_Detalhes_Esteira(esteira):
    print(" ")
    print("                    Detalhes")
    print('------------------------------------------------------')
    print(' ID  | Velocidade | Velocidade | Horario de registro  ')
    print('     |  do  rolo  | da esteira |                      ')
    print('------------------------------------------------------')
    i = 0
    for detalhe in esteira['detalhes']:
        i = i + 1
        v_rolo = detalhe['velocidade_rolo']
        v_esteira = detalhe['velocidade_esteira']
        data = datetime.strptime(detalhe['timestamp'][0:10], '%Y-%m-%d').date()
        hora = datetime.strptime(detalhe['timestamp'][11:19], '%H:%M:%S').time()
        print(f'{i:>4} | {v_rolo: >10.2f} | {v_esteira: >10.2f} | {data: %d/%m/%Y} {hora: %H:%M:%S}')

#----------------------------------------------------------------------
# IMPRIME A TABELA RESUMIDA DAS ESTEIRAS
#----------------------------------------------------------------------
def Tabela_Resumida():
    print('------------------------------------------------------')
    print('                TABELA RESUMIDA')
    print('------------------------------------------------------')
    print(' ID  | Velocidade | Velocidade | Horario de registro  ')
    print('     |  do  rolo  | da esteira |                      ')
    print('------------------------------------------------------')
    for linha in list_json:
        i = linha['id']
        v_rolo = linha['velocidade_rolo']
        v_esteira = linha['velocidade_esteira']
        data = datetime.strptime(linha['timestamp'][0:10], '%Y-%m-%d').date()
        hora = datetime.strptime(linha['timestamp'][11:19], '%H:%M:%S').time()
        print(f'{i:>4} | {v_rolo: >10.2f} | {v_esteira: >10.2f} | {data: %d/%m/%Y} {hora: %H:%M:%S}')
    print('------------------------------------------------------')

#----------------------------------------------------------------------
# IMPRIME A TABELA COMPLETA DAS ESTEIRAS
#----------------------------------------------------------------------
def Tabela_Completa(qde):
    for num_esteira in range(qde+1):
        esteira = Obter_esteira(list_json,num_esteira)
        Imprime_Esteira(esteira)
        Imprime_Detalhes_Esteira(esteira)

#----------------------------------------------------------------------
# ROTINA PRINCIPAL
#----------------------------------------------------------------------
list_json = Carrega_Esteira()
# json_pd = list_json

# qde_esteiras = len(list_json)
# print("Quantidade de esteiras registradas: ",qde_esteiras)

# Tabela_Resumida()

# distribuicao = json_pd.describe()
# print(json_pd['velocidade_rolo'].value_counts())
# json_pd['velocidade_rolo'].hist()
