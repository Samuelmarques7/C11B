
import numpy as np

musicas = []

while True:
    nome = input("Nome da música: ")
    ano = int(input("Ano de lançamento: "))
    musicas.append({"nome": nome, "ano": ano})

    continuar = input("Deseja cadastrar outra música? (s/n): ").strip().lower()
    if continuar != "s":
        break

print(f"\nForam cadastradas {len(musicas)} música(s).")

ano_mais_antigo = min(musica["ano"] for musica in musicas)
mais_antigas = [m for m in musicas if m["ano"] == ano_mais_antigo]

print(f"\nMúsica(s) do ano mais antigo ({ano_mais_antigo}):")
for m in mais_antigas:
    print(f"- {m['nome']} ({m['ano']})")