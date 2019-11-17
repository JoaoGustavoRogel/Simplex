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

print("Digite a função objetivo (forma padrão), siga o exemplo: Z +5A -7B +C = 0")
func_objetivo = input()

print("Digite a quantidade de restrições: ")
qtd_rest = int(input())
print("\nExemplo de restrição +A -3B +0C +X1 +0X2 = 0")
print("Obs.: Todas equações devem ter a mesma quantidade de variáveis, as variáveis devem aparecer na mesma ordem")
restricoes = []
for i in range(qtd_rest):
    print("Digite a " + str(i+1) + "º restrição: ")
    aux = input()
    restricoes.append(aux.split(' '))

print("\nDigite a quantidade de variáveis bases: ")
qtd_vb = int(input())
var_base = []
for i in range(qtd_vb):
    print("Digite a " + str(i+1) + "º variável base: ")
    aux = input()
    var_base.append(aux)

primeira_linha = []
primeira_linha.append("VB")
for i in func_objetivo.split(' '):
    if i == 'Z':
        continue
    elif i == '=':
        break
    else:    
        if len(i) == 3:
            primeira_linha.append(i[2])
        else:
            primeira_linha.append(i[1])

for i in var_base:
    if i == 'Z':
        continue
    primeira_linha.append(i)
primeira_linha.append("LD")

aux = []
for i in func_objetivo.split(' '):
    if i == 'Z':
        aux.append('Z')
        continue
    elif i == '=':
        break
    else:
        num = i[0]
        cont = 1
        while((i[cont] >= '0' and i[cont] <= '9') or i[cont] == '.'):
            num += i[cont]
            cont += 1
        aux.append(num)
for i in var_base:
    if i == 'Z':
        continue
    aux.append(0)
aux.append(func_objetivo[-1])

aux_quadro = []
aux_quadro.append(primeira_linha)
aux_quadro.append(aux)

cont = 1
for i in restricoes:
    linha = []
    linha.append(var_base[cont])
    flag = False
    for j in i:
        if flag:
            linha.append(j)
            break
        if j == '=':
            flag = True
            continue
        else:
            if len(j) == 2:
                linha.append('1')
            else:
                count = 1
                num = ""
                if j[0] == '-':
                    num += '-'
                while((j[count] >= '0' and j[count] <= '9') or j[count] == '.'):
                    num += j[count]
                    count += 1
                if num == "":
                    num = "1"

                linha.append(num)    
    cont += 1
    aux_quadro.append(linha)

quadro = np.matrix(aux_quadro)
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