# Atividade 01: Comparação de Idades
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

if idade1 > idade2:
    print("A primeira idade é maior que a segunda.")
elif idade1 < idade2:
    print("A primeira idade é menor que a segunda.")
else:
    print("As idades são iguais.")


# Atividade 02: Verificar Igualdade de Strings
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if palavra1 == palavra2:
    print("As palavras são iguais.")
else:
    print("As palavras são diferentes.")


# Atividade 03: Verificação de Maioridade e Habilitação
idade = int(input("Digite sua idade: "))
habilitacao = input("Você possui habilitação? (sim/não): ").lower()

if idade >= 18 and habilitacao == "sim":
    print("Você é maior de idade e possui habilitação.")
else:
    print("Você não atende aos requisitos para dirigir.")


# Atividade 04: Verificação de Notas Aprovadas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 >= 6 and nota2 >= 6:
    print("O aluno está aprovado.")
else:
    print("O aluno não está aprovado.")


# Atividade 05: Desconto em Preço
preco = float(input("Digite o preço do produto: "))
preco -= preco * 0.05
print(f"O preço do produto com desconto é: R$ {preco:.2f}")


# Atividade 06: Dobro do Valor
numero = float(input("Digite um número: "))
numero *= 2
print(f"O dobro do número é: {numero}")


# Atividade 07: Verificação de Caracteres em uma String
frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

if caractere in frase:
    print(f"O caractere '{caractere}' está presente na frase.")
else:
    print(f"O caractere '{caractere}' não está presente na frase.")


# Atividade 08: Verificação de Palavras em uma Frase
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

if palavra in frase:
    print(f"A palavra '{palavra}' está presente na frase.")
else:
    print(f"A palavra '{palavra}' não está presente na frase.")
