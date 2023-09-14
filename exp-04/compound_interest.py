def compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100) ** time
    interest = amount - principal
    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period (in years): "))

interest = compound_interest(principal, rate, time)
print(f"Compound Interest: {interest:.2f}")
