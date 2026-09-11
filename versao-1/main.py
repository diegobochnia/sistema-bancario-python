contas = {}
proximo_numero = 1001


def buscar_conta(numero):
    return contas.get(numero)


def criar_conta():
    global proximo_numero

    print("\n--- CRIAR CONTA ---")

    titular = input("Nome do titular: ").strip()

    if titular == "":
        print("O nome do titular não pode ficar vazio.")
        return

    conta = {
        "numero": proximo_numero,
        "titular": titular,
        "saldo": 0.0,
        "transacoes": []
    }

    contas[proximo_numero] = conta

    print("\nConta criada com sucesso!")
    print(f"Número da conta: {proximo_numero}")

    proximo_numero += 1


def listar_contas():
    print("\n--- CONTAS CADASTRADAS ---")

    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas.values():
        print("---------------------------")
        print(f"Conta: {conta['numero']}")
        print(f"Titular: {conta['titular']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")


def consultar_conta():
    print("\n--- CONSULTAR CONTA ---")

    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Digite um número válido.")
        return

    conta = buscar_conta(numero)

    if conta is None:
        print("Conta não encontrada.")
        return

    print(f"\nConta: {conta['numero']}")
    print(f"Titular: {conta['titular']}")
    print(f"Saldo: R$ {conta['saldo']:.2f}")


def editar_conta():
    print("\n--- EDITAR CONTA ---")

    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Digite um número válido.")
        return

    conta = buscar_conta(numero)

    if conta is None:
        print("Conta não encontrada.")
        return

    print(f"Titular atual: {conta['titular']}")

    novo_titular = input("Novo titular: ").strip()

    if novo_titular == "":
        print("O nome não pode ficar vazio.")
        return

    conta["titular"] = novo_titular

    print("Conta atualizada com sucesso!")


def excluir_conta():
    print("\n--- EXCLUIR CONTA ---")

    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Digite um número válido.")
        return

    conta = buscar_conta(numero)

    if conta is None:
        print("Conta não encontrada.")
        return

    if conta["saldo"] != 0:
        print("Não é possível excluir uma conta com saldo.")
        return

    del contas[numero]

    print("Conta excluída com sucesso!")


def depositar():
    print("\n--- DEPÓSITO ---")

    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Número inválido.")
        return

    conta = buscar_conta(numero)

    if conta is None:
        print("Conta não encontrada.")
        return

    try:
        valor = float(input("Valor do depósito: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("O valor deve ser maior que zero.")
        return

    conta["saldo"] += valor

    conta["transacoes"].append(
        f"Depósito: + R$ {valor:.2f}"
    )

    print("Depósito realizado com sucesso!")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")


def sacar():
    print("\n--- SAQUE ---")

    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Número inválido.")
        return

    conta = buscar_conta(numero)

    if conta is None:
        print("Conta não encontrada.")
        return

    try:
        valor = float(input("Valor do saque: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("O valor deve ser maior que zero.")
        return

    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return

    conta["saldo"] -= valor

    conta["transacoes"].append(
        f"Saque: - R$ {valor:.2f}"
    )

    print("Saque realizado com sucesso!")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")


def transferir():
    print("\n--- TRANSFERÊNCIA ---")

    try:
        origem = int(input("Conta de origem: "))
        destino = int(input("Conta de destino: "))
    except ValueError:
        print("Número de conta inválido.")
        return

    conta_origem = buscar_conta(origem)
    conta_destino = buscar_conta(destino)

    if conta_origem is None:
        print("Conta de origem não encontrada.")
        return

    if conta_destino is None:
        print("Conta de destino não encontrada.")
        return

    if origem == destino:
        print("Não é possível transferir para a mesma conta.")
        return

    try:
        valor = float(input("Valor da transferência: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("O valor deve ser maior que zero.")
        return

    if valor > conta_origem["saldo"]:
        print("Saldo insuficiente.")
        return

    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor

    conta_origem["transacoes"].append(
        f"Transferência enviada para conta {destino}: - R$ {valor:.2f}"
    )

    conta_destino["transacoes"].append(
        f"Transferência recebida da conta {origem}: + R$ {valor:.2f}"
    )

    print("Transferência realizada com sucesso!")


def extrato():
    print("\n--- EXTRATO ---")

    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Número inválido.")
        return

    conta = buscar_conta(numero)

    if conta is None:
        print("Conta não encontrada.")
        return

    print(f"\nTitular: {conta['titular']}")
    print(f"Conta: {conta['numero']}")
    print("---------------------------")

    if len(conta["transacoes"]) == 0:
        print("Nenhuma movimentação realizada.")
    else:
        for transacao in conta["transacoes"]:
            print(transacao)

    print("---------------------------")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")


def menu():
    while True:

        print("\n==========================")
        print("         BANCO PY")
        print("==========================")
        print("1 - Criar conta")
        print("2 - Listar contas")
        print("3 - Consultar conta")
        print("4 - Editar conta")
        print("5 - Excluir conta")
        print("6 - Depositar")
        print("7 - Sacar")
        print("8 - Transferir")
        print("9 - Extrato")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            criar_conta()

        elif opcao == "2":
            listar_contas()

        elif opcao == "3":
            consultar_conta()

        elif opcao == "4":
            editar_conta()

        elif opcao == "5":
            excluir_conta()

        elif opcao == "6":
            depositar()

        elif opcao == "7":
            sacar()

        elif opcao == "8":
            transferir()

        elif opcao == "9":
            extrato()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("Opção inválida.")


menu()