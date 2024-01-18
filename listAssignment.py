# 1. Write a program that accepts a list from user and print the alternate element of list. 
inputList = input('Input Element of list, separate it by space: ')
list_ = inputList.split(' ')
print("Altenative Elements of list are: ", list_[::-2])

# 2. Write a program that accepts a list from user. Your program should reverse the content of list and
# display it. Do not use reverse() method. 
inputList_ = input('Input Element of list, separate it by space: ')
list__ = inputList_.split(' ')
print('Reverse the content of list: ', list__[::-1])

# 3. Find and display the largest number of a list without using built-in function max(). Your program
# should ask the user to input values in list from keyboard. 
inputList__ = input("Input Element of list, separate it by space: ")
listing = inputList__.split(' ')

max_num = int(listing[0])
for element in listing:
    current_num = int(element)
    if current_num > max_num:
        max_num = current_num
        
print("Maximum number is: ", max_num)

# 4. Write a program that rotates the element of a list so that the element at the first index moves to the
# second index, the element in the second index moves to the third index, etc., and the element in the last
# index moves to the first index. 


# 5. Write a program that input a string and ask user to delete a given word from a string. 
word = input("Input list elements separated by space: ")
listing_ = word.split(' ')

delete = input("Input list item to delete it: ")
if delete in listing_:
    listing_.remove(delete)
    print("Item deleted. Updated list:", listing_)
else:
    print("Item not found in the list. No changes made.")