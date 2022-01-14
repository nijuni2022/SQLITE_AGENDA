import os
import sqlite3
from sqlite3 import Error

##Conexão
def ConexaoBanco():
    caminho='c:\\Users\\junio\\Documents\\SQLITE\\agenda.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)

    finally:
        print("Operacao Realizada com sucesso")
        conexao.close()

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    #conexao.close()
    return res




def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")


def menuInserir():
    os.system("cls")
    vnome=input("Digite o nome: ")
    vtelefone=input("Digite o telefone: ")
    vemail=input("Digite o email: ")
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    query(vcon,vsql)


def menuDeletar():
    print()

def menuAtualizar():
    print()


def menuConsultarID():
    print()


def menuConsultarNome():
    print()




opc=0
while opc!=6:
    menuPrincipal()
    opc=int(input("Digite uma opção: "))

    if opc==1:
        menuInserir()

    elif opc==2:
        menuDeletar()

    elif opc==3:
        menuAtualizar()

    elif opc==4:
        menuConsultarID()

    elif opc==5:
        menuConsultarNome()

    elif opc==6:
        os.system("cls")
        print("Programa finalizado")
    
    else:
        os.system("cls")
        print("opção invalida")
        os.system("pause")

vcon.close()
os.system("pause")
        




