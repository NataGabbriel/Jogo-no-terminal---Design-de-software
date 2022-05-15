
import ast
import random
import funcoes


with open('base_dados.txt', 'r') as arquivo:
    base_dados = arquivo.read()

dicionario = ast.literal_eval(base_dados)
dicio_norma = funcoes.normaliza(dicionario)

repost = 's'

while repost == 's':
    pais_sorteado = funcoes.sorteia_pais(dicio_norma)
    info_pais_sorteado = dicio_norma[pais_sorteado]

    

    n_tent = 20

    #Variáveis importantes para o desenvolvimento da dica
    dica1 = ("Cor da Bandeira  - custa 4 tentativas")       # daqui (natã)
    dica2 = ("Letra da capital - custa 6 tentativas")
    dica3 = ("População        - custa 5 tentativas")
    dica4 = ("Continente       - custa 9 tentativas")
    dica5 = ("Área             - custa 6 tentativas")
    l_dica = [dica1, dica2, dica3, dica4, dica5]
    preco_dica = [4, 6, 5, 9, 6]                             # até aqui (natã)
    dicas_validas = ["0","1","2","3","4","5"]
    lista_paises = []
    lista_dicas = []
    lista_l_sorteada = []
    l_cores_sorteadas = []
    lista_distancias = []
    

    #Variáveis importantes para o desenvolvimento das distâncias
    distancias = []
    paises_palpites = []

    print("=================================================")
    print("          Bem vindo ao Jogo dos países         ")
    print("        Desafio: Acertar o país sorteado       ")
    print("=================================================")
    print("Comandos:")
    print(" dicas - entre no mercado de dicas")
    print(" desisto - desiste dessa rodada")
    print(" inventario - exibe a posição")
    print("Um país foi sorteado, ADIVINHE!")
    while n_tent > 0:
        print("Você tem {} tentativas!".format(n_tent))
        palpite = (str(input("Qual o palpite? "))).lower()
                
        
        
        if palpite == pais_sorteado:
            if n_tent == 20:
                print("Parabéns!!! Você acertou de primeira!!!")
                n_tent = 0
            else:
                print("Parabéns! Você acertou depois de {} tentativas".format(20 - n_tent))
                n_tent = 0


        
        
        if palpite not in dicio_norma.keys() and palpite != "dicas" or palpite == "inventario" or funcoes.esta_na_lista(palpite, lista_paises) == True:
        
            if palpite in lista_paises:
                print("Esse país já foi escolhido. Tente outro!")
            elif palpite == "inventario":
                
                print("")
                print ("Distâncias: ")
                
                for dist in distancias:
                
                    if dist[1] < 1000:
                        operador2 = (('\033[32m'+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))
                    
                        print(operador2)    
                        
                    elif dist[1] < 5000 and dist[1] > 1000:
                        operador2 = (("\033[31m"+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))
                        print(operador2)     

                    elif dist[1] > 5000 and dist[1] < 10000:
                        operador2 = (('\033[35m'+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))      
                        print(operador2)
                    
                    elif dist[1] > 10000:
                        operador2 = (('\033[30m'+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))
                        print(operador2)

                print("Dicas: ")    
                for di in lista_dicas:
                    print(di)
                print("")

            elif palpite == "desisto":
                n_tent = n_tent - n_tent

            else:
                print("Pais desconhecido!")

        

        while palpite == "dicas" or palpite == 'dica': # daqui (natã)
            
            if n_tent - min(preco_dica) < 1:
                print("Você não tem saldo o suficiente!")
                break
            
            palpite = "nondicas"
            print("----------------------------------------")
            print("             Mercado de dicas:          ")
            print("----------------------------------------")
            cont = 0
            opcoes_dicas = ("0")
            while cont < len(preco_dica):
                

                if n_tent - preco_dica[cont] >= 1:
                    print("{}. {}".format(cont+1, l_dica[cont]))
                    opcoes_dicas = opcoes_dicas + ("| ") + str(cont+1)
                
                    
                
                
                
                cont += 1
            print("0. Sem dica         - cafézinho gratis ;)")
            escolha_dica = input("Escolha sua opção [{}]: ".format(opcoes_dicas))
            
            while escolha_dica not in dicas_validas:
                print("Caractere Inválido!")
                escolha_dica = input("Escolha sua opção [{}]: ".format(opcoes_dicas))

            
            indice = int(escolha_dica)-1
            

            
            
            if escolha_dica == "0":
                
                break
                
            
            elif l_dica[indice] == dica1:
                
                info_band = info_pais_sorteado["bandeira"]
                c = []
                for x in info_band.keys():
                    c.append(x)
                
                selec = "outras"
                while selec == "outras" or info_pais_sorteado["bandeira"][selec] == 0 or funcoes.esta_na_lista(selec, l_cores_sorteadas) == True:
                    selec = random.choice(c)
                
                d1 = (f"Cor da bandeira: {selec}")
                print(d1)
                lista_dicas.append(d1)
                l_cores_sorteadas = []

                n_tent = n_tent - 4
                
            
            
            
            elif l_dica[indice] == dica2:
                
                info_cap = info_pais_sorteado["capital"]
                

                letra_sorteada = funcoes.sorteia_letra(info_cap, lista_l_sorteada)
                

                d2 = (f"Letra da capital do país: {letra_sorteada}")
                print(d2)
                lista_dicas.append(d2)
                lista_l_sorteada.append(letra_sorteada)
                
                n_tent = n_tent - 6    # até aqui (natã)
            



            elif l_dica[indice] == dica3:       # João amanhã
                pop = info_pais_sorteado["populacao"] 
                
                d3 = (f" A população do país sorteado é de {pop} habitantes!")
                print(d3)
                lista_dicas.append(d3)
                
                n_tent = n_tent - 5
            



            elif l_dica[indice] == dica4:
                
                d4 = ("O continente do país sorteado é : {}".format(info_pais_sorteado["continente"]))
                print(d4)
                lista_dicas.append(d4)
                
                
                n_tent = n_tent - 9


            elif l_dica[indice] == dica5:
                
                d5 = (f'A área do país sorteado é de {info_pais_sorteado["area"]} km quadrados!')
                print(d5)
                lista_dicas.append(d5)
                
                n_tent = n_tent - 6      
                
            

            if palpite != "dicas":
                
                
                if l_dica[indice] != dica1 and l_dica[indice] != dica2:
                    del dicas_validas[-1]
                
                if l_dica[indice] != dica1 and l_dica[indice] != dica2:    
                    del preco_dica[indice]

                if l_dica[indice] != dica1 and l_dica[indice] != dica2:
                    del l_dica[indice]
                

            # até aqui
            
        if palpite != pais_sorteado and palpite  in dicio_norma.keys() and funcoes.esta_na_lista(palpite, distancias) == False and palpite != 'inventario':
            raio = 6371
            
            lati_sorteado = dicio_norma[pais_sorteado]['geo']['latitude']
            
            
            longi_sorteado = dicio_norma[pais_sorteado]['geo']['longitude']
            
            
            lati_palpite = dicio_norma[palpite]['geo']['latitude']
            

            longi_palpite = dicio_norma[palpite]['geo']['longitude']
            

            distancia_haversine = funcoes.haversine(raio, lati_sorteado, longi_sorteado, lati_palpite, longi_palpite)
            
            
            
            
            distancias = funcoes.adiciona_em_ordem(palpite, distancia_haversine, distancias) 

            
            print("")
            print("")
            print("Ainda não...veja a distância desse país para o país sorteado!")
            print("")
            print ("Distâncias: ")
            n_tent = n_tent - 1
            for dist in distancias:
                
                if dist[1] < 1000:
                    operador2 = (('\033[32m'+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))
                
                    print(operador2)    
                    
                elif dist[1] < 5000 and dist[1] > 1000:
                    operador2 = (("\033[31m"+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))
                    print(operador2)     

                elif dist[1] > 5000 and dist[1] < 10000:
                    operador2 = (('\033[35m'+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))      
                    print(operador2)
                
                elif dist[1] > 10000:
                    operador2 = (('\033[30m'+f"{dist[1] : .0f}km ------> {dist[0]}"+"\033[0;0m"))
                    print(operador2)
                                

        if n_tent == 0 and palpite != pais_sorteado :
            print("Você perdeu!")
            print(f'O país sorteado era:{pais_sorteado}')
    repost = input('Você deseja jogar de novo(s/n):')
    
    while repost != "s":
        if repost != "n":
        
            repost = input('Caractere Inválido! Você deseja jogar de novo(s/n):')
        else:
            break

        
        
        
