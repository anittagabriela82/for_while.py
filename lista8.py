produto = 1  # Começa com 1 para multiplicar
soma = 0     # Para somar os números

for i in range(1, 7):
    numero = float(input(f"Digite o {i}º número: "))
    produto *= numero
    soma += numero

media = soma / 6

print(f"O produto dos números digitados é: {produto}")
print(f"A média aritmética dos números é: {media}")
