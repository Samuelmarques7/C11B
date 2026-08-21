# Faça um programa que leia o nome e a média de um aluno e guarde
# os em um dicionário. Em seguida, a partir da média (para ser
# aprovado deve ter média >=50), gere a situação final do aluno (‘AP’
# ou ‘RP’), que  também deve ser guardada neste dicionário. No final,
# CIÊNCIA DE DADOS COM PYTHON Prof. Renzo Paranaíba Mesquita
# mostre todo o conteúdo deste dicionário;

Ciencia_de_dados = {}

Ciencia_de_dados['Nome'] = input("Digite o seu nome: ")
Ciencia_de_dados['Média'] = int(input("Qual a sua média: "))

if Ciencia_de_dados['Média'] >= 50:
    Ciencia_de_dados ['Final'] = 'AP'
else:
    Ciencia_de_dados['Final'] = 'RP'

print(Ciencia_de_dados.values())
# dados1 = {'Nome':'Aurelio',
#           'Média':89}
# dados2 = {'Nome':'Leonarnado',
#           'Média':70}
# dados3 = {'Nome':'Godinho',
#           'Média':100}
#
# Ciencia_de_dados_com_python = [dados1,dados2,dados3]
#
# for dado in Ciencia_de_dados_com_python :
#     if dado['Média'] >= 50:
#         dado ['Final'] = 'AP'
#
#
# print(Ciencia_de_dados_com_python )
#
