
def proOrSum (a,b):
    if a*b > 1000:
        print("The sum is:", a+b) 
    else: 
        print("The product is:", a*b) 

a = int(input("Enter 1st interger: "))
b = int(input("Enter 2nd interger: "))

print()
proOrSum(a, b)