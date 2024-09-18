def le_problema(arquivo_entrada: str):
    qtd_variaveis = None
    entrada = []

    with open(arquivo_entrada, 'r') as arquivo:
        linhas_do_arquivo = arquivo.readlines()
        
        qtd_variaveis = int(linhas_do_arquivo[0])
        
        for linha in linhas_do_arquivo[1:]:
            linha = linha.replace('\n', '')
            colunas = linha.split(' ')
            entrada.append([])
            for coluna in colunas:
                entrada[-1].append(int(coluna))

    return  qtd_variaveis, entrada

def is_a_solution(p, s):
    # Verificando se é completa
    for variavel in s:
        if variavel is None:
            return False

    for clausula in p:
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

def construct_candidates(s, i, p, dominio):
    # Não é possível fazer mais testes, pois s já possui todos os valores preenchidos
    # Vira uma busca exaustiva quando não existe uma solução
    if i > len(s): return []
       
    candidatos = []
    s_temp = s.copy()
    
    for c in dominio:
        satisfeita = False
    
        # Verifica todas as clausulas e testa se, até o i atual, elas são satisfeitas
        # Verifica somente as variáveis que já foram atribuidas
        s_temp[i-1] = c
        for clausula in p:
            for j in range(i):
                if clausula[j] == 1:
                    satisfeita = satisfeita or s_temp[j]
                elif clausula[j] == 0:
                    satisfeita = satisfeita or not s_temp[j]

        if satisfeita:
            candidatos.append(c)    
    
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

for i in range(9):
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
