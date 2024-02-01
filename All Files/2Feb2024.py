import numpy as np
foods = ['biryani', 'zarda']
foods.append('pani') # only one item can add to list usinf append
print(foods)

foods.insert(-1,'qorma') # index, item (index can be your choice)

foods.extend(['chapati', 'taftan', 'anda wala burger'])

# deleting item from list
del foods[3] # delete using index
foods

foods.remove('anda wala burger') # remove writtten item from list

foods

foods.pop() # remove default last value
foods.pop(3) # also remove using index
foods
foods.clear() # remove all item from list

foods

help(foods)
foods

str1 = 'muhammad'
for i in range(len(str1)):
    print(str1[i], end='')

list = []
for i in range(5):
    name = input("Enter Name: ")
    list.append(name)
list

# List comprehension
list = [input("Enter Name: ") for i in range(5)]
list

squares = [f'Square of {square} is {square**2}' for square in range(1, 101)]
squares[0:5]

names = input("Enter space separated name").split(" ")
names
" ".join(names)

unit_matrix = np.eye(3)
unit_matrix[0] + unit_matrix[1]

import pandas as pd
import numpy as np
from word2number import w2n

data = {'Number': ['one', 'two', 'nine', 'eleven']}
df = pd.DataFrame(data)

def word_to_number(row):
        return w2n.word_to_num(row)
    
df['WordToNumber'] = df['Number'].apply(word_to_number)
df
print(df)

type(data)
df.pop('Number')
df

# Dictionary
student = {'Names':['Umer', 'Taha', 'Zaid'], 'Age':[13, 15, 24]}
student
pd.DataFrame(student)