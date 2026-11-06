def costumer_welcome():                                 #def = function (in which we can call anything)
    print("hello , my friend  welcome to @rtsupplies.com")
    print("art essential are found here!")

costumer_welcome()

cost_of_drawing = float(input("Enter the cost of drawing in ($) :"))
TOTAL_drawing_sold =int(input("what is the number of drawing sold today :"))

def calculate_total(drawing,price):
    total = drawing * price
    return total

total_cost = calculate_total(cost_of_drawing,TOTAL_drawing_sold)

rounded_total = round (total_cost , 2)
print("total cost =",rounded_total)

amount_paid = float(input("amount paid by costumer = "))

def calculate_change(paid , total):
    give = paid - total
    return give

change_due = calculate_change(amount_paid,rounded_total)
rounded_change = round(change_due,2)
print("money to give you is ($) :",rounded_change)

