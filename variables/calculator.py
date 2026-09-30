# work with int
# x = int(input("Whats x? "))
# y = int(input("Whats y? "))

#print(x + y)

# work with float
x = float(input("Whats x? "))
y = float(input("Whats y? "))

z = (x / y)

print(f"{z:.2f}")

def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()