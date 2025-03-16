# switch same parameter
# if else not same parameter

# how many your total shopping price


shoppingPrice = int(input("Enter your shoppingPrice: "))

if shoppingPrice < 500:
    DC = 500
    totalDiscountCost = (shoppingPrice * 0)/100
    totalPrice = (DC + shoppingPrice)-totalDiscountCost
    print(f"You purchase product in {shoppingPrice} and discount is {totalDiscountCost} and delivery charges is {DC}")
    print("totalPrice is: ",totalPrice)
elif shoppingPrice >= 500 and shoppingPrice <= 1500:
    DC = 1000
    totalDiscountCost = (shoppingPrice * 5)/100
    totalPrice =  (DC + shoppingPrice)-totalDiscountCost
    print(f"You purchase product in {shoppingPrice} and discount is {totalDiscountCost} and delivery charges is {DC}")
    print("totalPrice is: ",totalPrice)
elif shoppingPrice > 1500 and shoppingPrice <= 2500:
    DC = 1500
    totalDiscountCost = (shoppingPrice * 10)/100
    totalPrice = (DC + shoppingPrice)-totalDiscountCost
    print(f"You purchase product in {shoppingPrice} and discount is {totalDiscountCost} and delivery charges is {DC}")
    print("totalPrice is: ",totalPrice)
elif shoppingPrice > 2500:
    DC = 0
    totalDiscountCost = (shoppingPrice * 15)/100
    totalPrice = (DC + shoppingPrice)-totalDiscountCost
    print(f"You purchase product in {shoppingPrice} and discount is {totalDiscountCost} and delivery charges is {DC}")
    print("totalPrice is: ",totalPrice)