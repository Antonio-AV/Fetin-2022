import numpy as np
import pandas as pd

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
    tabela = pd.read_excel("Teste Fetin.xlsx")
    nCriterios = tabela.shape[0]
    nAlternativas = tabela.shape[1] - 2
    notasAlternativas = []
    notasCriterios = []
    retSkSemSoma = []
    notasSkRk = []
    criterios = []
    retSk = []
    retRk = []
    retQk = []
    v = 0.5

    nomes = tabela["Critérios"]
    pesos = tabela["Pesos"]

    #Separando as notas por alternativa
    for i in range(nAlternativas):
        notasAlternativas.append(tabela.iloc[:, i+2])

    #Separando as notas por critério
    for i in range(nCriterios):
        crit = []
        for j in range(nAlternativas):
            crit.append(notasAlternativas[j][i])
        notasCriterios.append(crit)

#Preenchendo o  array de critérios
    for i in range(nCriterios):
        nome = nomes[i]
        peso = pesos[i]
        valores = notasCriterios[i]
        criterio_aux = Criterio(nome, peso, valores)
        criterios.append(criterio_aux)

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


#Pegando o nome de cada uma das opções
    cabecalho = tabela.head(0).columns
    opcoes = []
    for i in range(2, tabela.shape[1]):
        opcoes.append(cabecalho[i])
    opcoes = np.array(opcoes)

#Criando o dataframe final
    array = []
    for i in range(opcoes.size):
        array.append(opcoes[i])
        array.append(retQk[i])

    array = np.array(array).reshape(nAlternativas,2)
    df = pd.DataFrame(array, columns=['Opções', 'Qk'])
    df.to_excel('resultados.xlsx', index=False)










