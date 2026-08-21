# 7. Usando a lista de ingredientes já preenchida para a receita de bolo,  agora
# crie mais dois conjuntos representando os ingredientes que duas pessoas
# diferentes têm em casa. Mostre quais ingredientes da receita ainda faltam
# comprar pelas pessoas para se fazer o bolo.

ingredientes = ['Chocolate','Leite','Manteiga','Açucar']

ingredientes.append('Farinha')

ingredientes.insert(0, 'Ovos')

pessoa1 = {'Farinha', 'Manteiga', 'Leite'}

pessoa2 = {'Ovos'}


#transforma a lista em um conjunto
receita = set(ingredientes)

total = pessoa1 | pessoa2

faltante = receita - total
print("Ingredientes faltando para a receita")
print(receita)

print(faltante)