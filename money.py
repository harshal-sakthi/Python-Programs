# INR to USD Converter (User Input)

# Ask user for amount in INR
inr = float(input("Enter amount in INR: "))

# Ask user for current exchange rate (1 USD = ? INR)
exchange_rate = float(input("Enter current exchange rate (1 USD = ? INR): "))

# Convert INR to USD
usd = inr / exchange_rate

# Show result
print(f"₹{inr:.2f} INR = ${usd:.2f} USD")
