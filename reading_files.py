# Top 10 most common words in a text file
filename = input('Enter filename: ')
fhand = open(filename)
list1 = fhand.read().split()
list2 = []
dict1 = {}
# using Get method to get the value of a key
for i in list1:
    dict1[i] = dict1.get(i, 0) + 1

for key, value in dict1.items():
    list2.append((value, key))

#sort the list2 in reverse order
list2.sort(reverse=True)
for i, j in list2[:10]:
    print(j + ' = ', i)


    
    

    


