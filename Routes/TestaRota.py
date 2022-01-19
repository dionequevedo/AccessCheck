import socket
from csv import reader as rd
from telnetlib import Telnet as tn
from requests import get as GET
from requests import ConnectionError as CE

# Strings

id = 0
url = ''
port = 0

"""
    Function check_http https://gist.github.com/yasinkuyu/aa505c1f4bbb4016281d7167b8fa2fc2
"""

def check_Http(id: int, url: 'endereço http a ser testado'):
    """
    Recebe uma url e testa o acesso HTTP ou HTTPS conforme a porta fornecedida

    :param id: Ordem da URL
    :param url: URL para ser testada
    :param port: Porta a ser utilizada, caso não seja informada será utilizada a porta 443
    :return: Retorna uma string informando se a conexão foi bem sucedida ou não
    """
    if verifica_Se_Http_Ou_Https(url):
        try:
            _ = GET(url, timeout=100)
            print("{0}\t- {1} ==> HTTP ==> Conexão realizada com sucesso!".format(id, url))
            return True
        except CE:
            print("{0}\t- {1} ==> HTTP ==> Conexão recusada!".format(id, url))
            return False


def check_Telnet(id: int, url, port=23):
    """
    Recebe uma url e testa o acesso TELNET conforme a porta fornecedida

    :param id: Ordem da URL
    :param url: URL para ser testada
    :param port: Porta a ser utilizada, caso não seja informada será utilizada a porta 23
    :return: Retorna uma string informando se a conexão foi bem sucedida ou não
    """
    try:
        session = tn(url, port, timeout=100)
        print("{0}\t- {1}:{2} ==> Telnet ==> Connected!".format(id, url, port))
    except socket.timeout:
        print("{0}\t- {1}:{2} ==> Telnet ==> SOCKET Timeout!".format(id, url, port))
    except socket.gaierror:
        print("{0}\t- {1}:{2} ==> Telnet ==> GetAddrInfo Failed!".format(id, url, port))


def verifica_Se_Http_Ou_Https(url):
    if(url[0:5] == 'http:'):
        return True
    elif(url[0:5] == 'https'):
        return True
    else:
        return False


def le_Arquivo_Gera_Lista():
    with open("hosts.csv", "r", encoding='utf-8-sig') as a:
        lista = rd(a, delimiter=';')
        for item in lista:
            id = int(item[0])
            url = item[1]
            if int(item[2]) > 0:
                port = int(item[2])
                newUrl = "{0}{1}{2}".format(url, ':', port)
                check_Http(id, newUrl)
                check_Telnet(id, url, port)
            else:
                check_Http(id, url)
                check_Telnet(id, url)


le_Arquivo_Gera_Lista()
