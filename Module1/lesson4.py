#lesson4

print("this is you calculator, its simple but powerful")
print("select your first number.")
a=int(input())
print("select your second number")
b=int(input())

print("Choose an operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("Choose 1-4.")

choice =  input()
if choice == "1":
    print(("the sum is,"),(a+b))
if choice == "2":
    print(("the difference is,"),(a-b))
if choice == "3":
    print(("your product is,"),(a*b))
if choice == "4":
    print(("the quotient is,"),(a/b))



