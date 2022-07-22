# A Quiz Game in Python
print('Welcome to the Quiz Game!')
answer = input('Are you ready? (y/n): ')
score=0
total_questoin=3

if answer.lower()=='y':
    answer = input('Question 1: What is the capital of India? ')
    if answer.lower()=='delhi':
        score+=1
        print('Correct!')
    else:
        print('Wrong! :(')

    answer = input('Question 2: What is the capital of USA? ')
    if answer.lower()=='washington':
        score+=1
        print('Correct!')
    else:
        print('Wrong! :(')
        
    answer = input('Question 3: What is the capital of China? ')
    if answer.lower()=='beijing':
        score+=1
        print('Correct!')      
    else:
        print('Wrong! :(')
        
    print('Your score is: ', score)
    print('You got ', score, ' out of ', total_questoin)

print('Thanks for playing!')
    
    




