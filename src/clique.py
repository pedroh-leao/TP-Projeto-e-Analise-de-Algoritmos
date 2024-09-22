# Problema de Clique usando Branch and Bound
# Clique – Dado um grafo, encontre um conjunto maximo de vertices tal que todas as possiveis arestas entre eles estejam presentes.
import time

def leProblema(caminho_entrada):
    entrada = []

    with open(caminho_entrada, 'r') as arquivo:
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

def eCompleta(solucao):
    return not -1 in solucao

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
    if eCompleta(solucao):
        melhor[:] = solucao
        return melhor
    
    else:
        for j in range(2):
            solucao[i] = j
            
            if(eConsistente(solucao, problema, i) and ePromissora(solucao, problema, melhor, i)):
                melhor = branchAndBoundClique(solucao, i+1, problema, melhor)
            
            solucao[i] = -1
        
        return melhor

def Clique(caminho_entrada):
    inicio = time.time()
    problema = leProblema(caminho_entrada) # primeira linha = numero de vertices, demais linhas = matriz de adjacencia
    melhorSolucao = geraSolucao(problema)
    solucaoInicial = [-1] * problema[0][0]
    
    melhorSolucao = branchAndBoundClique(solucaoInicial, 0, problema, melhorSolucao)
    fim = time.time()

    print(melhorSolucao)

    print("Vértices presentes no clique:")
    for i in range(len(melhorSolucao)):
        if(melhorSolucao[i] == 1):
            print(i+1)

    print(f"Tempo de execução: {fim-inicio:.6f} segundos")

if __name__ == "__main__":
    for i in range(3):
        print(f"Problema: {i+1}")
        Clique(f"entradas/Clique/entradaClique{i+1}.txt")
        print("\n")