#lesson 9
account_balance = 1500
print("Your current Account Balance is: ", account_balance)

try:
    withdraw=int(input("Enter the amount you would like to withdraw from the account: "))
    if withdraw > account_balance:
        raise ValueError;
        print(f"Please enter a number less than {account_balance}")
    if withdraw < 0:
        raise ValueError;
        print(f"Please enter a number greater than 0. ")
except TypeError:
    print ("Please enter a number")


else:    
        print(f"Your new Account Balance is :", account_balance-withdraw)
finally:
    print("Thank you for banking with us today! ")
    
account_balance = 1500
print("Your current Account Balance is:", account_balance)

try:
    withdraw = int(input("Enter the amount you would like to withdraw from the account: "))
    if withdraw > account_balance:
        print(f"Please enter a number less than or equal to {account_balance}")
        raise ValueError("Insufficient balance for this withdrawal.")
    if withdraw < 0:
        print("Please enter a number greater than 0.")
        raise ValueError("Negative withdrawal amounts are not allowed.")
    
except ValueError as e:
    print("Error:", e)

else:
    account_balance -= withdraw
    print("Your new Account Balance is:", account_balance)

finally:
    print("Thank you for banking with us today!")
