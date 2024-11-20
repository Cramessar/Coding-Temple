#lesson 2

my_list = ("John Wick", "Kingdom of Heaven", "Lord of the Rings", "Man of Steel", "Scarface", 1108, 970)
print ("Third element:", my_list[2])
print ("Fifth element:", my_list[4])

sliced_tuple = my_list[1:7]
print("Sliced tuple:", sliced_tuple)

count_code = my_list.count("Code")
print("Count of 'Code':", count_code)

a, b, c, d, e, f, g, = my_list
print(a, b, c, d, e, f)

new_tuple = my_list + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)

