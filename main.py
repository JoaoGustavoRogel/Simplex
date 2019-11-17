import numpy as np

def verifica_solucao_otima(quadro):
    aux = np.inf
    flag = False

    for i in quadro.getA()[1]:
        if flag is True:
            aux = min(aux, float(i))
        flag = True    

    if aux < 0:
        return False
    else:    
        return True


def coluna_pivo(quadro):
    aux = np.inf
    res = 0
    cont = 0

    for i in quadro.getA()[1]:
        if cont >= 1 and float(i) < aux:
            aux = float(i)
            res = cont

        cont = cont + 1        
        flag = True    
    
    return res

def linha_pivo(quadro, col_pivo):
    flag = False
    res = 0
    cont = 0
    aux = np.inf

    for i in quadro.getA():
        if flag == True and float(i[col_pivo]) != 0:
            temp = float(i[-1]) / float(i[col_pivo])
            if temp > 0 and temp < aux:
                aux = temp
                res = cont

        flag = True
        cont = cont + 1
    
    return res

"""quadro = np.matrix([
    ['vb', 'g', 'm', 'a', 'b', 'c', 'ld'], 
    ['z', -5, -7, 0, 0, 0, 0],
    ['a', 3, 0, 1, 0, 0, 250],
    ['b', 0, 1.5, 0, 1, 0, 100],
    ['c', 0.25, 0.5, 0, 0, 1, 50]
    ])
"""

quadro = np.matrix ([
    ['VB', 'A', 'B', 'C', 'X1', 'X2', 'LD'],
    ['Z', -5, -7, -8, 0, 0, 0],
    ['X1', 1, 1, 2, 1, 0, 1190],
    ['X2', 3, 4.5, 1, 0, 1, 4000]
])

print(quadro, '\n')

while(not verifica_solucao_otima(quadro)):
    col_pivo = coluna_pivo(quadro)
    lin_pivo = linha_pivo(quadro, col_pivo)
    pivo = float(quadro.getA()[lin_pivo][col_pivo])

    linha_ref = quadro.getA()[lin_pivo]
    col = 0
    for i in linha_ref:
        if col >= 1:
            linha_ref[col] = float(linha_ref[col]) / pivo
        col += 1    

    linha = 0
    for i in quadro.getA():
        if linha == lin_pivo:
            quadro.getA()[linha] = linha_ref
        if linha >= 1 and linha != lin_pivo:
            col = 0
            coef = float(quadro.getA()[linha][col_pivo]) 
            for j in i:
                if col >= 1:
                    ref = float(linha_ref[col])
                    old = float(quadro.getA()[linha][col])
                    quadro.getA()[linha][col] = old + (-1 * coef * ref)
                col += 1
        linha += 1
       
    quadro.getA()[0][col_pivo], quadro.getA()[lin_pivo][0] = quadro.getA()[lin_pivo][0], quadro.getA()[0][col_pivo]

    print(quadro, '\n')