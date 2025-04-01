import os
import textwrap

opcoes_menu = ["Depositar", "Sacar", "Extrato", "Criar usuário", "Criar conta", "Listar contas", "Sair"]

saldo = 0
LIMITE_POR_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
usuarios = []
AGENCIA = "0001"
contas = []

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

def exibir_extrato(saldo, /, *, extrato):
    limpar_tela()

    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")

    input("\nPressione 'enter' para sair ")

    limpar_tela()    

def filtrar_usuario(cpf, usuarios):
    """Retorna o usuário com o CPF correspondente, se existir."""
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_usuario(usuarios):
    limpar_tela ()

    cpf = input("Informe seu CPF: ").replace("-", "").replace(".", "")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n❗ Já existe usuário com esse CPF cadastrado!")

        input("\nPressione 'Enter' para continuar...")

        limpar_tela()
        
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    print("\nEndereço\n")
    logradouro = input("Logradouro: ")
    nro = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla): ")

    endereco = {
        "logradouro": logradouro,
        "nro": nro,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado
    }

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\n✅ Usuário criado com sucesso!")

    input("\nPressione 'Enter' para continuar...")

    limpar_tela()

def criar_conta(agencia, numero_conta, usuarios):
    limpar_tela()

    cpf = input("Informe seu CPF: ").replace("-", "").replace(".", "")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")

        input("\nPressione 'Enter' para continuar...")

        limpar_tela()

        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado")
    
    input("\nPressione 'Enter' para continuar...")

    limpar_tela()

    return None

def listar_contas(contas):
    
    limpar_tela()

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))
        # print(linha)

        input("\nPressione 'Enter' para continuar...")

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
        exibir_extrato(saldo, extrato=extrato)
    
    elif opcao_selecionada == 4:
        criar_usuario(usuarios)
    
    elif opcao_selecionada == 5:
        numero_conta = len(contas)+1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao_selecionada == 6:
        listar_contas(contas)
    
    else:
        break

limpar_tela()
print("PyBank encerrado com sucesso")