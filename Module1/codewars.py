#vowel count kata
def vowel_count(text):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("Enter a word, and we will count the vowels: ").lower()
print("Number of vowels:", vowel_count(text))
###this isnt working in code wars and I dont see a clear reason why. 
# Return the number (count) of vowels in the given string. [line 8 ]
# We will consider a, e, i, o, u as vowels for this Kata (but not y). [line 3 defining the list]
# The input string will only consist of lower case letters and/or spaces [.lower()]

#number as string kata
def number_to_string(number):
    return str(number)

#even or odd kata
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
