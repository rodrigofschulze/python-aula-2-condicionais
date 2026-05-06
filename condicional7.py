salario = float(input("digite um salário"))
desconto10 = salario - (salario / 10)
desconto5 = salario - (salario / 5)

if salario > 5000:
    print(f"seu salário é {desconto10}")
elif salario < 5000:
    print(f"seu salário é {desconto5}")
else:
    print(f"{salario} não haverá desconto")