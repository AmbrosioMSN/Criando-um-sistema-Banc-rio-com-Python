# Dados Bancarios
menu_de_operacoes = """
        ---------------    MENU    ---------------        

                       [1] Depositar
                       [2] Sacar
                       [3] Extrato
                       [4] Criar Conta
                       [5] Criar Conta Corrente
                       [0] Sair

        >>>>>>>>>>>>> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
clientes = []
contas_corrente = []

AGENCIA = '0001'
LIMITE_SAQUES = 3

def criar_conta_cliente(lista_de_usuarios):
    cpf = input('Digite o CPF (Somente Número): ')
    usuarios_filtrados = filtra_usuarios(cpf, lista_de_usuarios)

    if usuarios_filtrados:
         print('Esse CPF já tem cadastro no sistema!')
         return
    nome = input('Digite o nome completo: ')
    data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Digite o endereço (logradouro, nro - bairro - cidade/sigla estado) : ')

    lista_de_usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Cliente Criado Com Sucesso!!')

def criar_conta(agencia, numero_conta, lista_de_clientes):
    cpf = input('Digite o CPF (Somente Número): ')
    usuarios_filtrados = filtra_usuarios(cpf, lista_de_clientes)

    if usuarios_filtrados:
         print('Conta criada com Sucesso!')
         return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuarios_filtrados}
    
    print('Usuário não encontrado, fluxo de criação de conta encerrado!')

def operacao_deposito(saldo, valor, extrato,/):
        # valor_deposito = float(input("Digite o valor de Deposito: "))
        if valor_deposito > 0:
            saldo += valor
            extrato += f"Depósito: {valor_deposito:.2f}\n"
            print("Valor Depósitado com Sucesso!!")
        else:
            print()
            print("O valor de deposito é inferior a 0 e não pode ser depositado!")
        return saldo, extrato

def operacao_saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
        if numero_saques != limite_saques:
        #    valor_saque = float(input("Digite o valor de Saque: "))
           if valor <= limite:
               if saldo < valor:
                   print()
                   print("Saldo insuficiente para a operação!")
               else:
                   extrato += f"Saque: {valor:.2f}\n"
                   numero_saques += 1
                   saldo -= valor
                   print(f"Saque de R${valor}")
                   print("Faça a retirada do valor na boca do Caixa")
                   print()
           else:
               print()
               print("Valor digitado maior que o limite de saque permitido!")
        else:
            print()
            print("Limite de saque diario atingindo!!")
        
        return saldo, extrato, numero_saques
        
def operacao_extrato(saldo,/,*,extrato):
        extrato += f"Saldo Atual = R${saldo:.2f}\n"
        print()
        print("*********** Extrato Bancário ***********")
        print(extrato)

def filtra_usuarios(cpf, lista_de_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_de_usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

while True:
    opcao_de_operacoes = input(menu_de_operacoes)

# Operação de Deposito
    if opcao_de_operacoes == "1":
        print()
        valor_deposito = float(input("Digite o valor de Deposito: "))
        saldo, extrato = operacao_deposito(saldo,valor_deposito,extrato)
    
# Operação de Saque
    elif opcao_de_operacoes == "2":
        print()
        print("*********** Lembrando que o limite de saque é R$500.00 ***********")
        valor_saque = float(input("Digite o valor de Saque: "))
        saldo, extrato, numero_saques = operacao_saque(
            saldo=saldo,
            valor=valor_saque,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

# Operação de Extrato
    elif opcao_de_operacoes == "3":
        operacao_extrato(saldo, extrato=extrato)
    
# Operação de Criar Cliente
    elif opcao_de_operacoes == "4":
         criar_conta_cliente(clientes)

# Operação de Criar Conta Corrente
    elif opcao_de_operacoes == "5":
         numero_conta = len(contas_corrente) + 1
         conta = criar_conta(AGENCIA, numero_conta, clientes)

         if conta: 
              conta.append(conta)

    elif opcao_de_operacoes == "0":
        print()
        print("Obrigado por utilizar nosso sistema, volte sempre!")
        break
    else:
        print()
        print("Operação inválida, por favor selecione novamente a operação desejada.")











