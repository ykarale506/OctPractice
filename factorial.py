# program to print the factorial

num = int(input("Enter number to calculate fact :"))
fact = 1
for i in range(1,num+1):
    fact =fact*i
print("Factorial of",num,"is :",fact)