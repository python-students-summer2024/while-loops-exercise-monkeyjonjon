def get_starting_number():
    """
    WITH A WHILE_LOOP_ACCUMULATOR:
    this function asks the user how many bottles of beer on the wall they want to start singing with, 
    e.g. "How many bottles of beer on the wall?" 
    The function asks this question as many times as necessary until the user enters a valid response, 
    which is considered to be any integer 1 or greater. 
    The function then returns the integer equivalent of the value the user entered.
    (Added a token for fun)
    """
    correct_inputs = 0 # The accumulator
    tokens = 0
    while correct_inputs <= 0:
        bottle_number = input("How many bottles of beer are on the wall? ")
        if bottle_number.isdigit() and int(bottle_number) >= 1:
            bottle_number = int(bottle_number)
            correct_inputs += 1 # The accumulator accumulates?
            if tokens > 0:
                print("That's the spirit! ")
            return bottle_number
        print("What do you mean!? ")
        tokens += 1

def sing(input_number):
    """
    WITH A WHILE_LOOP:
    this function takes an argument specifying how many bottles of beer to start with, 
    and then outputs the lyrics to the song, starting from that number of bottles.
    """
    verse_num = input_number # I think a reverse accumulator counts as an accumulator? A decumulator?
    bottle_number = verse_num
    while verse_num > 0:
        if verse_num == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        elif verse_num == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.")
        elif verse_num > 2:
            print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
            print(f"Take one down, pass it around, {bottle_number - 1} bottles of beer on the wall.")
        verse_num -= 1
        bottle_number = verse_num

def sing_alt(input_number):
    """
    I also made an alternative sing() function, that uses an "accumulating" accumulator.
    """
    sung_verses = 0
    bottle_number = input_number
    new_bottle_number = bottle_number - 1
    while sung_verses != input_number:
        if sung_verses == input_number - 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        elif sung_verses == input_number - 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.")
        elif sung_verses <= input_number - 2:
            print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
            print(f"Take one down, pass it around, {bottle_number - 1} bottles of beer on the wall.")
        sung_verses += 1
        bottle_number = new_bottle_number
