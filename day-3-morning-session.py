num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

def add(num1,num2):
    """This function adds two numbers it gets from a user"""
    sum=num1+num2
    return sum

print("The sum is",add(num1,num2))
print(add.__doc__)