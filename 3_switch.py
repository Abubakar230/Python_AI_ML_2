# switch same parameter
# if else not same parameter

day = int(input("Enter a day in number: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case default:
        print("Invalid day")


hours = int(input("Enter value in hours between 1 to 24"))
match hours:
    case _ if 6 <= hours < 12:
        print("Morning")
    case _ if 12 <= hours < 15:
        print("Afternoon")
    case _ if 15 <= hours < 19:
        print("Evening")
    case _ if 19 <= hours <= 24 or 1 <= hours < 6:
        print("Night")
    case default:
        print("Plz enter between 1 to 24")


# Wildcard Matching

# _ matches any value, making it useful for conditional cases.
# case _ if condition: allows filtering based on conditions rather than exact values.