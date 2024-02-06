# import pandas as pd

my_dict = {"ID":[1, 2, 3,4 ,5 ,6 ,7 ,8 ,9 ,10],
           "Name":['Umer', 'Abdullah', 'Farhan', "Ali", "Zaid",
                   "Uzair", "Musab", "Osman", "Abu Bakar", "Kashan"],
           "Age":[23, 45, 67, 87, 55, 65, 34, 32, 23, 43],
           }
# df = pd.DataFrame(my_dict)
# df.head()
# df.drop(columns='ID', inplace=True)
print(my_dict)
my_dict.keys()
my_dict.items()

# Tuple 
# immutable
a = (1, 2, 3, 4, 5, 6)
type(a)
# 
# Loops

for i,n in enumerate(a):
        print(i, n)
        
number = []
for input_ in range(10):
        inputNumber = int(input("Enter Number: "))
        if (inputNumber%2!=0):
                number.append(inputNumber)
        else:
                continue
print(number)

nameList = []
for i in range(10):
        names = input("Input names: ")
        if (len(names.strip()) <= 6):
                nameList.append(names)
        else: continue
nameList

newList = []
for i in nameList:
        if (i[0] == 'a') or (i[-1] =='d') or (i[0] == 'u'):
                newList.append(i)
newList

newList = []
for i in nameList:
        if i.startswith('a') or i.startswith('u') or i.endswith('d'):
                newList.append(i)
newList
