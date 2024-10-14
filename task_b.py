try:
    number = int(input("Enter numerical grade: "))
    

    if number < 0 or number > 100:
        print("Error: Grades must be between 0 and 100")
    else:
        if number >= 80 and number <= 100:
            print("Your grade is: A")
        elif number >= 60 and number <= 79:
            print("Your grade is: B")
        elif number >= 50 and number <= 69:
            print("Your grade is: C")
        elif number >= 40 and number <= 59:
            print("Your grade is: D")
        elif number >= 0 and number <= 49:
            print("Your grade is: F")
except ValueError:
    print("Error: Please enter a number.")