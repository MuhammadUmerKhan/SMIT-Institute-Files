# Write a program that accepts a string from user. Your program should count and display number of
# vowels in that string. 
numOfVowel = 0
inputString = input("Input String: ").lower()
for vowel in inputString:
    alphabel = ['a', 'e', 'i', 'o', 'u']
    if vowel in alphabel:
        numOfVowel = numOfVowel + 1
print("There are Number of vowels {} in '{}'".format(numOfVowel, inputString))

#  2. Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string 

uppercase = 0
lowercase = 0
lowercase =0 
whitespace = 0
others = 0
inputString_ = input("Input String: ")
for alpha in inputString_:
    if alpha.isupper():
        uppercase +=1
    elif alpha.islower():
        lowercase += 1
    elif alpha.isspace():
        whitespace += 1
    else:
        others +=1
print("""
    Number of Upper Case Alphabets are: {}
    Number of Lower Case Alphabets are: {}
    Number of Whitespaces are: {}
    Number of special characters are: {}
    are in '{}'
      """.format(uppercase, lowercase, whitespace, others, inputString_))

#  3. Write a Python program that accepts a string from user. Your program should create and display a
# new string where the first and last characters have been exchanged. 
inputString__ = input("Input String: ").lower()
newString = inputString__[-1]+inputString__[1:-1]+inputString__[-1]
print(newString)

#  4. Write a Python program that accepts a string from user. Your program should create a new string in
# reverse of first string and display it.
inputString___ = input("Input String: ").lower()
newString_ = inputString___[::-1]
newString_

# 5. Write a Python program that accepts a string from user. Your program should create a new string by
# shifting one position to left. 
inputString____ = input("Input String: ").lower()
newString__ = inputString____[1:]+inputString____[0]
newString__

# 6. Write a program that asks the user to input his name and print its initials. Assuming that the user
# always types first name, middle name and last name and does not include any unnecessary spaces.

fullName = input("Enter you full name: ")

firstSpace = fullName.find(' ')
secondSpace = fullName.rfind(' ')

print("Your initials are: {}. {}. {}".format(fullName[0], fullName[firstSpace+1], fullName[secondSpace+1]))

# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad,
# madam and radar are all palindromes. Write a programs that determines whether the string is a
# palindrome. 

inputString_____ = input("Input String: ").lower()
palindrome = inputString_____[::-1]
if str(inputString_____) == str(palindrome):
    print("It's a Palindrome word")
else:
    print("Not a Palindrome Word")

# 8. Write a program that display following output:
# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT
string = "SHIFT"
for i in range(len(string)):
    suffle = string[i:] + string[:i]
    print(suffle)
    
#  9. Write a program in python that accepts a string to setup a passwords. Your entered password must
# meet the following requirements:
# The password must be at least eight characters long.
# It must contain at least one uppercase letter.
# It must contain at least one lowercase letter.
# It must contain at least one numeric digit.
# Your program should should perform this validation.
upper = 0
lower = 0
numeric = 0

inputString = input("Input String: ")

if len(inputString) >= 8:
    for char in inputString:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isnumeric():
            numeric += 1

    if upper < 1 or lower < 1 or numeric < 1:
        print("""
            It must contain at least one uppercase letter.
            It must contain at least one lowercase letter.
            It must contain at least one numeric digit.
        """)
    else:
        print("Your Password matches all Requirements")
else:
    print("The password must be at least eight characters long.")
