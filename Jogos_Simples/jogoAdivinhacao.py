import random
opt=2; palpite=0; tentativas=0
while(opt != 0):
    print("============Jogo de Adivinhação============")
    print("Será gerado um numero aleatório de 1 a 100, tente descobrir")
    print("Você terá 5 tentativas")
    print("1: para iniciar")
    print("0: para encerrar")
    print("===========================================")
    opt = int(input("Escolha uma opção: 1"))
    if (opt == 1):
        numeroAd = random.randrange(1,101)
    else:
        print("Obrigado por jogar!") 
   
    while (palpite != numeroAd):
        if (tentativas == 5):
            print("Sua ultima tentativa, boa sorte!")
        
        palpite = int(input("Digite um palpite: "))
        if (palpite > numeroAd and tentativas < 5):
            if (palpite == numeroAd+1 or palpite == numeroAd-1):
                print("Muito perto!")
            else:
                print("Um pouco menor!")
        elif (palpite < numeroAd and tentativas < 5):
            if (palpite == numeroAd+1 or palpite == numeroAd-1):
                print("Muito perto!")
            else:
                print("um pouco maior!")
                
        
        if (palpite == numeroAd):
            print("Acerto miseravi!!!")
        else:
            tentativas += 1
            if(tentativas == 6):
                print("Não foi dessa vez!")
                palpite = numeroAd
                tentativas = 0
        
        
            