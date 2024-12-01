jedi_name = "luke skywalker"
jedi_rank = "jedi knight"
force_power = 100

""""
Docstrings
    1. what the fuction does
    2. the received parameters and data types
    3. what is the returned and data type
"""

def greet_all_jedi():
    """ 
    Greets the jedi
    """
    print("Hello Jedi")

greet_all_jedi()

def attack(target, weapon="lightsaber"):
    """
    Perform an attack on a target with a specified weapon.
    Parameters:
    target (str): The target being attacked.
    weapon (str): The weapon being used. Defaults to "lightsaber".
    
    Returns:
    str: The action of the attack.
    """
    jedi_name="obi wan kenobi"
    return f"{jedi_name} attacks {target} with a {weapon}"

print(attack("Darth Vader"))
print(attack("darth maul", "stomach slice"))
print(f"the global var jedi_name {jedi_name} was not affected")

def add_force_power(*points):
    print(points[0])
    print(points[1])
    """
    Adds points to the Jedi's total points.
    Parameters:
    *points (int): Multiple point values to be added.
        - The * means it can accept however many arguments passed in
        - Values are placed in a tuple (immutable list)
    
    Returns:
    int: The new total points.
    """
    total_power = sum(points)
    global force_power # uses the global force_power var, not a local one
    force_power += total_power
    return force_power

print(f"Jedi's force power after battle: {add_force_power(50, 75, 25)}")
print(f"The global var force_power was changed to {force_power}")


def use_force(power, **kwargs):
    """
    Use the Force to perform an action with additional effects.
    Parameters:
    power (str): The type of Force power.
    **kwargs: Additional named arguments (e.g., 'duration', 'intensity').
        - accepts "key = value" arguments and puts them in a dictionary
    Returns:
    str: Description of the Force action.
    """
    action_details = ""
    
    for key, value in kwargs.items():
        action_details += key + " : "
        action_details += value + " | "    
    
    # another way of doing this using a shorthand method
    #action_details = ' | '.join(f"{key}: {value}" for key, value in kwargs.items())
    
    return f"{jedi_name} uses {power} with the following effects: {action_details}."
print(use_force("Telekinesis", duration="5 seconds", intensity="High"))


