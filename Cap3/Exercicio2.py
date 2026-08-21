# Crie dois conjuntos, um para cada loja. Identifique quais modelos de
# smartphones cada uma delas vendem. Em seguida, mostre quais
# modelos no total você terá opção de comprar se visita-las e quais
# modelos se encontram disponíveis em ambas as lojas;

silvashop = {'Samsung', 'Apple'}

martstore = {'Xioami','Motorola','Sony'}

cel = silvashop | martstore

print(cel)

print("Silvashop: ",silvashop)
print("Martstore: ", martstore)