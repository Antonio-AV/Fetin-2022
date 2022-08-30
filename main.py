import numpy as np

class Criterio:
    def __init__(self, nome, peso, valores):
        self.nome = nome
        self.peso = peso
        self.valores = np.array(valores)

def skSemSoma(notas, peso):
    maior = np.max(notas)
    menor = np.min(notas)
    cont = 0

    resultados = []
    for nota in range(notas.size):
        resultado = round(peso * (abs(maior-notas[cont])/abs(maior-menor)),2)
        resultados.append(resultado)
        cont += 1

    resultados = np.array(resultados)

    return resultados


def Sk(notas):
    return np.sum(notas)

def Rk(notas):
    return np.max(notas)

def Qk(v, sk, rk):
    sMais = np.min(sk)
    sMenos = np.max(sk)

    rMais = np.min(rk)
    rMenos = np.max(rk)

    qk = []

    for i in range (len(sk)):
        aux = (v*(sk[i]-sMais)/(sMenos-sMais))+((1-v)*(rk[i]-rMais)/(rMenos-rMais))
        qk.append(aux)

    qk = np.array(qk)
    return qk


if __name__ == "__main__":
    nCriterios = int(input("Digite quantos criterios serão usados:"))
    nAlternativas = int(input("Digite o número de alternativas:"))
    contAlt = 0
    contCrit =0
    retSkSemSoma = []
    notasSkRk = []
    criterios = []
    retSk = []
    retRk = []
    retQk = []
    v = 0.5


    for criterio in range(nCriterios):
        nome = input("Digite o nome do critério:")
        peso = float(input("Digite o peso do critério:"))
        alternativas = []
        for alternativa in range(nAlternativas):
            print("Digite a nota da alternativa ", contAlt+1, ":")
            valor = float(input())
            alternativas.append(valor)
            criterio_aux = Criterio(nome, peso, alternativas)
            contAlt += 1
        criterios.append(criterio_aux)
        contCrit += 1
        contAlt = 0

    criterios = np.array(criterios)


# Trabalhando com a função SkSemSoma
    for c in criterios:
        ret = skSemSoma(c.valores, c.peso)
        retSkSemSoma.append(ret)

    retSkSemSoma = np.array(retSkSemSoma)


# Trabalhando com a função Sk
    for i in range(nAlternativas):
        alt = []
        for j in range(nCriterios):
            alt.append(retSkSemSoma[j][i])
        notasSkRk.append(alt)

    notasSkRk = np.array(notasSkRk)

    for n in notasSkRk:
        ret = round(Sk(n),2)
        retSk.append(ret)

    retSk = np.array(retSk)

# Trabalhando com a função Rk
    for n in notasSkRk:
        retu = Rk(n)
        retRk.append(retu)

    retRk = np.array(retRk)

# Trabalhando com a função Qk
    notasQk = Qk(v, retSk, retRk)

    for i in notasQk:
        ret = round(i,6)
        retQk.append(ret)

    retQk = np.array(retQk)

    print(retQk)











