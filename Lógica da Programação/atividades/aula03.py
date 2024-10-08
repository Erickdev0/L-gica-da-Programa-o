# Atividade 01: Contagem de 1 a 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1


# Atividade 02: Soma de Números de 1 a 100
soma = 0
contador = 1
while contador <= 100:
    soma += contador
    contador += 1
print(f"A soma dos números de 1 a 100 é: {soma}")


# Atividade 03: Tabuada de um Número
numero = int(input("Digite um número para ver a tabuada: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1


# Atividade 04: Contagem Regressiva
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("Feliz Ano Novo!")


# Atividade 05: Contagem de Números Ímpares até o Número Inserido
numero = int(input("Digite um número: "))
contador = 1
while contador <= numero:
    if contador % 2 != 0:
        print(contador)
    contador += 1


# Atividade 06: Soma de Números Positivos
soma = 0
numero = float(input("Digite um número (digite um número negativo para parar): "))
while numero >= 0:
    soma += numero
    numero = float(input("Digite um número (digite um número negativo para parar): "))
print(f"A soma dos números positivos é: {soma}")


# Atividade 07: Tabuada com Condicional
numero = int(input("Digite um número para ver a tabuada: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    if resultado % 3 == 0:
        print(f"{numero} x {contador} = {resultado}")
    contador += 1


# Atividade 08: Média de Notas
soma = 0
contador = 0
nota = float(input("Digite a nota do aluno (digite -1 para parar): "))
while nota != -1:
    soma += nota
    contador += 1
    nota = float(input("Digite a nota do aluno (digite -1 para parar): "))

if contador > 0:
    media = soma / contador
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
