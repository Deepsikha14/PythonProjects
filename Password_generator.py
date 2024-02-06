print("WELCOME TO THE PASSWORD GENERATOR!!")
import random
letters = ['a','b','c','d','e','f','g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','%','^','&','*','(',')']
nr_letters = int(input(f"How many letters do you want? \n"))
nr_numbers = int(input(f"How many numbers do you want? \n"))
nr_symbols = int(input(f"How many symbols do you want? \n"))

password_list = []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
      