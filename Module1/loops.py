characters = ["Luke Skywalker", "Darth Vader", "Yoda", "Leia Organa", 
              "Han Solo", "Emperor Palpatine", "Chewbacca"]

for i in range (0, len(characters)):
    print (f"{i+1} - {characters[i]}")

for index, name in enumerate (characters):
    #print (i) #i is the index
    print (f"{index+1} - {name}")

print("-" * 30)
    
print ("Preparing for light speed jump!")
for second in range (5, 0, -1):
    print (f"{second}...")
print ("light speed activated! VROOM!!!")

print ("-" * 30)

print ("Who will bring balance to the force?")    
for character in characters:
    if character == "Darth Vader": 
        print(f"{character} brought balance to the for but at great cost!")
    elif character == "Emperor Palpatine":
        print(f"{character} is pure evil!")
    else:
        print(f"{character} is probably an ally")
    
print ("-" * 30)

weapons = ["lightsaber", "force choke", "force push", "blaster"]

for weapon, character in zip(weapons, characters):
    print(f"{weapon} protects {character}")

while True:
    print("This will blow up the world")
    break

tracker=True
while tracker:
    print("This will blow up the world")
    tracker=False
    
