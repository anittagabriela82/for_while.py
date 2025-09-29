numero = int(input("Digite o número da tabuada: "))
inicio = int(input("digite o inicio da tabuada: "))
final = int(input("digite o final: "))
for i in range (inicio,final +1):
    resultado = numero*i
    print(f"{numero} x {i} = {resultado}")
