import os

opcoes_menu = ["Depositar", "Sacar", "Extrato", "Sair"]

saldo = 0
LIMITE_POR_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")    
def exibir_titulo():
    titulo = "Bem-vindo ao PyBank"
    borda = "-"*len(titulo)

    print(borda)
    print(titulo.center(len(borda)))
    print(f"{borda}\n")
def listar_opcoes():
    for indice, opcao in enumerate(opcoes_menu, start=1):
        print(f"[{indice}] - {opcao}")
def selecionando_opcao():
    while True:
        try:
            opcao = int(input("\nO que deseja fazer? "))

            if 0 < opcao <= len(opcoes_menu):
                return opcao
            else:
                print("\nPor favor! Selecione uma opção válida")            
        except ValueError:
            print("\nPor favor! Selecione uma opção válida")

def depositar():
    global saldo, extrato  # <- declare as variáveis globais

    limpar_tela()

    valor = float(input("Informe o valor do depósito R$: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("[ERROR] - O valor informado é inválido")
    
    input("\nPressione 'enter' para sair ")

    limpar_tela()

def sacar():
    global saldo, extrato, numero_saques

    limpar_tela()

    valor = float(input("Informe o valor do saque R$: "))

    if valor > saldo:
        print(f"Operação falhou! Saldo insuficiente\nSaldo R$ {saldo}")
    elif valor > LIMITE_POR_SAQUE:
        print(f"Operação falhou! O valor do saque execede o limite\nLimite R$ {LIMITE_POR_SAQUE}")
    elif numero_saques >= LIMITE_SAQUES_DIARIOS:
        print(f"Operação falhou! Número máximo de saques excedito.\nLimite de saques diários: {LIMITE_SAQUES_DIARIOS}")
    elif valor < 0:
        print("Operação falhou! O valr informado é inválido")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    input("\nPressione 'enter' para sair ")

    limpar_tela()

def exibir_extrato():
    limpar_tela()

    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")

    input("\nPressione 'enter' para sair ")

    limpar_tela()    

while True:
    exibir_titulo()

    listar_opcoes()

    opcao_selecionada = selecionando_opcao()

    if opcao_selecionada == 1:
        depositar()
    elif opcao_selecionada == 2:
        sacar()
    elif opcao_selecionada == 3:
        exibir_extrato()
    else:
        break

limpar_tela()
print("PyBank encerrado com sucesso")