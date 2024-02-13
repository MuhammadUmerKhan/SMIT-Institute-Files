# tuple
a = 1, 2, 3, 4, 5, 6
type(a) # tuple

country_capital = {"Pakistan":['Islamad'],
                   "America":["New York"]};
city_pop = {}
for a in range(5):
    city_name = input("Enter City name: ").capitalize()
    if  city_name in city_pop.keys():
        print("Already Added")
    else:    
        pop = int(input("Enter Population: "))
        city_pop[city_name] = pop
        
glossary = {}
for i in range(5):
    language = input("Enter Programming Language Name: ").capitalize()
    if language in glossary.keys():
        print("Already added...")
    else:
        meaning = input("Enter meaning: ")
        glossary[language] = meaning

searchWord = input("Enter Word").capitalize()
if searchWord in glossary:
    print(glossary[searchWord])
    
length = input("How many times you want to search: ")
for i in range(int(length)):
    word = input("Enter Country name or q to exit: ").capitalize()
    if word == 'Q':
        break
    elif word in city_pop.keys(): 
        print("Population: ", city_pop[word])
    else:
        print("Word not matched")