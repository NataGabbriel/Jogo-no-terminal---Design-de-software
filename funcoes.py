from random import choice
import math


def normaliza(dicio):
    dicio_saida = {}
    for i, k in dicio.items():
        for j, l in k.items():
            pais = j
            dicio_saida[pais] = l
            dicio_saida[pais]['continente'] = i
    return dicio_saida




def sorteia_pais(dicio_paises):
    lista_paises = []
    for i in dicio_paises.keys():
        lista_paises.append(i)
    pais = choice(lista_paises)
    return pais





def haversine(r, la1 , lo1, la2, lo2):
    la1 = math.radians(la1)
    lo1 = math.radians(lo1)
    la2 = math.radians(la2)
    lo2 = math.radians(lo2)
    op1 = (math.sin((la2-la1)/2))**2
    op2 = math.cos(la1)*math.cos(la2)*((math.sin((lo2-lo1)/2))**2)
    raiz = math.sqrt((op1+op2))
    d = 2 * r * math.asin(raiz) 
    return d




def adiciona_em_ordem(pais, distancia, lista):
    new_lista = []
    cont = 0
    
    if len(lista) == 0:
        return [[pais, distancia]]
        
    for x in lista:
        if x[1] < distancia:
            new_lista.append(x)
            if cont == len(lista)-1:
                new_lista.append([pais, distancia])
                
        elif x[1] > distancia:
            new_lista.append([pais, distancia])
            for x in lista[cont:]:
                new_lista.append(x)
            
            break
        cont += 1
    
    return new_lista




def esta_na_lista(nome, lista):
    for j in lista:
        if j[0] == nome:
            return True
    return False




def sorteia_letra(palavra,lista):
    lista_letras = []

    for i in palavra:
        if i not in lista:
            lista_letras.append(i)
    letra_sorteada = choice(lista_letras)
    return letra_sorteada