def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period (in years): "))

interest = simple_interest(principal, rate, time)
print(f"Simple Interest: {interest:.2f}")
