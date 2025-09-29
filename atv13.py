positivos = 0
negativos = 0
zeros = 0   

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1
print("\nResultado:")
print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
print("Quantidade de zeros:", zeros)
    




