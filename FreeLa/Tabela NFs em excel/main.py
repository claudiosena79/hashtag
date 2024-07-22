#Biblioteca que transforma xml num dicionário
import xmltodict
# Biblioteca pra visualizao o dicionário de maneira mais intuitiva
#from pprint import pprint
#Biblioteca para abrir arquivos
import os
#Biblioteca pra construir a tabela
import pandas as pd


def pegar_informacoes(nome_arquivo, lista_valores):
    print(f'pegando informações do {nome_arquivo}')
    with open(f'nfs/{nome_arquivo}', 'rb') as arquivo_xml:
        dicionario_arquivo = xmltodict.parse(arquivo_xml)
        
        
        if 'NFe' in dicionario_arquivo:
            informacoes_nota = dicionario_arquivo['NFe']['infNFe']
        else:
            informacoes_nota = dicionario_arquivo['nfeProc']['NFe']['infNFe']
        numero_nota = informacoes_nota['@Id']
        cliente_nota = informacoes_nota['dest']['xNome']
        if 'CNPJ' in informacoes_nota['dest']:
            documento_cliente = informacoes_nota['dest']['CNPJ']
        else:
            documento_cliente = informacoes_nota['dest']['CPF']
        endereco_cliente = informacoes_nota['dest']['enderDest']
        emissor_nota = informacoes_nota['emit']['xNome']
        if 'CNPJ' in informacoes_nota['emit']:
            documento_emissor = informacoes_nota['emit']['CNPJ']
        else:
            documento_emissor = informacoes_nota['emit']['CPF']
        endereco_emissor = informacoes_nota['emit']['enderEmit']
        transportador_nota = informacoes_nota['transp']['transporta']['xNome']
        if 'CNPJ' in informacoes_nota['transp']['transporta']:
            documento_transportador = informacoes_nota['transp']['transporta']['CNPJ']
        else:
            documento_transportador = informacoes_nota['transp']['transporta']['CPF']
        if 'vol' in informacoes_nota['transp']:
            peso_nota = informacoes_nota['transp']['vol']['pesoB']
        else:
            peso_nota = 'PESO NÃO DECLARADO'

        lista_valores.append([numero_nota, cliente_nota, documento_cliente, endereco_cliente, emissor_nota, documento_emissor, endereco_emissor, transportador_nota, documento_transportador, peso_nota])
       
        

        

lista_arquivos = os.listdir('nfs')

colunas = ['numero NFe', 'Nome do Cliente', 'Documento do Cliente', 'Endereço do Cliente','Nome Emissor', 'Documento Emissor', 'Endereco Emissor', 'Nome Transportador', "Documento Transportador", 'Peso Nota']
lista_valores = []

for arquivo in lista_arquivos:
    pegar_informacoes(arquivo, lista_valores)

tabela = pd.DataFrame(columns= colunas, data= lista_valores)
tabela.to_excel('TabelaNotasFiscais.xlsx', index= False)
    
