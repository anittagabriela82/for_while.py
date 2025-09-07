usuario = input("Digite o nome de usuário: ")
senha = input("Agora digite a senha: ")
while True:
    if senha == usuario:
        print("Obs: A senha não pode ser igual ao nome de usuário,tente novamente.")
        senha = input("Agora digite novamente a senha: ")
    else:
        break
print("Login efetuado com sucesso!")
