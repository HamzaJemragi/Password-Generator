import random
#The lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input how may letters, numbers and symbols you want
print('Welcome to The PyPassword Generator!')
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Create a password list
password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))
    
#Shuffle the password list
random.shuffle(password_list)

#Add the password string
password = ""
for char in password_list:
    password += char
    
#Print the random Password
print(f'Your password is : {password}')