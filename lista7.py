# Inicializa uma variável para armazenar o menor número
menor = None

# Lê 7 números do usuário
for i in range(1, 8):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    
    if menor is None or numero < menor:
        menor = numero

# Mostra o menor número
print(f"O menor número digitado foi: {menor}")
