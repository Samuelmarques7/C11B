# 6. Crie uma lista com ingredientes de uma receita de bolo:
# a. Adicione um novo ingrediente no final;
# b. Insira outro em uma posição específica;
# c. Remova um ingrediente pelo valor

ingredientes = []

ingredientes.append(input("Digite um ingrediente: "))

print(ingredientes)


ingredientes.insert(int(input("qual posiçao deseja inserir o ingrediente: ")), input("Digite o  Ingrediente: "))

print(ingredientes)

ingredientes.remove(input("Digiete o ingrediente a ser removido: "))

print(ingredientes)