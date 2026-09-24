conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Não foi possível realizar o saque.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente.")

conta_normal = False
conta_universitaria = True
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente.")

conta_normal = False
conta_universitaria = False
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente.")
else:
    print("O sistema não reconheceu o seu tipo de conta, entre em contato com o gerente.")

conta_normal = False
conta_universitaria = False
conta_especial = False
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente.")
elif conta_especial:
    print("Conta especial selecionada!")
else:
    print("O sistema não reconheceu o seu tipo de conta, entre em contato com o gerente.")
    
