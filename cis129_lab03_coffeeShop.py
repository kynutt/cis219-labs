#KNuttall Homework Lab 3 for CIS129
#Program that asks for the number of coffee and muffins they are purchasing.
#The price of a cup of coffee is $5 and the price of a muffin is $4. There is a 6% tax on the subtotal.
#Follow the formatting:
"""
***************************************
My Coffee and Muffin Shop
Number of coffees bought?
1
Number of muffins bought?
2
***************************************

***************************************
My Coffee and Muffin Shop Receipt
1 Coffee at $5 each: $ 5.00
2 Muffins at $4 each: $ 8.00
6% tax: $ .78
---------
Total: $ 13.78
***************************************
"""

#The flair at the beginning and end of each section
flair = ('***************************************') 

print(flair + '\nMy Coffee and Muffin Shop')

#Asks for user input relevant to the question. Restricted to integer answers to avoid later errors.
coffeeAmt = int(input('Number of coffees bought?\n'))
muffinAmt = int(input('Number of muffins bought?\n'))

print(flair + '\n\n' + flair)

print('My Coffee and Muffin Shop Receipt')

#Calculates the cost of the item. 
coffeeTotal = coffeeAmt * 5
muffinTotal = muffinAmt * 4

#Prints "<Amt> <Item> at <Price> each: $<TotalItemCost>"
print(str(coffeeAmt) + ' Coffee at $5 each: $ ' + str(coffeeTotal) + '.00')
print(str(muffinAmt) + ' Muffin at $4 each: $ ' + str(muffinTotal) + '.00')

#Calculates the subtotal by adding ItemTotals. Calculates tax, rounding to 2 decimal points. Then adds the two for Total 
subTotal = coffeeTotal + muffinTotal 
tax = round((.06 * subTotal),2) 
Total = subTotal + tax

print('6% tax: $ ' + str(tax))
print("---------")
print('Total: $ ' + str(Total))
print(flair)
