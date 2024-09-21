# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally, a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.
hotdog = float(print('Hot Dog = $3.50'))
chili_dog = float(print('Chili Dog = $4.50'))
cheese = float(print('Cheese = $0.50'))
peppers = float('$0.75')
grilled_onions = float('$1.00')
if hotdog:
    print(hotdog)
    if cheese or peppers or grilled_onions:
        print(((input('Topping 1: ') + input('Topping 2: ') + input('Topping 3: ')) * float(0.07)) + (input('Topping 1: ') + input('Topping 2: ') + input('Topping 3: ')))
    else:
        print('No Toppings')
else:
    print(chili_dog)
    if cheese or peppers or grilled_onions:
        print(((input('Topping 1: ') + input('Topping 2: ') + input('Topping 3: ')) * float(0.07)) + (
                input('Topping 1: ') + input('Topping 2: ') + input('Topping 3: ')))
    else:
        print('No Toppings')
