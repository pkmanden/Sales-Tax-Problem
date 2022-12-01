import math

BASE_TAX = 10   # base tax 10%

def print_receipt(inp):
    # Function to retrieve the input items and print out the receipt

    exempted_goods = ['book', 'chocolate', 'pills', 'books', 'chocolates'] # list of exempted goods
    sales_taxes = 0.00
    total_price = 0.00

    # Loop through the input list to process each of the items
    for item in inp:
        item_tax = BASE_TAX     # tax rate for an item
        exempted = False        # flag for exempted item
        imported = False        # flag for imported item
        item_total = 0.00       # item price after tax calculation
        item_tax_amount = 0.00  # tax amount for an item

        item_to_list = item.split()         # convert the input to a list
        quantity = int(item_to_list.pop(0)) # item quantity extracted
        price = float(item_to_list.pop())   # item price
        item_to_list.pop()                  # remove 'at' from list
        
        # Loop through the converted item list to check whether the item is exempted or imported
        for i in item_to_list:
            if i in exempted_goods:
                exempted = True
            if 'import' in i:
                imported = True

        # set tax rate according to whether exempted and imported
        if exempted: 
            if imported:
                item_tax = 5
            else:
                item_tax = 0
        else:
            if imported:
                item_tax = 15
                
        # Calculate taxes and final prices
        item_tax_amount = round_tax((item_tax * price) / 100)
        item_total = round((price + item_tax_amount), 2)

        sales_taxes = round_tax(sales_taxes + item_tax_amount) 
        total_price = round((total_price + item_total), 2)

        # Print out the item details and final receipt
        print(str(quantity)+ ' ' + ' '.join(item_to_list)+' :', item_total)
    print('Sales Taxes : ' , sales_taxes)
    print('Total : ' , total_price)


def round_tax(amount) :
    # Function for the sales tax rounding rules
    return math.ceil(round(amount,2) * 20) / 20 # using 20 because of rounding up to 0.05


if __name__ == "__main__":
    input_1 = ["1 book at 12.49", "1 music CD at 14.99", "1 chocolate bar at 0.85"]
    input_2 = ["1 imported box of chocolates at 10.00", "1 imported bottle of perfume at 47.50"]
    input_3 = [" 1 imported bottle of perfume at 27.99", "1 bottle of perfume at 18.99", "1 packet of headache pills at 9.75", "1 box of imported chocolates at 11.25"]
    print_receipt(input_1)
    print_receipt(input_2)
    print_receipt(input_3)
