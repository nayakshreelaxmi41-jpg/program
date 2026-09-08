# Program to handle positive and negative exponents

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

if exponent >= 0:
    result = base ** exponent
else:
    result = 1 / (base ** abs(exponent))

print("Result =", result)
