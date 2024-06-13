def get_starting_number():
    """
    WITH A WHILE_LOOP_FLAG:
    this function asks the user how many bottles of beer on the wall they want to start singing with, 
    e.g. "How many bottles of beer on the wall?" 
    The function asks this question as many times as necessary until the user enters a valid response, 
    which is considered to be any integer 1 or greater. 
    The function then returns the integer equivalent of the value the user entered.
    (Added a token for fun)
    """
    correct = False # A flag
    token = False
    while not correct:
        bottle_number = input("How many bottles of beer are on the wall? ")
        if bottle_number.isdigit() and int(bottle_number) >= 1:
            bottle_number = int(bottle_number)
            correct = True # Flip the flag!
            if token == False:
                print("That's the spirit! ")
            return bottle_number
        print("What do you mean!? ")
        token = False

def sing(input_number):
    """
    WITH A WHILE_LOOP_FLAG:
    this function takes an argument specifying how many bottles of beer to start with, 
    and then outputs the lyrics to the song, starting from that number of bottles.
    """
    singing = True
    bottle_number = input_number
    while singing:
        if bottle_number <= 0:
            singing = False # No more bottles? Stop singing
        if bottle_number == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        elif bottle_number == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.")
        elif bottle_number > 2:
            print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
            print(f"Take one down, pass it around, {bottle_number - 1} bottles of beer on the wall.")
        bottle_number -= 1
