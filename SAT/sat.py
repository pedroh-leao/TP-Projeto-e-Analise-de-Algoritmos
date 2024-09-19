# O tamanho de uma cláusula é a soma de todos o literais diferentes de -1,
# ou seja, que estão presentes
def tamanho_clausula(clausula):
    return sum(1 for literal in clausula if literal != -1)

def le_problema(arquivo_entrada: str):
    with open(arquivo_entrada, 'r') as arquivo:
        qtd_variaveis = int(arquivo.readline().strip())
        entrada = []
        
        for linha in arquivo:
            clausula = [int(coluna) for coluna in linha.strip().split()]
            entrada.append({
                'len': tamanho_clausula(clausula),
                'literais': clausula
            })

    return qtd_variaveis, entrada

def is_a_solution(p, s):
    # Verificando se é completa
    for variavel in s:
        if variavel is None:
            return False

    for clausula in p:
        clausula = clausula['literais']
        satisfeita = False
        # Toda clausula terá sempre três literais
        for variavel, valor_atual in zip(clausula, s):
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
    

def construct_candidates(s, i, p, dominio):
    # Não é possível fazer mais testes, pois s já possui todos os valores preenchidos
    if i > len(s): return []
       
    candidatos = dominio.copy()
    s_temp = s.copy()
    
    # Testando cada valor do domínio
    for c in dominio:
        s_temp[i-1] = c

        # Verifica se todas as clausulas possíveis podem ser satisfeitas com o valor candidato atual
        # Se uma cláusula for falsa, já cancela o candidato atual        
        for cl in p:
            satisfeita = False  
            clausula = cl['literais']

            # Se foi atribuido menos valores à solução do que o tamanho da cláusula, ela ainda não pode ser verificada
            # Garantindo que a cláusula tem tamanho igual ou menor que a quantidade de itens mapeados,
            #   agora verificamos se os itens após o i-ésimo não são -1, porque, se forem, também não pode ser verificada
            if cl['len'] <= i and clausula_computavel(i, clausula):
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
def backtrack(s, i, p):
    dominio = [False, True]
    global finished

    #print("Solucao parcial:", s)
    if is_a_solution(p, s):
        finished = True
    else:
        i = i + 1
        candidates = construct_candidates(s, i, p, dominio)
        for cand in candidates:
            s[i-1] = cand
            backtrack(s, i, p)
            if finished:
                return 
            s[i-1] = None


for i in range(10):
    print(f"Iniciando problema {i+1}")
    finished = False
    qtd_variaveis, p = le_problema(f"SAT/entrada{i+1}.txt")
    s = [None] * qtd_variaveis
    backtrack(s, 0, p)

    if finished:
        print("Solução encontrada:", s)
    else:
        print("Solução não encontrada")
    print("\n")
