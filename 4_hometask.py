productCategory = input("Enter the product category e.g watch, book: ")
shoppingPrice = int(input("Enter your shoppingPrice: "))
location = input("Enter your location e.g national, International: ")
quantity = int(input("Enter no. of products yoy buy: "))

if quantity <= 5:
    discount = 0
elif quantity <= 10:
    discount = 5
elif quantity <= 15:
    discount = 15
else:
    discount = 20

if location == "national":
    DC = 200
elif location == "International":
    DC = 500

discountPrice = (shoppingPrice * discount) / 100
totalPrice = ((quantity*shoppingPrice) - discountPrice) + DC

print(f"product is {productCategory} and shopping price is {shoppingPrice} that have {quantity} and discount is {discountPrice} and Deliver charges is {DC} and total bill is {totalPrice}")