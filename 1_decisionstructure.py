# Decision structure 
#  is used to change the flow of the program according to the given condition
#  if , if-else , switch , nested decision structure


age = int(input("Enter your age"))
if age >= 18:
    print("Eligible for apply CNIC")
else:
    print("Not eligible for apply CNIC")



qualification = int(input("Enter your qualification in number"))
weight = int(input("Enter your weight"))
height = float(input("Enter your height"))

if qualification == 12:
    if weight >= 70:
        if height >= 5.10:
            print("Eligible")
        else:
            print("Not Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")



p = 45
if p <= 10:
    print("Free")
elif p > 10 and p < 20:
    print("5 per off")
elif p > 20 and p < 30:
    print("10 per off")
else:
    print("20 per off")


# switch same parameter
# if else not same parameter