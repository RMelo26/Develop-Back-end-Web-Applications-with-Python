
dicCandidatos = {} # {'nomeCanditado':[NP, NM, NCG]}
dicMedias = {} # {'nomeCadidato': media}
listaAprovados = []


# funcao para informar os candidatos
# retorna um dicionario de candidatos
# chave : valor
# 'maria' : [10, 5.5, 9]
def popular_candidatos():
    nome = ''
    nportugues = 0
    nmatematica = 0
    nconhecgerais = 0
    continua = True
    listaNotas = []
    dicCand = {}

    while continua:
        nome = input('Informe o nome do candidato: ')
        nportugues = float(input(f'Informe a nota de Português do candido {nome}: '))
        nmatematica = float(input(f'Informe a nota de Matemática do candido {nome}: '))
        nconhecgerais = float(input(f'Informe a nota de Conhecimentos Gerais do candido {nome}: '))
        
        listaNotas.append(nportugues)
        listaNotas.append(nmatematica)
        listaNotas.append(nconhecgerais)

        dicCand[nome] = listaNotas
    
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
    
    return dicCand

# calcular medias dos alunos
def calcular_medias(dicCandidatosLidos):
    dicMedias = {}
    chaves = dicCandidatosLidos.keys()
    for chave in chaves:
        notas_aluno = dicCandidatosLidos.get(chave)
        media = sum(notas_aluno) / len(notas_aluno)
        dicMedias[chave] = media
        
    return dicMedias


# recuperar aprovados 
def recuperar_aprovados(dicCandidatos):
    listaAprovados = {}
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

    return listaAprovados

# calcular a quantidade de candidatos com media > 4.5 e nota de cg > 6
def calcular_qtd_candidatos_media_maior_45(dicCandidatos, dicMedias):
    qtdCandidatosMediaMaior45 = 0
    chaves = dicCandidatos.keys()
    for chave in chaves:
        notas_aluno = dicCandidatos.get(chave)

        # candidatos com media > 4.5 e nota de cg > 6
        if dicMedias.get(chave) > 4.5 and notas_aluno[2] > 6:
            qtdCandidatosMediaMaior45 = qtdCandidatosMediaMaior45 + 1

    return qtdCandidatosMediaMaior45

# calcular media prova portugues
def calcular_media_prova_portugues(dicCandidatos):
    somaNotas = 0
    for chave in chaves:
        notas_aluno = dicCandidatos.get(chave)
        somaNotas = somaNotas + notas_aluno[0] 

    media = somaNotas / len(chaves)
    return media

# calcular a qtd candidatos aprovados com nota de matematica > 5
def calcular_qtd_cantidados_aprovados_nota_matematica_maior_5(dicCandidatos):
    qtdCandidatosAprovadosMatematicaMaior5 = 0
    for chave in chaves:
        notas_aluno = dicCandidatos.get(chave)
        if notas_aluno[1] > 5:
            qtdCandidatosAprovadosMatematicaMaior5 = qtdCandidatosAprovadosMatematicaMaior5 + 1
    
    return qtdCandidatosAprovadosMatematicaMaior5  

def exibir_resultados(dicCandidatos, dicMedias, listaAprovados, mediaProvaPortugues, qtdCandidatosMediaMaior45, qtdCandidatosAprovadosMatematicaMaior5):
    print()
    chaves = dicCandidatos.keys()
    for chave in chaves:        
        notas_aluno = dicCandidatos.get(chave)
        print(chave, ' => Português: ', notas_aluno[0], ' / Matemática: ', notas_aluno[1], ' / Conhec Gerais: ', notas_aluno[2])        

    print("Médias dos candidatos: ", dicMedias)
    print("Aprovados:", listaAprovados)
    print("A média da prova de Português foi {0:.2f}".format(mediaProvaPortugues)) 
    print(f"Qtd Candidatos com média > 4.5 e nota Conhec Gerais > 6:  {qtdCandidatosMediaMaior45}")    
    print(f"Qtd Candidatos aprovados com nota de Matemática > 5: {qtdCandidatosAprovadosMatematicaMaior5}") 
    
    return None

#######################

# programa principal

# entrada de dados 
dicCandidatos = popular_candidatos(dicCandidatos)

# calcular medias
dicMedias = calcular_medias(dicCandidatos)

# recuperar aprovados
listaAprovados = recuperar_aprovados(dicCandidatos)

# calcular a quantidade de candidatos com media > 4.5 e nota de cg > 6
qtdCandidatosMediaMaior45 = calcular_qtd_candidatos_media_maior_45(dicCandidatos, dicMedias)

# calcular media prova portugues
mediaProvaPortugues = calcular_media_prova_portugues(dicCandidatos)

# calcular qtd aprovados matematica > 5
qtdCandidatosAprovadosMatematicaMaior5 = calcular_qtd_cantidados_aprovados_nota_matematica_maior_5(dicCandidatos)

# exibir resultados
exibir_resultados(dicCandidatos, dicMedias, listaAprovados, mediaProvaPortugues, qtdCandidatosMediaMaior45, qtdCandidatosAprovadosMatematicaMaior5)

