import random
from passgensheetmaupulation import add_to_sheet



# this generates the password:
def generator(user_name):

    size = user_name.__len__()
    generated_password = ""

    integers = random.randint(141,570)
    symbols = "!@#$%^&*()"
    symbols_random1 = random.randint(0,9)
    letter= user_name.capitalize()
    first_letter = letter[0]

    generated_password += first_letter
    generated_password += symbols[symbols_random1]
    generated_password += str(integers)
    
    symbols_random2 = random.randint(0,9)
    generated_password += symbols[symbols_random2]

    count = 0
    while count<2:
        int_rand = random.randint(1,size-1)
        random_characters = user_name[int_rand]
        generated_password += random_characters
        count += 1

# generated_password = [1]first_Capital_letter + [2] 1_special_character + [3] three_random_integer 
#                     + [4] 1_special_character + Two_random_characters(taken from the username)
    return generated_password



# main() block: 
print("\n........................................................................\n")
print("Enter the command you want to execute: \n\n :) Generate \n\n : Show_my_pass \n\n <3 Admin_login")
user_command = input(">>")


if user_command == "Generate":
    user_name=input("Enter your User_name: ")
    if(user_name.__len__() < 3):
        print("please, Enter a user_name consiting more than 2 letters")
    
    else: 
        password=generator(user_name)

# function from module :-| passgensheetmaupulation | which will add the info to the sheet :)
        add_to_sheet(user_name,password)
        print(password)

if user_command == "Show_my_pass":
    print("....")

if user_command == "Admin_login":
    print(".....") 

