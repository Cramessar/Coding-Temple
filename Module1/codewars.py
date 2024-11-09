#vowel count kata
#need to read carefully and not just make changes 
def get_count(text):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count



#number as string kata
def number_to_string(number):
    return str(number)

#even or odd kata
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
