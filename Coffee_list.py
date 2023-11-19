# Create a python script that has a dicatinary of coffee product and price
# User wants to pick a product and return the cost for that proudtc and then
# Ask the user if they want anything else and if not than produce the total bill


# Create a dictonary with the list items and the associated cost
product_list = {
    'Matcha': 3.50,
    'Americano': 2.25,
    'Chai': 3.15,
    'Lattes': 4.00
}
user_continue = 'Yes'

bill = 0

while user_continue == 'Yes':
    product_name = input("Which item on our list would you like? ")
    price = product_list.get(product_name, 0)
    print(product_list.get(product_name, 'We do not sell this product, please try again.'))
    user_continue = input('Would you like another item or to quit? Yes or No ')
    bill = bill + price
    
print(f'Thank you for coming your total price is {bill}')

