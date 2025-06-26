# Input: number of terms
n = int(input("Enter how many Fibonacci numbers to print: "))

# First two terms
a, b = 0, 1
count = 0

print("Fibonacci Series:")

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

