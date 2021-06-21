"Peter Nguyen"
"6/20/2021"
"CIS2348"
"1860823"
"6.22 CIS 2348 LAB: Brute force equation solver"

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

solution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            solution = True

if not solution:
    print("No solution")