"""
Problem:
You are tasked with developing a Python applications that converts amounts between USD(United states Dollars) and PHP(Peso). The application should prompt the user to enter the amount in USD and convert this to PHP based on a predefined exchange rate. Additionally, the application should handle different data types and ensure proper type conversions where necessary.

Requirements
user_input
amount_rate_usd
amount_rate_eur
converted_amount

"""

# Exchange Rate
amount_rate_php = 60

while True:
    try:
        # Prompt for user input
        amount_rate_usd = float(input("Amount in USD: "))
        
        # Conversion
        converted_amount = amount_rate_usd * amount_rate_php
        
        # Output the converted amount
        print(f"Converted amount: {converted_amount} PHP")
        
    except ValueError:
        # Handle invalid float input
        print("Enter a valid amount")
        continue
    
    while True:
        # Ask the user if they want to exit
        user_input = input("Want to exit? (yes/no): ").lower().strip()
        
        if user_input == 'yes':
            print("Exiting the program.")
            exit(0)  # Exit the loop and program if user inputs 'yes'
        elif user_input == 'no':
            break  # Break the inner loop and continue with the next iteration of the main loop
        else:
            print("Please enter 'yes' or 'no'.")

print("Exiting the program.")
