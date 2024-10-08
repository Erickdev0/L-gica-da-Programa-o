# FUNCIONAMENTO DO FOR

# Exemplo Prático: Iterando de 0 a 4
for i in range(5):
    print(i)

# Iterando sobre cada letra de "Infinity"
for letra in "Infinity":
    print(letra)

# A função range() gera uma sequência de números, frequentemente usada em loops for para iteração eficiente.

# ATIVIDADE PRÁTICA

# Atividade 01: Tabuada de um Número
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Atividade 02: Soma de Números de 1 a 100
soma = 0
for i in range(1, 101):
    soma += i
print(f"A soma de 1 a 100 é: {soma}")

# ATIVIDADE PRÁTICA

# Atividade 03: Caractere por Caractere
palavra = input("Digite uma palavra: ")
for caractere in palavra:
    print(caractere)

# Atividade 04: Contagem Regressiva de 10 a 1
for i in range(10, 0, -1):
    print(i)
print("Feliz Ano Novo!")

# FOR + CONDICIONAIS

# Exemplo: Imprimindo Números Pares de 1 a 10
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} é par")

# Contagem de Vogais em uma String
texto = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contagem = 0
for letra in texto:
    if letra in vogais:
        contagem += 1
print(f"O texto contém {contagem} vogais.")

# ATIVIDADE PRÁTICA

# Atividade 05: Contagem de Números Positivos e Negativos
positivos = 0
negativos = 0
for _ in range(10):
    numero = int(input("Digite um número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

# Atividade 06: Soma de Números Pares
soma_pares = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma_pares += i
print(f"A soma dos números pares de 1 a 50 é: {soma_pares}")

# ATIVIDADE PRÁTICA

# Atividade 07: Contagem de Vogais em uma Palavra
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contagem_vogais = 0
for letra in palavra:
    if letra in vogais:
        contagem_vogais += 1
print(f"A palavra '{palavra}' contém {contagem_vogais} vogais.")

# Atividade 08: Cálculo de Média de Notas
soma_notas = 0
for _ in range(5):
    nota = float(input("Digite a nota do aluno: "))
    soma_notas += nota
media = soma_notas / 5
if media >= 6:
    print(f"Média: {media:.2f} - Aprovado")
else:
    print(f"Média: {media:.2f} - Reprovado")

# ATIVIDADE PRÁTICA

# Atividade 09: Verificar Números Pares e Ímpares com Interrupção
for i in range(1, 21):
    if i == 15:
        break
    elif i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")

# Atividade 10: Contar Números Positivos e Negativos com Interrupção
positivos = 0
negativos = 0
for _ in range(10):
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

# ATIVIDADE PRÁTICA

# Atividade 11: Verificar Múltiplos de 5 e Parar
for i in range(1, 31):
    if i > 20:
        break
    if i % 5 == 0:
        print(f"{i} é múltiplo de 5")

# Atividade 11 (Parte 2): Cálculo Total com Desconto e Interrupção
total = 0
for _ in range(5):
    preco = float(input("Digite o preço do produto: "))
    total += preco
    if total > 100:
        total *= 0.9  # Aplica desconto de 10%
        print(f"Desconto aplicado! Total com desconto: R$ {total:.2f}")
        break
print(f"Total final: R$ {total:.2f}")
