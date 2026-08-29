import random
import os
contas = []

def LimparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

LimparTerminal()


def verificar_numero(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor < 0:
                print("\nDigite um número positivo!")
            else:
                return valor

        except ValueError:
            print("\nDigite apenas números!")


def verificar_texto(mensagem):
    while True:
        valor = input(mensagem)

        if valor.strip() == "":
            print("\nO campo não pode ficar vazio!")

        elif valor.replace(" ", "").isalpha():
            return valor

        else:
            print("\nDigite apenas texto!")


def verificar_vazio(mensagem):
    while True:
        valor = input(mensagem)

        if valor.strip() == "":
            print("\nO campo não pode ficar vazio!")
        else:
            return valor


def verificar_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor <= 0:
                print("\nDigite um valor maior que zero!")
            else:
                return valor

        except ValueError:
            print("\nDigite apenas números!")


def ja_existe(campo, valor):
    for conta in contas:
        if str(conta[campo]).lower() == str(valor).lower():
            return True

    return False


def encontrar_conta(campo, valor):
    for conta in contas:
        if str(conta[campo]).lower() == str(valor).lower():
            return conta

    return None


def gerar_chave_acesso():
    while True:
        chave = random.randint(1, 1000)

        if not ja_existe("chave de acesso", chave):
            return chave


def cadastro():
    print("\n( + ======== BANCO IFRN CADASTRO ========== + )\n")

    while True:
        nome = verificar_texto("Nome: ")

        if ja_existe("nome", nome):
            print("\nEsse nome já está cadastrado!")
        else:
            break

    while True:
        pix = verificar_vazio("Crie uma chave Pix: ")

        if ja_existe("pix", pix):
            print("\nEssa chave Pix já está cadastrada!")
        else:
            break

    chave_acesso = gerar_chave_acesso()

    print(f"\nSua chave de acesso é: {chave_acesso}")
    print("Guarde essa chave para fazer login!")

    contas.append({
        "nome": nome,
        "pix": pix,
        "chave de acesso": chave_acesso,
        "saldo": 0.0,
        "extrato": []
    })

    print("\nConta cadastrada com sucesso!")


def login():
    if not contas:
        print("\nNenhuma conta cadastrada!")
        return None

    print("\n( + ========== BANCO IFRN LOGIN ========== + )\n")
    print()

    pix = verificar_vazio("Digite sua chave Pix: ")
    chave = verificar_numero("Digite sua chave de acesso: ")

    conta = encontrar_conta("pix", pix)

    if conta is not None and conta["chave de acesso"] == chave:
        print(f"\nLogin realizado com sucesso, {conta['nome']}!")
        return conta

    print("\nPix ou chave de acesso incorretos!")

    return None


def ver_conta(conta):
    print("\n═════════════════════════════════════════════════")
    print("                  SUA CONTA                 ")
    print("═════════════════════════════════════════════════")
    print(f" Nome:   {conta['nome']:<18}               ")
    print(f" Pix:    {conta['pix']:<18}                ")
    print(f" Chave:  {conta['chave de acesso']:<18}    ")
    print(f" Saldo:  R$ {conta['saldo']:<13.2f}        ")
    print("═════════════════════════════════════════════════")


def ver_saldo(conta):
    print(f"\nSeu saldo é: R$ {conta['saldo']:.2f}")


def ver_extrato(conta):

    if not conta["extrato"]:
        print("\nExtrato: Nenhuma movimentação realizada!")
        return

    for movimento in conta["extrato"]:
        print(f"\nSeu extrato é: {movimento}")


def deposito(conta):
    print("\n( + ========== DEPÓSITO ========== + )")

    valor = verificar_valor("Valor do depósito: R$ ")

    conta["saldo"] += valor

    conta["extrato"].append(
        f"Depósito: + R$ {valor:.2f}"
    )

    print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")


def transferencia(conta):
    print("\n( + ========== TRANSFERÊNCIA ========== + )")

    pix_destino = verificar_vazio(
        "Chave Pix do destinatário: "
    )

    if pix_destino.lower() == conta["pix"].lower():
        print("\nVocê não pode transferir para sua própria conta!")
        return

    conta_destino = encontrar_conta("pix", pix_destino)

    if conta_destino is None:
        print("\nConta destinatária não encontrada!")
        return

    valor = verificar_valor(
        "Valor da transferência: R$ "
    )

    if valor > conta["saldo"]:
        print("\nSaldo insuficiente!")
        return

    conta["saldo"] -= valor
    conta_destino["saldo"] += valor

    conta["extrato"].append(
        f"Transferência enviada para "
        f"{conta_destino['nome']}: - R$ {valor:.2f}"
    )

    conta_destino["extrato"].append(
        f"Transferência recebida de "
        f"{conta['nome']}: + R$ {valor:.2f}"
    )

    print("\nTransferência realizada com sucesso!")

1
def menu_conta(conta):
    while True:
        print("\n( + ========== BANCO IFRN ========== + )")
        print(f"Olá, {conta['nome']}!\n")
        print("1 - Ver saldo")
        print("2 - Ver extrato")
        print("3 - Depositar")
        print("4 - Transferência")
        print("5 - Ver conta")
        print("6 - Ver chave Pix")
        print("7 - Sair da conta")

        opcao = verificar_numero("\nEscolha: ")

        match opcao:

            case 1:
                LimparTerminal()
                ver_saldo(conta)

            case 2:
                LimparTerminal()
                ver_extrato(conta)

            case 3:
                LimparTerminal()
                deposito(conta)

            case 4:
                LimparTerminal()
                transferencia(conta)

            case 5:
                LimparTerminal()
                ver_conta(conta)

            case 6:
                LimparTerminal()
                print(f"\nSua chave Pix é: {conta['pix']}")

            case 7:
                LimparTerminal()
                print("\nSaindo da conta...")
                break

            case _:
                print("\nOpção inválida!")


while True:
    print("\n( + ========== BANCO IFRN ========== + )")
    print("\n1 - Se cadastrar")
    print("2 - Entrar em uma conta")
    print("3 - Sair")

    escolha = verificar_numero("\nEscolha: ")

    match escolha:

        case 1:
            LimparTerminal()
            cadastro()
        case 2:
            LimparTerminal()
            conta_logada = login()

            if conta_logada is not None:
                menu_conta(conta_logada)

        case 3:
            LimparTerminal()
            print("\nSaindo do Banco IFRN...")
            break

        case _:
            print("\nOpção inválida!")