# Populações iniciais
pop_A = 90000
pop_B = 250000

# Taxas de crescimento anual
taxa_A = 0.035  # 3.5%
taxa_B = 0.012  # 1.2%

# Contador de anos
anos = 0

# Loop até que a população de A ultrapasse ou iguale a de B
while pop_A < pop_B:
    pop_A += pop_A * taxa_A
    pop_B += pop_B * taxa_B
    anos += 1

# Resultado
print(f"A cidade A ultrapassará ou igualará a cidade B em {anos} anos.")
