def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # checking if discount is greater or equal to 20%
       get_discount = (price * discount_percent) / 100  #calculating the discount amount first
       discounted_price = price - get_discount  # Calculating the final price after discount
       return f'Your total price after discount is: {discounted_price:.2f}'
    else:
        return f'Your total price without discount is: {price:.2f}'

#prompting the user to enter the original price of an item and the discount percentage
original_price = float(input('Enter your price: '))
percent_discount = float(input('Enter percentage discount: '))

# Call the function with user inputs
item_price=calculate_discount(original_price, percent_discount)
print(item_price)
 