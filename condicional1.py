num1 = float(input("digite um número"))

if num1 > 0:
    print(f"{num1}é positivo")
elif num1 < 0:
    print(f"{num1}é negativo")
else:
    num1 = 0
    print(f"{num1}é zero")