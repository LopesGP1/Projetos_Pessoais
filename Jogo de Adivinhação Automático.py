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
x = int (input("Digite o número que você escolheu "))




def busca_binaria (vetor,inici,fim,x):
   
    while inici<= fim:
        m = int ((inici+fim) // 2 )#indice do meio do vetor
        if x > vetor[m]:
            return busca_binaria (vetor,m+1,fim,x)
        elif x < vetor [m]:
            return busca_binaria (vetor,inici,m-1,x)
        else:
            print(m)

vetor =list (range(0,101)) 
posicao = busca_binaria(vetor,0,len(vetor)-1,x) 


# Exibir o resultado
if posicao <= 0:
    print (posicao)

#contador = 0
#  while contador != "" :
        
#     contador = (contador+1)