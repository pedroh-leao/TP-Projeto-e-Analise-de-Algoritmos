# Satisfabilidade – Dada uma formula booleana na forma normal conjuntiva, encontre uma
# atribuição de valores-verdade às variáveis da fórmula que a torne verdadeira, ou informe
# que não existe tal atribuição.

# Variáveis: X1, X2, ... Xn
# Domínio: Xi ∈ {0, 1}
# Restrição: 
# Solução: 

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


# É preciso gerar um valor, mesmo que seja aleatório
def geraSolucaoInicial(qtd_variaveis):
    return [None] * qtd_variaveis

# Verifica se a solução é completa percorrendo todos os elementos do vetor de solução
# Se possuir um None, então a solução não é completa
def eCompleta(s, i):
    for variavel in s:
        if variavel is None:
            return False
    return True    
    
# Verifica se a solução parcial satisfaz a cláusula atual
def eConsistente(p, s, i):
    # for j in range (i):
    #     if s[j] is not None:
    #         return False
    return True


# Verifica se a solução satisfaz a fórmula completa
def objetivo(p, s):
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


# s: solução que está sendo montada
# i: variavel a ser atualizada
# p: problema ser resolvido
def BTOtimizacao(s, i: int, p):
    
    if eCompleta(s, i) and objetivo(p, s):
        global melhor 
        melhor = s.copy()
        global finished
        finished = True
        print("terminou")

    else:
        for j in [False, True]:
            s[i] = j
            if (eConsistente(p, s, i)):
                BTOtimizacao(s, i+1, p)
            if finished:
                return
            s[i] = None

finished = False
qtd_variaveis, p = le_problema("SAT/entrada2.txt")
melhor = geraSolucaoInicial(qtd_variaveis)
inicial = [None] * qtd_variaveis

BTOtimizacao(inicial, 0, p)
print(finished)
print(melhor)