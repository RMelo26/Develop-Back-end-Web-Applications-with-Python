nome = "Maria"
mes = "abril"
salario = 10500.50

# print("O salário de Maria no mês de abril foi R$ 10500.50")
texto_resultado = "O salário de {0} no mês de {1} foi R$ {2:.2f}".format(nome, mes, salario)
print()
print("O salário de {0} no mês de {1} foi R$ {2:.2f}".format(nome, mes, salario))
print(texto_resultado)

# imprimir cada caracter da string
# for caracter in texto_resultado:
#     print(caracter)

# imprimir tamanho da string
tamanho_string = len(texto_resultado)
print("A string tem {0} caracter(es)".format(tamanho_string))

# conversao/descoberta de tipos
a = "10"
print(a)
b = int(a)
c = float("200.89")
print(b + c)
print(type(a))
print(type(b))
print(type(c))
