nome = ''
nportugues = 0
nmatematica = 0
nconhecgerais = 0
continua = True

listaNomes = []
listaPort = []
listaMat = []
listaCG = []
listaMedias = []
listaAprovados = []

# entrada de dados 
while continua:
    nome = input('Informe o nome do candidato: ')
    nportugues = float(input(f'Informe a nota de Português do candido {nome}: '))
    nmatematica = float(input(f'Informe a nota de Matemática do candido {nome}: '))
    nconhecgerais = float(input(f'Informe a nota de Conhecimentos Gerais do candido {nome}: '))
    
    listaNomes.append(nome)
    listaPort.append(nportugues)
    listaMat.append(nmatematica)
    listaCG.append(nconhecgerais)
    
    resposta = input("\nDeseja cadastrar novo candidato (S)IM ou (N)ÃO): ")
    if resposta.upper() == 'N':
        continua = False

# processamento
# calcular medias
qtdCandidatos = len(listaNomes)
for indice in range(qtdCandidatos):
    media = (listaPort[indice] + listaMat[indice] + listaCG[indice]) / 3
    listaMedias.append(media)

# recuperar aprovados e candidatos com media > 4.5 e nota de cg > 6
qtdCandidatosMediaMaior45 = 0
for indice in range(qtdCandidatos):
    # aprovado
    if listaMedias[indice] > 4 and (listaPort[indice] >= 2 and listaMat[indice] >= 2 and listaCG[indice] >= 2):
        listaAprovados.append(indice)
    
    # candidatos com media > 4.5 e nota de cg > 6
    if listaMedias[indice] > 4.5 and listaCG[indice] > 6:
        qtdCandidatosMediaMaior45 = qtdCandidatosMediaMaior45 + 1
        
# media prova portugues
somaNotas = 0
for nota in listaPort:
    somaNotas = somaNotas + nota 

media = somaNotas / len(listaPort)

# qtd candidatos aprovados com nota de matematica > 5
qtdCandidatosAprovadosMatematicaMaior5 = 0
for indice_candidato_aprovado in listaAprovados:
    if listaMat[indice_candidato_aprovado] > 5:
        qtdCandidatosAprovadosMatematicaMaior5 = qtdCandidatosAprovadosMatematicaMaior5 + 1
    
        
print(listaNomes, ' => Notas Português: ', listaPort, ' / Notas Matemática: ', listaMat, ' / Notas Conhec Gerais: ', listaCG)        
print(listaMedias)
print(listaAprovados)
print("A média da prova de Português foi {0:.2f}".format(media))        
print(f"Qtd Candidatos com média > 4.5 e nota Conhec Gerais > 6:  {qtdCandidatosMediaMaior45}")    
print(f"Qtd Candidatos aprovados com nota de Matemática > 5: {qtdCandidatosAprovadosMatematicaMaior5}")
    
    
    

