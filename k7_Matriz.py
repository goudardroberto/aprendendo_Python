"""
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("- "*30)
for l in range(0, 3):
    for c in range(0, 3):
        # Podemos manipular quando for valores assimétricos centralizando com :^
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
"""

# Aprimorando o exercício anterior, mostrando:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("- "*30)
for l in range(0, 3):
    for c in range(0, 3):
        # Podemos manipular quando for valores assimétricos centralizando com :^
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print("- "*30)
print(f"A soma dos valores pares é {spar}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scol}.")
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"O maior valor da segunda linha é {mai}.")
