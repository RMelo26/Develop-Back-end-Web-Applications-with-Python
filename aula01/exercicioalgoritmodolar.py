# Solicitar ao usuário a quantidade de dólares no cofre
quantidade_dolares = float(input("Digite a quantidade de dólares no cofre: "))

# Solicitar a cotação do dólar do dia
cotacao_dolar = float(input("Digite a cotação do dólar do dia: "))

# Calcular o valor em reais
valor_reais = quantidade_dolares * cotacao_dolar

# Exibir o valor em reais
print(f"O valor correspondente em reais é: R$ {valor_reais:.2f}")
