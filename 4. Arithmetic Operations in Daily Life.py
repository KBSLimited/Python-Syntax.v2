#Task 1: Grocery Store Math
x = 8.65
y = 4.99
z = 3.50

total = x + y + z
print("The total is:", total)

# Task 2: Bank Interest
principal = 10000  # Use descriptive variable names
n = 4              # Number of times interest is compounded per year
rate = 8.00        # Annual interest rate in percentage
years = 1          # Number of years

# Calculate future value (FV)
FV = principal * (((1 + ((rate / 100.0) / n)) ** (n * years)))

print("The final amount after", years, "years is:", FV)