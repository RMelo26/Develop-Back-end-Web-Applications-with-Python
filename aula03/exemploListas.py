listaNomes = []
listaFamilias = []

qtdNomes = 2
qtdFamilias = 2

for f in range(qtdFamilias):
    for n in range(qtdNomes):
        nome = input(f"Informe o {n+1}o. nome da {f+1}a. Família: ")
        listaNomes.append(nome)
  
    listaFamilias.append( listaNomes )
    listaNomes = []

x = 0 
for nomes in listaFamilias:  
    x += 1
    print(f'Nomes da Família {x}: {nomes}')
    print()
  
listaFamilias.sort()
print(f"Famílias e nomes informados: {listaFamilias}")