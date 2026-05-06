idade = int(input("Digite sua idade: "))

if idade < 0:
    print("idade inválida")
elif idade <= 12:
    print("é uma criança")
elif idade <= 17:
    print("é um adolescente")
elif idade <= 59:
    print("é um adulto")
else:
    print("é um idoso")