# Atividade 1
saudacao = "Hello World"
print(saudacao)


# Atividade 2
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))

print(f"Nome: {nome} (Tipo: {type(nome)})")
print(f"Idade: {idade} (Tipo: {type(idade)})")
print(f"Altura: {altura} (Tipo: {type(altura)})")

# Atividade de Cálculo da Média de Notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Sua média é: {media}")


# Atividade de Cálculo de Salário por Hora
salario_mensal = float(input("Digite seu salário mensal: "))
horas_por_semana = float(input("Digite o número de horas trabalhadas por semana: "))


# Multiplicando por 4 para obter o total de horas trabalhadas no mês
horas_por_mes = horas_por_semana * 4
salario_por_hora = salario_mensal / horas_por_mes

print(f"Você trabalha {horas_por_mes} horas por mês.")
print(f"Seu salário por hora é: R$ {salario_por_hora:.2f}")


# Atividade com f-string
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade_natal = input("Digite sua cidade natal: ")

mensagem = f"Olá, {nome}! Você tem {idade} anos e é de {cidade_natal}."
print(mensagem)
