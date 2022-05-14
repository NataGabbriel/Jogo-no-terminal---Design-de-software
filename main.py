import ast
import random
import funcoes


with open('base_dados.txt', 'r') as arquivo:
    base_dados = arquivo.read()

dicionario = ast.literal_eval(base_dados)
dicio_norma = funcoes.normaliza(dicionario)

repost = 's'


while repost != "s":
        
    pais_sorteado = funcoes.sorteia_pais(dicio_norma)
    info_pais_sorteado = dicio_norma[pais_sorteado]
   
        
    print("=================================================")
    print("          Bem vindo ao Jogo dos países         ")
    print("        Desafio: Acertar o país sorteado       ")
    print("=================================================")
    print("Comandos:")
    print(" dicas - entre no mercado de dicas")
    print(" desisto - desiste dessa rodada")
    print(" inventario - exibe a posição")
    print("Um país foi sorteado, ADIVINHE!")    
        
        
        
        
        
    repost = input('Você deseja jogar de novo(s/n):')    
    while repost != "s":    
        if repost != "n":
            
            repost = input('Caractere Inválido! Você deseja jogar de novo(s/n):')
        else:
            break