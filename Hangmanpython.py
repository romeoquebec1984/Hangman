# Word Selector
word_pool=['dragon','stone','god','armor','baseball']
import random
i=random.randint(1,len(word_pool))
chosen_word =word_pool[i-1]


print(chosen_word)
print(len(chosen_word))
print(chosen_word[0])

lives=0
word='incomplete'
letterschosen=[]

#game
while lives<6 and word=='incomplete':
    lettercount=0
    turn=1
    

    for i in range(0,len(chosen_word)):
        if chosen_word[i] in letterschosen:
            lettercount=lettercount+1
            print(chosen_word[i])
        else:
            print(' _ ')
    if past==present and turn!=1:
        lives+1
    letterschosen.append(input('\nguess a letter'))



    if lettercount== len(chosen_word):
        print('You win')
        word='complete'
    if lives>6:
        print('You loose')
    lives=lives+1

    print(f'letter {lettercount}')
    print(f'lives{lives}')
    turn=turn+1

print('\n\n\nendofgame')

