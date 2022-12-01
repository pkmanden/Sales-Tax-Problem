# Sales-Tax-Problem

Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. Import duty is an additional sales tax
applicable on all imported goods at a rate of 5%, with no exemptions. When I purchase items I receive a receipt which lists the name of all the items and their price (including tax), finishing with the total cost of the items,
and the total amounts of sales taxes paid. The rounding rules for sales tax are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.
Write an application that prints out the receipt details for these shopping baskets...


### INPUT:
Input 1:
> 1 book at 12.49

> 1 music CD at 14.99

> 1 chocolate bar at 0.85

Input 2:
> 1 imported box of chocolates at 10.00 

> 1 imported bottle of perfume at 47.50

Input 3:
> 1 imported bottle of perfume at 27.99 

> 1 bottle of perfume at 18.99

> 1 packet of headache pills at 9.75

> 1 box of imported chocolates at 11.25


# How to run
In order to run the application, only python3 is needed. print_tax_receipt.py is the file to be run as

python3 print_tax_receipt.py


# Assumptions

Assuming the goods are of types chocolates, pills and books for these particular shopping baskets.
