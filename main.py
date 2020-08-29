price = float(input('What is the price of the item? '))
itemTax = price*0.06
PriceWTax = price+itemTax
rawTax = '6%'

print('Item price is $' + str(price) + " before tax.")
print('Tax on the item will be ' + str(rawTax))
print('This item costs $' + str(round(PriceWTax, 2)))
