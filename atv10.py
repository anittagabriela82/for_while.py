prim1 = int(input("Digite um número inteiro: "))
seg2 = int(input("Digite outro número inteiro: "))
if prim1 > seg2:
    prim1, seg2 = seg2, prim1
pares = [n for n in range(prim1, seg2 + 1) if n % 2 == 0]
print("Números pares no intervalo:", pares)
