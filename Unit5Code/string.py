
def password_checker(password):
    upperCount = 0
    lowerCount = 0
    digitCount = 0
    if password.isalnum() == False:
        print("Invalid")
    elif len(password) < 8 or len(password) > 12:
        print("Invalid")
    else:
        for char in password:
            if char.isupper():
                upperCount += 1
            elif char.islower():
                lowerCount += 1
            elif char.isdigit():
                digitCount += 1
        if lowerCount >= 3 and upperCount >=2 and digitCount >= 1:
            print("Valid")
        else:
            print("Invalid")    

password_checker("PaSsWo123")