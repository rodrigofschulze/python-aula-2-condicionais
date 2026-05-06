usuario = "admin" 
senha = 1234

login1 = input("digite seu usuário:")
login2 = input("digite sua senha")

if login1 == usuario and login2 == senha:
    print("login feito com sucesso")
else:
    print("usuário ou senha incorretas")


