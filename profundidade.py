grafo = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd', 'f'],
    'f': ['e']
}

# coisos globais
valor_profundidade_entrada = 0 # contador da profundidade em que os vertices entram da pilha (chamado recursivamente)
valor_profundidade_saida = 0 # contador da profundidade em que os vertices saem da pilha (termina sua chamada recursiva)
# dicionario com as profunfidades em que cada vertice entrou e saiu da pilha numa lista [profundidade_entrada, profundidade_saida]
profundidades_entrada_saida = {}
father = {} # dicionario com os pais de cada vertice na arvore de busca em profundidade
niveis = {} # nivel de cada vertice na arvore de busca em profundidade
# o low eh o vertice mais proximo da raiz da arvore de busca em profundidade que consigo chegar descendo pelas arestas de arvore quantas vezes eu queira (incluindo 0 vezes) e subindo uma unica vez por uma aresta de retorno
low = {}

citiesArray = [
    "Rostock",
    "Berlin",
    "Dresden",
    "Leipzig",
    "Magdeburg",
    "Lübeck",
    "Braunschweig",
    "Hannover",
    "Hamburg",
    "Bremen",
    "Munster",
    "Köln",
    "Düsseldorf",
    "München", 
    "Ulm",
    "Ingolstadt",
    "Stuttgart",
    "Baden",
    "Frankfurt",
    "Nürnberg",
    "Mainz",
    "Trier",
    "Bonn",
]

citiesRoutes = {
   "Rostock": ["Berlin", "Magdeburg", "Lübeck"],
   "Berlin": ["Rostock", "Magdeburg", "Dresden"],
   "Dresden": ["Berlin", "Leipzig"],
   "Leipzig": ["Dresden", "Magdeburg", "Nürnberg"],
   "Magdeburg": ["Rostock", "Berlin", "Leipzig", "Braunschweig", "Lübeck"],
   "Lübeck": ["Rostock", "Magdeburg", "Braunschweig", "Hannover", "Hamburg"],
   "Braunschweig": ["Lübeck", "Magdeburg", "Nürnberg", "Mainz", "Düsseldorf", "Munster", "Hannover"],
   "Hannover": ["Lübeck", "Braunschweig", "Munster", "Bremen", "Hamburg"],
   "Hamburg": ["Lübeck", "Hannover", "Bremen"],
   "Bremen": ["Hamburg", "Hannover", "Munster"],
   "Munster": ["Bremen", "Hannover", "Braunschweig", "Düsseldorf", "Köln"],
   "Köln":["Düsseldorf","Bonn","Munster" ],
   "Düsseldorf":["Munster","Köln","Mainz","Braunschweig"],
   "München":["Ulm","Ingolstadt"],
   "Ulm":["Ingolstadt","München","Stuttgart"],
   "Ingolstadt":["Ulm","München","Stuttgart","Nürnberg"],
   "Stuttgart":["Frankfurt","Baden","Ulm","Ingolstadt"],
   "Baden":[ "Frankfurt","Stuttgart"],
   "Frankfurt":["Nürnberg","Mainz","Trier","Baden","Stuttgart"],
   "Nürnberg": ["Frankfurt", "Ingolstadt","Leipzig","Braunschweig","Mainz" ],
   "Mainz": ["Frankfurt","Trier","Nürnberg","Braunschweig","Düsseldorf","Köln","Bonn" ],
   "Trier": ["Bonn","Frankfurt","Mainz"],
   "Bonn":["Trier","Mainz","Köln" ],
}

def busca_em_profundidade(graph, selectedCity):
    for city in graph:
        low[city] = city

    father[selectedCity] = None
    call_to_busca_em_profundidade(graph, selectedCity, 1)

def call_to_busca_em_profundidade(grafo, vertice_do_grafo, nivel):
    global valor_profundidade_entrada, valor_profundidade_saida
    valor_profundidade_entrada += 1 # atualizando o contador de profundidade de entrada
    profundidades_entrada_saida[vertice_do_grafo] = [valor_profundidade_entrada, None] # anotando profundidade de entrada de vertice_do_grafo
    niveis[vertice_do_grafo] = nivel # anotando o nivel desse vertice_do_grafo na arvore de busca em profundidade

    count_filhos = 0 # contador de filhos do vertice por arestas de arvore que soh serah usado pela busca_em_profundidade (chamada da raiz) para concertar a raiz caso ela tenha sido escolhida como articulacao erroneamente

    for vizinho in grafo.get(vertice_do_grafo): # percorrendo os vizinhos de vertice_do_grafo
        # (descomente os codigos abaixo para ver a ordem em que as arestas sao visitadas e suas respectivas classificacoes)
        # print('%s -> %s:' % (str(vertice_do_grafo), str(vizinho)))
        if not profundidades_entrada_saida.get(vizinho): # testa se esse vizinho jah foi empilhado (chamado pela recursao)
            # se ainda naum foi empilhado, eh hora de...
            father[vizinho] = vertice_do_grafo # ... atualizar quem eh o pai dele na arvore de busca em profundidade
            # MOMENTO PARA VISITAR vertice_do_grafo -> vizinho COMO ARESTA DE ARVORE
            count_filhos += 1 # contando a quantidade de filhos do vertice por arestas de arvore (esse valor soh serah relevante para a raiz (primeira chamada de call_to_busca_em_profundidade feita por busca_em_profundidade))
            # aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
            # print('aresta de arvore')
            # chamada de recursao escolhendo agora esse vizinho como raiz:
            call_to_busca_em_profundidade(grafo, vizinho, nivel + 1) # o proximo vertice estarah um nivel abaixo desse na arvore de busca em profundidade
            # HORA DE TESTAR SE O MEU FILHO TEM UM LOW MELHOR QUE O MEU!
            if niveis[low[vizinho]] < niveis[low[vertice_do_grafo]]: # caso meu filho tenha um low melhor que o meu...
                low[vertice_do_grafo] = low[vizinho] # atualizo o meu low, para o low do meu filho (afinal podemos descer quantas vezes quisermos por arestas de arvore para achar o low, lembram?)
            # NESSE MOMENTO EU JAH SEI SE MEUS FILHOS SAO DEMARCADORES OU NAUM!
        else: # caso o vizinho jah esteja na pilha (jah houve uma chamada de call_to_busca_em_profundidade com parametro vertice_do_grafo=vizinho)
            # testa se esse vizinho jah foi desempilhado (terminou sua chamada de call_to_busca_em_profundidade)
            if not profundidades_entrada_saida[vizinho][1]:
                if father[vertice_do_grafo] != vizinho: # testando se o vizinho eh o pai do vertice tratado nessa chamada de call_to_busca_em_profundidade
                    # caso o vizinho naum seja o pai do vertice dessa chamada de call_to_busca_em_profundidade, eh hora de...
                    # MOMENTO PARA VISITAR vertice_do_grafo -> vizinho COMO ARESTA DE RETORNO
                    # aresta[(vertice_do_grafo, vizinho)] = 'aresta de retorno'
                    # print('aresta de retorno')
                    # por se tratar de uma aresta de retorno, pode ser que meu vizinho esteja mais proximo da raiz que o meu low...
                    if niveis[vizinho] < niveis[low[vertice_do_grafo]]:
                        low[vertice_do_grafo] = vizinho # ... nesse caso, atualizo meu low

    valor_profundidade_saida += 1 # atualizando o contador de profundidade de saida
    profundidades_entrada_saida[vertice_do_grafo][1] = valor_profundidade_saida

print("Selecione uma cidade de partida \n")

i = 0

while i < len(citiesArray):
    nextItem = str(i+1)
    print(nextItem + " - " + citiesArray[i])
    i+=1

print()
selectedCityId = int(input())
selectedCityId-=1

selectedCity = citiesArray[selectedCityId]

count_filhos = busca_em_profundidade(citiesRoutes, selectedCity)

print(niveis)
