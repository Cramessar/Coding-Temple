#again if anyone reads this code dont judge me too harshly

#numbers and squares
numbers = list(range(0, 10))
print("list of numbers", numbers)
squares = [number**2 for number in numbers]
print("List of squares:", squares)


#odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
 
#pizza toppings, yes pineapple is acceptable!    
toppings = []
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")

    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"{topping} added to your pizza.")
print("\nYour favorite pizza toppings are:")
for topping in toppings:
    print(f"- {topping}")

"https://github.com/Cramessar/Coding-Temple/blob/main/Working_with_Data.py"