import math

K = 0.01
L = 3
x = y = a = b = float()

print("Please enter a value for X:")
x = float(input())

a = 7.002 * math.sqrt(K) - 1 + 0.1 * (math.exp(x) + math.exp(-x))
if a <= 0:
    print("ERROR: Negative value in square root calculation for 'a'.")
else:
    a = math.exp((1.0 / 5.0) * (math.log(a)))
    print("Result for A is:", a)

    b = math.log10(L) * (math.cos(math.pi / 5) + math.cos(3 * math.pi / 5))
    print("Result for B is:", b)

    if a ** 2 + b ** 2 > 0.1:
        y = math.atan(5 * a ** 2 + 7 * b ** 2)
    else:
        if 1 - math.pow(5 * a ** 2 + 7 * b ** 2, 2) == 0:
            print("ERROR:devision by zero")
        else:
            y = math.atan(5 * a ** 2 + 7 * b ** 2 / (math.sqrt(1 - math.pow(5 * a ** 2 + 7 * b ** 2, 2))))
    print("Result for Y is:", y)