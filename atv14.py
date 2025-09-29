numero=int(input("digite o numero:"))
if numero<=1:
    print("Não é um número primo.")
else:
    eprimo=True
    for i in range(2,numero):
        if numero%i==0:
            eprimo=False
            break
    if eprimo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
