salario = float(input("digite um salário"))

if salario == 5000:
    print("esse é o primeiro salário")
elif 5000 % 10:
    print(f"{salario}foi aplicado o desconto")
elif 5000 % 5:
    print(f"{salario}foi aplicado outro desconto")
else:
    print(f"{salario}não haverá desconto")