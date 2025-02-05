# rock,paper,scissors

import random

count = 0 #turn count
c_score = 0 #computer score
u_score = 0 #user score
name = input('Enter your name: ') #user name
print('welcome', name)
print()

while True:
    if count ==3:
        break
    else:
        options = ['rock', 'paper', 'scissors' ]
        print(' 1.ROCK   2. PAPER   3. SCISSORS 4. EXIT')
        u_turn = input('Enter you choice: ')
        c_turn = random.choice(options)

        if u_turn == 'rock':
            print('computer choice: ', c_turn)
            if c_turn == 'paper':
                count = count+1
                print('computer won')
                print()
                c_score = c_score +1
                
            elif c_turn == 'scissors':
                count = count+1
                u_score = u_score +1
                print(name,' Won')
                print()
                
            elif c_turn == 'rock':
                count = count+1
                print('Tie')
                print()
                

        elif u_turn == 'paper':
            print('computer choice: ', c_turn)
            if c_turn == 'paper':
                count = count+1
                print('Tie')
                print()
                
            elif c_turn == 'scissors':
                count = count+1
                print('computer won')
                print()
                c_score = c_score +1
                
            elif c_turn == 'rock':
                count = count+1
                u_score = u_score +1
                print(name,' Won')
                print()

        elif u_turn == 'scissors':
            print('computer choice: ', c_turn)
            if c_turn == 'paper':
                count = count+1
                u_score = u_score +1
                print(name,' Won')
                print()
                
            elif c_turn == 'scissors':
                count = count+1
                print('Tie')
                print()
                
            elif c_turn == 'rock':
                count = count+1
                print('computer won')
                print()
                c_score = c_score +1

        elif u_turn == 'exit':
            print(name, 'Bye')
            break

        else:
            print(name, 'Please give correct input')
            print()

#final result

print('*'*25)
if c_score > u_score: #if computer has more score
    print('*',name, ' you lost! Computer won','*')

elif u_score > c_score: #if user has more score
    print('*',name,' you won!','*')

elif u_score ==0 and c_score == 0: 
    print('*','come again','*')
     
else:
    print('*','   Its a tie!  ','*')
print('*'*25)
