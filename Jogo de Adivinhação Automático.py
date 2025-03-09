import os 
import time 

time.sleep(0.5)
print ("===== Jogo de Adivinhação Automático ===== ")
time.sleep(0.5)
print ("Explicação do jogo : ")
time.sleep(0.5)
print ("A única regra e que voce tem que escolher um numero 1 entre 100!!!") 
time.sleep(0.5)
print ("O próprio sistema vai estar adivinhando qual número você chutou.")
time.sleep(0.5)
print ("LEMBREÇE NÃO PODE ALTERAR O NUMERO DEPOIS QUE O SISTEMA COMEÇOU A ADIVINHAR !!!")
time.sleep(1.5)

comecar = input ("Pronto para começar ? s/n ")
print ("escolha um número de 1 a 100 :  ")



# maior
# menor
#acertou


def busca_binaria (vetor,inici,fim):  
   

    def busca_maior():
        return busca_binaria (vetor,m+1,fim)
    def busca_menor():
        return busca_binaria (vetor,inici,m-1)
    def acerto():
        print(f"Encontrei! O número é {vetor[respt_user]}")
        return respt_user 
        
    
    
    m = int ((inici+fim) // 2 )#indice do meio do vetor
    respt_user = input (f"Meu palpite e esse {m}") 
    if   respt_user == "maior":
        busca_maior()   
    elif respt_user== "menor":
        busca_menor() 
    elif respt_user== "acertou":
        acerto()
        
         


vetor =list (range(0,101)) 
posicao = busca_binaria(vetor,0,len(vetor)-1) 


# Exibir o resultado


#contador = 0  print (tentativas)tentativas = tentativas+1
#  while contador != "" :
        
#     contador = (contador+1)