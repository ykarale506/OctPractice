# Program for calculator

print('''1. Addition
2. Substarction
3. Multiplication
4. Division''')
num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))
choice = input("Enter your choice from above menu :")

if choice == '1':
    print("You selected Sum option :", num_1+num_2)
elif choice == '2':
    print("You selected Substaction option :", num_1-num_2)
elif choice == '3':
    print("You selected Product option :", num_1*num_2)
elif choice == '4':
    print("Ypu selected Division option :", num_1/num_2)




