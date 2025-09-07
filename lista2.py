def ler_nome():
    while True:
        nome = input("Digite seu nome (mínimo 4 letras): ").strip()
        if len(nome) >= 4:
            return nome
        print("Nome inválido! Deve ter pelo menos 4 letras.")
def ler_idade():
    while True:
        try:
            idade = int(input("Digite sua idade (entre 1 e 100 anos): "))
            if 1 <= idade <= 100:
                return idade
            print("Idade inválida! Deve ser entre 1 e 100.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro para a idade.")
def ler_salario():
    while True:
        try:
            salario = float(input("Digite seu salário (valor positivo): "))
            if salario >= 0:
                return salario
            print("Salário inválido! Deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número para o salário.")
def ler_genero():
    while True:
        genero = input("Digite seu gênero ('f' - feminino, 'm' - masculino, 'o' - outro): ").lower()
        if genero in ['f', 'm', 'o']:
            return genero
        print("Gênero inválido! Digite 'f', 'm' ou 'o'.")
def ler_situacao_empregaticia():
    while True:
        situacao = input("Digite sua situação empregatícia ('e' - empregado, 'd' - desempregado, 'a' - autônomo): ").lower()
        if situacao in ['e', 'd', 'a']:
            return situacao
        print("Situação inválida! Digite 'e', 'd' ou 'a'.")
def main():
    nome = ler_nome()
    idade = ler_idade()
    salario = ler_salario()
    genero = ler_genero()
    situacao = ler_situacao_empregaticia()
    print("\n--- Dados do Formulário ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Gênero: {genero}")
    print(f"Situação Empregatícia: {situacao}")
if __name__ == "__main__":
    main()


