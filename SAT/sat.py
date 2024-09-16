# Satisfabilidade – Dada uma formula booleana na forma normal conjuntiva, encontre uma
# atribuição de valores-verdade às variáveis da fórmula que a torne verdadeira, ou informe
# que não existe tal atribuição.

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


p = le_problema(le_problema("SAT/entrada1.txt"))

"""
p = LeProblema()
melhor = geraSolucaoInicial(p)

inicial = []

def BTOtimizacao(Solucao s, int i, Problema p)
    if (eCompleta(p,s,i) and (eConsistente(p,s,i)):
        if(objetivo(p,s) > objetivo(p,melhor)):
            melhor = s;
    else
        j = primeiroValor(p,i);
        while (j <= ultimoValor(p,i))
            s[i] = j;
            if (eConsistente(p,s)):
                BTOtimizacao(s,i+1,p)
            s[i] = livre
            j += 1

BTOtimizacao(inicial,1,p)
"""