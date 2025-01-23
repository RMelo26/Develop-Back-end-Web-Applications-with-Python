nome = ''
nportugues = 0
nmatematica = 0
nconhecgerais = 0
continua = True

dicCandidatos = {} # {'nomeCanditado':[NP, NM, NCG]}
dicMedias = {} # {'nomeCadidato': media}
listaAprovados = []
listaNotas = []

# entrada de dados 
while continua:
    nome = input('Informe o nome do candidato: ')
    nportugues = float(input(f'Informe a nota de Português do candido {nome}: '))
    nmatematica = float(input(f'Informe a nota de Matemática do candido {nome}: '))
    nconhecgerais = float(input(f'Informe a nota de Conhecimentos Gerais do candido {nome}: '))
    
    listaNotas.append(nportugues)
    listaNotas.append(nmatematica)
    listaNotas.append(nconhecgerais)

    dicCandidatos[nome] = listaNotas
   
    pergunta_respondida = 'OK'
    while pergunta_respondida == 'OK':
      
        resposta = input("\nDeseja cadastrar novo candidato (S)IM ou (N)ÃO): ")
        if resposta.upper() == 'S' or resposta.upper() == 'N':
            if resposta.upper() == 'N':
                continua = False
            pergunta_respondida = 'NOK' # break
        
        else:
            print("\nInforme na pergunta 'S' para 'SIM' ou 'N' para 'NÃO'.")
        
    listaNotas = []
    
# processamento
# calcular medias
# chave : valor
# 'maria' : [10, 5.5, 9]
chaves = dicCandidatos.keys()
for chave in chaves:
    notas_aluno = dicCandidatos.get(chave)
    media = sum(notas_aluno) / len(notas_aluno)
    dicMedias[chave] = media

print(dicMedias)

# recuperar aprovados e candidatos com media > 4.5 e nota de cg > 6
qtdCandidatosMediaMaior45 = 0
for chave in chaves:
    # aprovado
    # pega as notas do candidato
    aprovado = False
    notas_aluno = dicCandidatos.get(chave)

    # verifica se tem alguma das notas menor que 2
    if notas_aluno[0] >= 2 and notas_aluno[1] >= 2 and notas_aluno[2] >= 2:
        aprovado = True
    
    # verifica se ele foi aprovado
    if dicMedias.get(chave) > 4 and aprovado == True:
        listaAprovados.append(chave)

    # candidatos com media > 4.5 e nota de cg > 6
    if dicMedias.get(chave) > 4.5 and notas_aluno[2] > 6:
        qtdCandidatosMediaMaior45 = qtdCandidatosMediaMaior45 + 1
        
# media prova portugues
somaNotas = 0
for chave in chaves:
    notas_aluno = dicCandidatos.get(chave)
    somaNotas = somaNotas + notas_aluno[0] 

media = somaNotas / len(chaves)

# qtd candidatos aprovados com nota de matematica > 5
qtdCandidatosAprovadosMatematicaMaior5 = 0
for chave in chaves:
    notas_aluno = dicCandidatos.get(chave)
    if notas_aluno[1] > 5:
        qtdCandidatosAprovadosMatematicaMaior5 = qtdCandidatosAprovadosMatematicaMaior5 + 1

print()
for chave in chaves:        
    notas_aluno = dicCandidatos.get(chave)
    print(chave, ' => Português: ', notas_aluno[0], ' / Matemática: ', notas_aluno[1], ' / Conhec Gerais: ', notas_aluno[2])        
    print() 
    
print("Médicas dos candidatos: ", dicMedias)
print("Aprovados", listaAprovados)
print("A média da prova de Português foi {0:.2f}".format(media))        
print(f"Qtd Candidatos com média > 4.5 e nota Conhec Gerais > 6:  {qtdCandidatosMediaMaior45}")    
print(f"Qtd Candidatos aprovados com nota de Matemática > 5: {qtdCandidatosAprovadosMatematicaMaior5}")
    
    
    
