"""Author:Liya Binu
Date:19-11-2024
program to calculate store details"""
inventory=[("Laptop",10,40000),
           ("smart phone",20,12000),
           ("keyboard",15,200)]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=(quantity*unit_price)
    print("item name:",item_name,"the total value is",stock_value)
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
        print(f"highest stock value is{stock_value}")
        print("item with highest stock value is:",item_with_highest_stock_value)
