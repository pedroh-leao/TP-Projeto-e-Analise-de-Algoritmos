# Problema do conjunto independente deve ser resolvido por meio de redução com custo polinimial ao problema do Clique, já implementado usando branch and bound.

import time

def leProblema():
    entrada = []

    with open('entrada3.txt', 'r') as arquivo:
        for linha in arquivo:
            colunas = linha.split(' ')
            
            for i, _ in enumerate(colunas):
                colunas[i] = int(colunas[i])

            entrada.append(colunas) 

    return entrada

def geraSolucao(problema):
    solucao = [0] * problema[0][0]

    for i in range(problema[0][0]):
        for j in range(problema[0][0]):
            if(problema[i+1][j] == 1):
                solucao[i] = 1
                solucao[j] = 1
                return solucao

    solucao[0] = 1
    return solucao

def eCompleta(solucao, problema):
    for i in range(problema[0][0]):
        if solucao[i] == -1:
            return False
        
    return True

def eConsistente(solucao, problema, i):
    verticesNaSolucao = []
    
    for j in range(i+1):
        if solucao[j] == 1:
            verticesNaSolucao.append(j)

    for j in range(len(verticesNaSolucao)-1):
        for k in range(j+1, len(verticesNaSolucao)):
            if(problema[verticesNaSolucao[j]+1][verticesNaSolucao[k]] == 0):
                return False
            
    return True 
            
def ePromissora(solucao, problema, melhor, i):
    numVerticesMelhor = sum(melhor)
    numVerticesMaximoSolucao = 0 # armazena o numero maximo de vertices possiveis nessa solucao
    
    for j in range(i+1):
        numVerticesMaximoSolucao += solucao[j]

    numVerticesMaximoSolucao += (problema[0][0] - (i+1))
    
    return numVerticesMaximoSolucao > numVerticesMelhor

def branchAndBoundClique(solucao, i, problema, melhor):
    if eCompleta(solucao, problema):
        melhor[:] = solucao
        return melhor
    
    else:
        for j in range(2):
            solucao[i] = j
            
            if(eConsistente(solucao, problema, i) and ePromissora(solucao, problema, melhor, i)):
                melhor = branchAndBoundClique(solucao, i+1, problema, melhor)
            
            solucao[i] = -1
        
        return melhor

def geraComplemento(problema):
    numVertices = problema[0][0]  # Número de vértices (primeira linha da matriz)
    
    # Inicializa a matriz de complemento
    complemento = [[0] * numVertices for _ in range(numVertices)]
    
    # Preenche a matriz de complemento
    for i in range(numVertices):
        for j in range(numVertices):
            if i != j:  # Não considerar a diagonal principal
                complemento[i][j] = 1 - problema[i + 1][j]
    
    # Adiciona o número de vértices como a primeira linha da matriz de complemento
    complemento.insert(0, [numVertices])
    
    return complemento

def print_grafo(matriz):
    num_vertices = matriz[0][0]  # Número de vértices (primeira linha da matriz)
    
    print(f"Número de vértices: {num_vertices}")
    
    for i in range(1, num_vertices + 1):
        linha = ' '.join(str(valor) for valor in matriz[i])
        print(linha)

def print_conjunto_independente_maximo(solucao):
    indices = [i + 1 for i in range(len(solucao)) if solucao[i] == 1]
    print("\nConjunto independente máximo:", end=" ")
    print("{", end="")
    print(", ".join(map(str, indices)), end="")
    print("}")

if __name__ == "__main__":

    inicio = time.time()
    problema = leProblema() 
    complemento = geraComplemento(problema)
    print_grafo(complemento)

    melhorSolucao = geraSolucao(complemento)
    solucaoInicial = [-1] * complemento[0][0]
    
    melhorSolucao = branchAndBoundClique(solucaoInicial, 0, complemento, melhorSolucao)
    fim = time.time()

    print_conjunto_independente_maximo(melhorSolucao)
    print(f"Tempo de execução: {fim-inicio:.6f} segundos")