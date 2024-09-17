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


finished = False
def backtrack(s, i, p):
    if i >= len(s): return

    global finished
    if is_a_solution(p, s):
        finished = True
    else:
        for j in [False, True]:
            s[i] = j
            backtrack(s, i + 1, p)
            if finished:
                return

qtd_variaveis, p = le_problema("SAT/entrada1.txt")
s = [None] * qtd_variaveis
backtrack(s, 0, p)
print(finished, s)
