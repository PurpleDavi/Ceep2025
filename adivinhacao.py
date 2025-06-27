#Davi Carlos N°7

import random
# biblioteca para efetivar o sorteio do numero, já pronto, apenas iremos informar posteriormente o interior
import os
# bilbioteca do sistema operacional, para limapr a tela, se winodows cls, no linux clear
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("digite seu número!   "))
while(sorteado>jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("ERRO, o número é maior")
    elif(sorteado<jogador):
        print("ERRO, o número é menor")
        erros+=1
        jogador=int(input("digite seu número:   "))
print("Número" + str(jogador) + " , você acertou em: " + str(erros+1) + "  tentativas")