colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}},
    {"color": "yellow", "type": "primary","code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}},
    {"color": "blue", "type": "primary","code": {"rgba": [0,0,255,1],"hex": "#00F"}}
]

cores_primarias = [c["color"] for c in colors if c["type"] == "primary"]
print("Cores primárias:", cores_primarias)

hex_azul_maximo = [c["code"]["hex"] for c in colors if c["code"]["rgba"][2] == 255]
print("Hex com azul máximo:", hex_azul_maximo)

valores = []
for c in colors:
    valores.append(c["color"])
    valores.append(c["code"]["hex"])
array_1d = np.array(valores)
print("\nArray 1D:", array_1d)

array_2d_cores = array_1d.reshape(-1, 2)
print("\nArray 2D:")
print(array_2d_cores)


traducao = {"black": "preto", "green": "verde", "yellow": "amarelo", "blue": "azul"}

array_2d_cores = array_2d_cores.astype('<U10')

for linha in array_2d_cores:
    linha[0] = traducao[linha[0]]

print("\nArray 2D com nomes em português:")
print(array_2d_cores)