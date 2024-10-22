#it took a while to figure out the spacing of the output but print fixes all.
def display_friends_info():
    friends = {
        'Chris': {'hobby': 'Gaming', 'food': 'RedBull SugarFree'},
        'Mia': {'hobby': 'Sleeping', 'food': 'Pizza and Hotdogs'},
        'Alex': {'hobby': 'Rocket League', 'food': 'Burgers'}
    }

    for name, info in friends.items():
        print(f"{name}'s favorite hobby is {info['hobby']} and their favorite food is {info['food']}.")


print("\nDisplaying friends' info:")
display_friends_info()
print()

#fighting the urge to make anything under 25 a child. -_-
def check_age():
    age = int(input("Please enter your age: "))

    if age < 13:
        print("You are a child.")
    elif 13 <= age < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")
print("Checking user age category:")
check_age()

def calc_input():
    print("\nGive me 2 numbers you want to multiply and add.")
    a = float(input("Give me the first number: ")) #used float because someone, somewhere will try a decimal at some point.
    b = float(input("Give me the second number: "))

    def multiply_numbers(a, b):
        return a * b

    def sum_list(numbers):
        return sum(numbers)

    product_result = multiply_numbers(a, b)
    sum_result = sum_list([a, b])

    print(f"\nThe sum of {a} and {b} is: {sum_result}")
    print(f"The product of {a} and {b} is: {product_result}")


if __name__ == "__main__":
    calc_input()
