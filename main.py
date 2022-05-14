import ast
import random
import funcoes


with open('base_dados.txt', 'r') as arquivo:
    base_dados = arquivo.read()

dicionario = ast.literal_eval(base_dados)
dicio_norma = funcoes.normaliza(dicionario)

repost = 's'


while repost != "s":
        
        
        
        
        
        
        
        
        
        
        
        if repost != "n":
        
            repost = input('Caractere Inválido! Você deseja jogar de novo(s/n):')
        else:
            break