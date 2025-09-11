# Solicita os dados ao usuário e armazena nas variáveis corretas
pop_A = float(input("Qual o valor para população A? "))
taxa_A = float(input("Qual a taxa de crescimento para A ? ")) / 100

pop_B = float(input("Qual o valor para população B? "))
taxa_B = float(input("Qual a taxa de crescimento para B ? ")) / 100

# Contador de anos
anos = 0

# Loop até que a população de A ultrapasse ou iguale a de B
while pop_A < pop_B:
    pop_A += pop_A * taxa_A
    pop_B += pop_B * taxa_B
    anos += 1

# Resultado
print(f"A cidade A ultrapassará ou igualará a cidade B em {anos} anos.")

