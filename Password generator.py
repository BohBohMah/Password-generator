import string
import secrets

while True:
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation

    password_length = int(input("Enter the length of the password: "))

    password_type = input("Do you want to use letters? Y/N: ").upper() + input("Do you want to use numbers? Y/N: ").upper() + input("Do you want to use special characters? Y/N: ").upper()
    if password_type == "NNN":
        print("You need to use at least one type of character")
        if input("Do you want to retry? Y/N: ").upper() == "N":
            break
    elif password_type == "YYY":
        password == "".join(secrets.choice(letters + numbers +
                        special_characters) for i in range(password_length))
        print(password)
    elif password_type == "YYN":
        password = "".join(secrets.choice(letters + numbers)
                        for i in range(password_length))
        print(password)
    elif password_type == "YNY":
        password = "".join(secrets.choice(letters + special_characters)
                        for i in range(password_length))
        print(password)
    elif password_type == "YNN":
        password = "".join(secrets.choice(letters) for i in range(password_length))
        print(password)
    elif password_type == "NYY":
        password = "".join(secrets.choice(numbers + special_characters)
                        for i in range(password_length))
        print(password)
    elif password_type == "NYN":
        password = "".join(secrets.choice(numbers) for i in range(password_length))
        print(password)
    elif password_type == "NNY":
        password = "".join(secrets.choice(special_characters)
                        for i in range(password_length))
        print(password)
    else:
        print("Wrong input, use only Y, N, y, n")
        if input("Do you want to retry? Y/N: ").upper() == "N":
            break
    
    if input("Do you want to generate another password? Y/N: ").upper() == "N":
        break