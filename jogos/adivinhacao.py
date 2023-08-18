from random import randint
sn = 1
while(sn == 1):
    print('-----------------------------')
    print('         Adivinhação         ')
    print('-----------------------------')
    print('Ola! eu pensei em um numero de 0 a 50 tente adivinhar que numero é este!')

    mnum = randint(0, 50)
    chances = 4
    ganhar = False


    while(chances > 0):
        print('Chances: {}'.format(chances))
        unum = int(input('Que numero voce acha que estou pensando? '))

        if unum == mnum:
            print('\033[32mVocê acertou! Parabens!\033[m')
            ganhar = True
            break
        elif unum > mnum:
            print('O numero que eu pensei é \033[33mmenor\033[m')
        else:
            print('O numero que eu pensei é \033[33mmaior\033[m')

        print('-----------------------------')

        chances -= 1

    if ganhar == False:
        print('\033[31mVocê perdeu :(\033[m\nSuas chances acabaram! a resposta certa era {}'.format(mnum))

    print('OBRIGADA POR JOGAR!\n')

    print('-----------------------------')
    print('''Quer jogar novamente?
        1 - Sim
        0 - Não''')
    sn = int(input('Digite sua opção: '))
    print('-----------------------------')



