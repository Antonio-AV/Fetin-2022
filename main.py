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


    #resultados = np.array(resultados)

    for result in resultados:
        print(result)




if __name__ == "__main__":
    nCriterios = int(input("Digite quantos criterios serão usados:"))
    nAlternativas = int(input("Digite o número de alternativas:"))
    contAlt = 0
    contCrit =0

    criterios = []


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

    for c in criterios:
        skSemSoma(c.valores, c.peso)





