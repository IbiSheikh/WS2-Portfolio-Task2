
def day_number(day):


    match day:
        case "Monday":
            return 1
        case "Tuesday":
            return 2
        case "Wednesday":
            return 3
        case "Thursday":
            return 4
        case "Friday":
            return 5
        case "Sunday":
            return 6
        case "Saturday":
            return 7
        case _:
            return "Please enter a valid day"

user_input = input("Enter a day of the week: ").strip().lower().title()
print(user_input + " is day " + str(day_number(user_input)))