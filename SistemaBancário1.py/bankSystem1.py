saldo = 0
limite = 500
op = 0
count = 0
extrato = []
while op!=4:
    print("""
                Menu
          ===================
            1 - Depositar
            2 - Sacar
            3 - Extrato
            4 - Sair
          ===================
           
""")
    op = int(input("Escolha uma opção de 1 a 4: "))
    if op == 1:
        deposito = float(input("Insira o valor do depósito: "))
        if deposito<1:
            print("Valor de depósito inválido!")
        else:
            saldo+=deposito
            print(f"Depósito feito com sucesso! Saldo atual: {saldo}")
            extrato.append(f"Deposito: R${deposito:.2f}")
    elif op == 2:
        saque = float(input("Insira o valor do saque: "))
        if saque>500 or saque<0:
            print("Valor de saque inferior a 0 ou superior a 500")
        elif count>3:
            print("Limite de 3 saques diários atingido, tente novamente em um outro dia!")
        elif saque>saldo:
            print("Valor de saque superior ao saldo!")
        else:
            saldo-=saque
            print(f"Saque feito com sucesso! Saldo atual: {saldo}")
            extrato.append(f"Saque: R${saque:.2f}")
            count+=1
    elif op == 3:
        for i in extrato:
            print(i)
        print(f"Saldo atual: R${saldo:.2f}")
    if op not in [1,2,3,4]:
        print("Opção inválida")