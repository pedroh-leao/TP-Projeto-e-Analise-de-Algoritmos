# Problema do conjunto independente deve ser resolvido por meio de redução com custo polinimial ao problema do Clique, já implementado usando branch and bound.


def leProblema():
    entrada = []

    with open('entradaClique3.txt', 'r') as arquivo:
        for linha in arquivo:
            colunas = linha.split(' ')
            
            for i, _ in enumerate(colunas):
                colunas[i] = int(colunas[i])

            entrada.append(colunas) 

    return entrada

def geraSolucao(numVertices):
    solucao = [1] + [0] * (numVertices - 1)
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
    numVertices = problema[0][0]
    complemento = [[numVertices]]
    for i in range(1 , numVertices + 1):
        linha = []
        for j in range(numVertices):
            if i -1 == j:
                linha.append(0)
            else: 
                linha.append(1 - problema[i][j])
            complemento.append(linha)
    return complemento

if __name__ == "__main__":

    problema = leProblema() 
    complemento = geraComplemento()

    melhorSolucao = geraSolucao(problema[0][0])
    solucaoInicial = [-1] * problema[0][0]
    
    melhorSolucao = branchAndBoundClique(solucaoInicial, 0, complemento, melhorSolucao)

    print(melhorSolucao)

    print("Vértices presentes no clique:")
    for i in range(len(melhorSolucao)):
        if(melhorSolucao[i] == 1):
            print(i+1)