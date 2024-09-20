import time


def le_problema(arquivo_entrada: str):
    with open(arquivo_entrada, 'r') as arquivo:
        qtd_variaveis = int(arquivo.readline().strip())
        entrada = []
        
        for linha in arquivo:
            clausula = [int(coluna) for coluna in linha.strip().split()]
            entrada.append(clausula)

    return qtd_variaveis, entrada

def solucao_inicial(qtd_variaveis: int):
    return [None] * qtd_variaveis

def verificar_solucao(problema, solucao):
    # Verificando se é completa
    for variavel in solucao:
        if variavel is None:
            return False

    for clausula in problema:
        satisfeita = False
        # Toda clausula terá sempre três literais
        for variavel, valor_atual in zip(clausula, solucao):
            if variavel == 1:
                satisfeita = satisfeita or valor_atual
            elif variavel == 0:
                satisfeita = satisfeita or not valor_atual

        # Se uma clausula não foi satisfeita, não é necessário seguir
        # as disjunções se tornarão falsas
        if not satisfeita:
            return False
    return True


# A cláusula é computável quando todos os literais após o i sõ valores diferentes de -1
# pois até o i-ésimo eles já foram preenchidos
def clausula_computavel(i, clausula):
    tamanho_clausula = len(clausula)
    
    for j in range(i, tamanho_clausula):
        if clausula[j-1] == -1:
            return False
    

def construir_candidatos(solucao, i, problema, dominio):
    # Não é possível fazer mais testes, pois s já possui todos os valores preenchidos
    if i > len(solucao): return []
       
    candidatos = dominio.copy()
    s_temp = solucao.copy()
    
    # Testando cada valor do domínio
    for c in dominio:
        s_temp[i-1] = c

        # Verifica se todas as clausulas possíveis podem ser satisfeitas com o valor candidato atual
        # Se uma cláusula for falsa, já cancela o candidato atual        
        for clausula in problema:
            satisfeita = False  

            # Verificamos se os itens após o i-ésimo não são -1, porque, se forem, nao podemos verificar a clausula ainda
            if clausula_computavel(i, clausula):
                for variavel_atual, literal in enumerate(clausula):
                    if literal == 1:
                        satisfeita = satisfeita or s_temp[variavel_atual]
                    elif literal == 0:
                        satisfeita = satisfeita or not s_temp[variavel_atual]
            else:
                continue

            # Se não satisfez a cláusula atual, não poderá satisfazer as próximas, então o ramo deste candidato pode ser removido
            if not satisfeita:
                candidatos.pop(0)
                break
    return candidatos


global finished
def backtrack(solucao, i, problema):
    dominio = [False, True]
    global finished

    #print("Solucao parcial:", solucao)
    if verificar_solucao(problema, solucao):
        finished = True
    else:
        i = i + 1
        candidatos = construir_candidatos(solucao, i, problema, dominio)
        for c in candidatos:
            solucao[i-1] = c
            backtrack(solucao, i, problema)
            if finished:
                return 
            solucao[i-1] = None


def SAT(caminho_problema):
    global finished
    finished = False
    inicio = time.time()
    qtd_variaveis, problema = le_problema(caminho_problema)
    solucao = solucao_inicial(qtd_variaveis)
    backtrack(solucao, 0, problema)
    fim = time.time()
    if finished:
        print("Solução encontrada:", solucao)
    else:
        print("Solução não encontrada")
    
    tempo_execucao = fim - inicio
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")


if __name__ == "__main__":
    for i in range(10):
        print(f"Problema {i+1}")
        SAT(f"SAT/entrada{i+1}.txt")
        print("\n")
