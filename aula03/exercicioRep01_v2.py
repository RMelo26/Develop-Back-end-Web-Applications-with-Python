numeros = []
positivos = []
negativos = []

# receber os numeros
for x in range(4):
    numero = int(input("Informe o {0}o. número: ".format(x+1)))
    numeros.append(numero)

# avaliar os numeros positivos e negativos
if (numeros >= 0):
    positivos.append([n for n in numeros if n >= 0])
    negativos.append([n for n in numeros if n < 0])
    
# imprimir resultado
if len(positivos) >= 0:
    soma_positivos = sum(positivos)
    print("Os números positivos são {0} e sua soma é igual a {1}".format(positivos, soma_positivos))
else: 
    print("Nenhum número positivo foi informado")

if len(negativos) >= 0:
    qtd_negativos = len(negativos)
    print("Os número negativos são {0} e sua quantidade é igual a {1}".format(negativos, qtd_negativos))
else: 
    print("Nenhum número negativos foi informado")
    
    