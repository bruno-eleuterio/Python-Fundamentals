nome = "Bruno"
idade = 32
profissao = "Administrador"
linguagem = "Python"
saldo = 45.435
dados = {"nome": "Bruno", "idade":32}

print("Nome: %s Idade: %d" % (nome,idade)) #oldstyle

print("Nome: {} Idade: {}".format(nome,idade)) #.format_1
print("Nome: {1} Idade: {0}".format(idade,nome)) #.format_2
print("Nome: {1} Idade: {0} Nome: {1} {1} {1}".format(idade,nome)) #.format_2

print("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade)) #.format_3
print("Nome: {name} Idade: {age}".format(age=idade, name=nome)) #.format_3
print("Nome: {nome} Idade: {idade}".format(**dados)) #.format_4

print(f"Nome: {nome} Idade: {idade}") #f-string

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")
