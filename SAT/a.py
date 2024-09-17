# Exemplo de uma fórmula CNF: [[1, -2, 3], [-1, 2], [2, -3]]
# A fórmula representa (x1 ∨ ¬x2 ∨ x3) ∧ (¬x1 ∨ x2) ∧ (x2 ∨ ¬x3)

def leProblema():
    # A fórmula booleana em CNF: cada sublista é uma cláusula
    return [[1, 1, 1], [1, 0, -1], [2, -3]]

def eConsistente(p, s):
    """Verifica se uma solução parcial satisfaz todas as cláusulas até o momento"""
    for clause in p:
        satisfeita = False
        for literal in clause:
            var = abs(literal)
            if var <= len(s) and s[var-1] is not None:
                # Verifica se o literal é satisfeito
                if literal > 0 and s[var-1] == True:
                    satisfeita = True
                elif literal < 0 and s[var-1] == False:
                    satisfeita = True
        # Se alguma cláusula não está satisfeita, a solução é inconsistente
        if not satisfeita:
            return False
    return True

def eCompleta(p, s, i):
    """Verifica se todas as variáveis foram atribuídas"""
    return i > len(s)

def objetivo(p, s):
    """Verifica se a solução satisfaz a fórmula completa"""
    for clause in p:
        satisfeita = False
        for literal in clause:
            var = abs(literal)
            if (literal > 0 and s[var-1] == True) or (literal < 0 and s[var-1] == False):
                satisfeita = True
        if not satisfeita:
            return False
    return True


def BTOtimizacao(s, i, p):
    global melhor
    if eCompleta(p, s, i) and eConsistente(p, s):
        if objetivo(p, s):
            melhor = s.copy()
    else:
        for valor in [True, False]:
            s[i-1] = valor
            if eConsistente(p, s):
                BTOtimizacao(s, i+1, p)
            s[i-1] = None

# Função principal para resolver a fórmula booleana em CNF
def resolverCNF(p):
    global melhor
    melhor = None
    inicial = [None] * len(p[0])  # Assumindo que o número de variáveis é igual ao número de literais na primeira cláusula
    BTOtimizacao(inicial, 1, p)
    if melhor:
        return melhor
    else:
        return "Não existe solução que satisfaça a fórmula."

# Exemplo de uso
p = leProblema()
solucao = resolverCNF(p)
print("Solução encontrada:", solucao)
