#My first program that is Created by my own
#concept from moving balling(spin ) going in forward direction
#it  took 2 hours 
# Hurray First program that has my own concept
import os
from side_by_side import print_side_by_side
text = input('Enter the name: ')
list1 = []
for i in text:
    list1.append(i) 
print(list1)
i = 0
j = 0
#increase speed of while Loop
print('    *')
print('   * *')
print('  * * *')
print(' * * * *')
print('* * * * *')
print('* * * * *')
print('* * * * *')
print('* * * * *')
print('* * * * *')
print('* * * * *')
print(' * * * *')
print('  * * * ')
print('   * *')
print('    * ')
print('    * ')
print('    * ')
print('* * * * *')
print('* * * * * ')


while True:
    items = list1.pop()
    list1.insert(0, items)
    #print list1 in side by side
    
    str1 = ''.join(list1)
    #print the string in same column
    for j in range(i):
        print(' ', end='')
    
    print(str1, end='')
    
    
    #quit the while loop if i>= 100
    
        
    
    i += 1
    
    
    
    
    #clear the screen
    os.system('cls')
    


   

    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
        
    
    
    
    
    
   
    

    
        
    
        
    
        
    
            
            
        
        
    
    
    
