numeros = []
positivos = []
negativos = []
soma_positivos = 0
qtd_negativos = 0

# receber os numeros
for x in range(4):
    numero = int(input("Informe o {0}o. número: ".format(x+1)))
    numeros.append(numero)


# avaliar os numeros positivos e negativos
for numero in numeros:
    if (numero >= 0):
        positivos.append(numero)
        soma_positivos = soma_positivos + numero
    else:
        negativos.append(numero)
        qtd_negativos = qtd_negativos + 1
        
# imprimir resultado
if len(positivos) >= 0:
    print("Os números positivos são {0} e sua soma é igual a {1}".format(positivos, soma_positivos))
else: 
    print("Nenhum número positivo foi informado")

if len(negativos) >= 0:
    print("Os número negativos são {0} e sua quantidade é igual a {1}".format(negativos, qtd_negativos))
else: 
    print("Nenhum número negativos foi informado")
    
    