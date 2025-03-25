def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price
    
# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))
    
    # calculate the final price
    final_price = calculate_discount(original_price, discount)
    
    # print the result
    if final_price < original_price:
        print(f"The final price after applying a {discount}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
        
except ValueError:
    print('Please enter valid numeric values for price and discount percentage.')