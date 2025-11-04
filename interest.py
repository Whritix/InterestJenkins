principal = 10000;
rate = 12
time = 3


simple_interest = (principal * rate * time) / 100
compound_interest = principal * (1 + rate/100) ** time - principal

# Output
print("Simple Interest is:", simple_interest)
print("Compound Interest is:", compound_interest)