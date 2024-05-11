# Python3 program to find compound
# interest for given values.

def compound_interest(principal, rate, time):
    # Calculates compound interest
    A = principal * (pow((1 + rate / 100), time))
    CI = A - principal
    print("Compound interest is", CI)


compound_interest(10000, 5, 2)