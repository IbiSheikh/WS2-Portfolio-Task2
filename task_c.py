def password_checker(password):

    if len(password) < 8:
        return False

    contain_letter = False
    contain_digit = False

    for char in password:
        if char.isalpha():
            contain_letter = True
        elif char.isdigit():
            contain_digit = True 


    return contain_letter and contain_digit 

password = input("Enter a password which contains numbers and letters only: ")

if password_checker(password):
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")