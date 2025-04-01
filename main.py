import os

opcoes_menu = ["Depositar", "Sacar", "Extrato", "Nova Conta", "Listar Contas", "Novo Usuário", "Sair"]

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

def depositar(saldo, valor, extrato, /):
    
    limpar_tela()
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido")
        input("\nPressione 'Enter' para para continuar...")
        limpar_tela()
        return saldo, extrato
    
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("\n✅ Depósito realizado com sucesso!")

    input("\nPressione 'Enter' para continuar...")
    limpar_tela()
    return saldo, extrato

def sacar(*, saldo, valor, extrato, LIMITE_POR_SAQUE, numero_saques, LIMITE_SAQUES_DIARIOS):
    
    limpar_tela()

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_POR_SAQUE
    excedeu_saques_diarios = numero_saques >= LIMITE_SAQUES_DIARIOS

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido")
        input("\nPressione 'Enter' para para continuar...")
        limpar_tela()
        return saldo, extrato
    if excedeu_saldo:
        print(f"Operação falhou! Saldo insuficiente\nSaldo R$ {saldo}")
        return saldo, extrato
    if excedeu_limite:
        print(f"Operação falhou! O valor do saque execede o limite\nLimite R$ {LIMITE_POR_SAQUE}")
        return saldo, extrato
    if excedeu_saques_diarios:     
        print(f"Operação falhou! Número máximo de saques excedito.\nLimite de saques diários: {LIMITE_SAQUES_DIARIOS}")
        return saldo, extrato
    
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    print("\nSaque realizado com sucesso!")
 
    input("\nPressione 'enter' para sair ")
    limpar_tela()

    return saldo, extrato 

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
        valor = float(input("Informe o valor do depósito R$: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao_selecionada == 2:
        valor = float(input("Informe o valor do saque R$: "))
        saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            LIMITE_POR_SAQUE = LIMITE_POR_SAQUE,
            numero_saques = numero_saques,
            LIMITE_SAQUES_DIARIOS = LIMITE_SAQUES_DIARIOS           
        )
    
    elif opcao_selecionada == 3:
        exibir_extrato()
    
    elif opcao_selecionada == 4:
        ...
    
    elif opcao_selecionada == 5:
        ...
    
    elif opcao_selecionada == 6:
        ...
    
    else:
        break

limpar_tela()
print("PyBank encerrado com sucesso")