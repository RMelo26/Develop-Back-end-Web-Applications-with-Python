# Leitura dos quatro números inteiros
numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(4)]

# Filtrar e exibir os números divisíveis por 2 e 3
divisiveis = [numero for numero in numeros if numero % 2 == 0 and numero % 3 == 0]

# Exibir os resultados
if divisiveis:
    print("Números divisíveis por 2 e 3:", divisiveis)
else:
    print("Nenhum número é divisível por 2 e 3.")
