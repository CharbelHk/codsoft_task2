def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if y == 0:
        return "Error!"
    return x/y

print("Operations:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice 1/2/3/4: ")
x = float(input("Enter x: "))
y = float(input("Enter y: "))

if choice == '1':
    print("The answer is: " + "x " + "+" + " y" + " =", addition(x,y))
elif choice == '2':
    print("The answer is: " + "x " + "-" + " y" + " =", substraction(x,y))
elif choice == '3':
    print("The answer is: " + "x " + "*" + " y" + " =", multiply(x,y))
elif choice == '4':
    print("The answer is: " + "x " + "/" + " y" + " =", division(x,y))
else:
    print("Invalid Input")

