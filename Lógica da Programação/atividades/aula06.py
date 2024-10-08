# Conversão de Metros para Centímetros
metros = float(input("Digite o valor em metros: "))
centimetros = metros * 100
print(f"{metros} metros é igual a {centimetros} centímetros.")

# Cálculo de Área de um Retângulo
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = largura * altura
print(f"A área do retângulo é: {area} unidades quadradas.")

# Cálculo de IMC
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

# Cálculo de Juros Simples
capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa de juros (em %): ")) / 100
tempo = float(input("Digite o tempo de aplicação (em anos): "))
montante = capital * (1 + taxa * tempo)
print(f"O valor futuro do investimento é: R$ {montante:.2f}")

# Algoritmo de Cálculo de Média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

# Algoritmo de Cálculo de Desconto
preco_original = float(input("Digite o preço original do produto: "))
desconto = float(input("Digite o percentual de desconto: ")) / 100
preco_com_desconto = preco_original * (1 - desconto)
print(f"O preço com desconto é: R$ {preco_com_desconto:.2f}")

# Algoritmo de Conversão de Tempo
segundos = int(input("Digite a quantidade de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
seg_restantes = segundos % 60
print(f"{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {seg_restantes} segundos.")

# Algoritmo de Conversão de Temperatura
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

# Categoria de Idade
idade = int(input("Digite sua idade: "))
if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade < 18:
    print("Você é um adolescente.")
elif 18 <= idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

# Classificação de Notas
nota = float(input("Digite uma nota de 0 a 100: "))
if nota >= 90:
    print("Conceito A")
elif nota >= 80:
    print("Conceito B")
elif nota >= 70:
    print("Conceito C")
elif nota >= 60:
    print("Conceito D")
else:
    print("Conceito F")

# Verificação de Signo
dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento (número): "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Áries"
# Adicione outros signos aqui conforme necessário...
else:
    signo = "Outro Signo"

print(f"Seu signo é {signo}")

# Sistema de Login
usuario_cadastrado = "admin"
senha_cadastrada = "1234"

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")
