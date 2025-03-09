import os 
import time 

# maior
# menor
#acertou


# A função vai estar fazendo a busaca binária 
def busca_binaria (vetor,inici,fim,tentativas = 1):  
   
    #Criei funções internas para estar funcionando melhor caso eu for passar para um arquivo app e melhor passar as funçoes para externas para o fluxo ser melhor
    def busca_maior():
        return busca_binaria (vetor,m+1,fim,tentativas + 1)
    def busca_menor():
        return busca_binaria (vetor,inici,m-1,tentativas + 1)
    def acerto():
        time.sleep(0.5)
        print(".", end="")
        time.sleep(0.5)
        print(".", end="")
        time.sleep(0.5)
        print(".")
        time.sleep(0.9)
        print(f"Acertei em {tentativas} tentativas!")  # Exibe as tentativas
        return tentativas
        
    
    
    m = int ((inici+fim) // 2 )#indice do meio do vetor
    respt_user = input (f"Meu palpite e esse {m}: ").lower()
    
    if   respt_user == "maior":
        busca_maior()   
    elif respt_user== "menor":
        busca_menor() 
    elif respt_user== "acertou":
        acerto()
        


# O sistema vai começar aqui 

time.sleep(0.5)
print ("===== Jogo de Adivinhação Automático ===== ")
time.sleep(0.5)
print ("Explicação do jogo : ")
time.sleep(0.5)
print ("A única regra é que você tem que escolher um número entre 1 e 100!!!") 
time.sleep(0.5)
print ("O próprio sistema vai estar adivinhando qual número você escolheu.")
time.sleep(0.5)
print(f"Depois que o sistema der o palpite, digite uma destas três opções: 'maior', 'menor' ou 'acertou'")
time.sleep(0.5)
print ("LEMBRE-SE: NÃO PODE ALTERAR O NÚMERO DEPOIS QUE O SISTEMA COMEÇOU A ADIVINHAR!!!")
time.sleep(1.5)

while True:
    comecar = input("Pronto para começar? (s/n): ")
    os.system('cls')
    if comecar.lower() == 's':
        print("Escolha um número de 1 a 100 e não diga para o computador!")
        time.sleep(1)
        vetor =list (range(0,101)) 
        posicao = busca_binaria(vetor,1,len(vetor)-1) 
    else:
        print("Tudo bem, jogamos outra hora!")
        break


# Exibir o resultado


#contador = 0  print (tentativas)tentativas = tentativas+1
#  while contador != "" :
        
#     contador = (contador+1)


"""""# *Documentação - Jogo de Adivinhação Automático*  

## *Descrição do Jogo*  
Neste jogo, o computador tentará adivinhar o número que o jogador escolheu. Ele usará uma estratégia chamada *busca binária*, que permite encontrar o número rapidamente reduzindo a faixa de possibilidades a cada tentativa.  
## *Regras do Jogo*  
1. O jogador escolhe um número secreto dentro de um intervalo (ex: *1 a 100*).  
2. O computador fará um palpite no meio do intervalo.  
3. O jogador responde se o número é *maior, menor ou se acertou*.  
4. O computador ajusta seu palpite com base na resposta.  
5. O jogo continua até o computador acertar o número.  

## *Funcionamento da Lógica*  
- O computador começa chutando o valor médio do intervalo.  
- Se o palpite for *menor*, o computador ajusta o intervalo para números maiores.  
- Se for *maior*, ele ajusta o intervalo para números menores.  
- Esse processo continua até o palpite ser igual ao número escolhido.  
## *Exemplo de Fluxo do Jogo*  
1. O jogador pensa no número *68* (sem dizer ao computador).  
2. O computador chuta *50*.  
   - O jogador diz: "Maior".  
3. O computador ajusta e chuta *75*.  
   - O jogador diz: "Menor".  
4. O computador chuta *62*.  
   - O jogador diz: "Maior".  
5. O computador chuta *68*.  
   - O jogador diz: "Acertou!".  

O jogo finaliza, e o computador informa quantas tentativas foram necessárias.
"""