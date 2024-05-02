"""
Problem:
You are tasked with developing a Python applications that converts amounts between USD(United states Dollars) and PHP(Peso). The application should prompt the user to enter the amount in USD and convert this to PHP based on a predefined exchange rate. Additionally, the application should handle different data types and ensure proper type conversions where necessary.

Requirements
user_input
amount_usd
exchange_rate_php
converted_amount

"""
# Exchange Rate
exchange_rate_php = 60

while True:
    try:
        # Prompt for user input
        amount_usd = float(input("Amount in USD: "))
        
        # Conversion
        converted_amount = amount_usd * exchange_rate_php
        
        # Output the converted amount with two decimal places
        print(f"Converted amount: {converted_amount:.2f} PHP")
        print("Converted Successfully")
        
    except ValueError:
        # Handle invalid float input
        print("Please enter a valid amount.")
        continue
    
    while True:
        # Ask the user if they want to exit
        user_input = input("Do you want to exit? (yes/no): ").lower().strip()
        
        if user_input == 'yes':
            print("Exiting the program.")
            break  # Exit the loop and program if user inputs 'yes'
        elif user_input != 'no':
            print("Please enter 'yes' or 'no'.")

print("Program is Terminated")

