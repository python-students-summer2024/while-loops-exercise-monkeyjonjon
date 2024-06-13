def get_starting_number():
    """
    WITH A FOR_LOOP:
    this function asks the user how many bottles of beer on the wall they want to start singing with, 
    e.g. "How many bottles of beer on the wall?" 
    The function asks this question as many times as necessary until the user enters a valid response, 
    which is considered to be any integer 1 or greater. 
    The function then returns the integer equivalent of the value the user entered.
    (Added a token for fun)
    """
    chances = 1 # You get one chance!
    tokens = 0
    chance_list = list(range(chances))
    for chance in chance_list:
        bottle_number = input("How many bottles of beer are on the wall? ")
        if bottle_number.isdigit() and int(bottle_number) >= 1:
            bottle_number = int(bottle_number)
            chances = 0 
            if tokens > 0:
                print("That's the spirit! ")
            return bottle_number
        print("What do you mean!? ")
        tokens += 1
        chance_list.append(0) # Just kidding you can have more.

def sing(input_number):
    """
    WITH A FOR_LOOP:
    this function takes an argument specifying how many bottles of beer to start with, 
    and then outputs the lyrics to the song, starting from that number of bottles.
    """
    # soooo it turns out I don't need to write bottle_number -= 1 at the end of each loop if I write for bottle_number. good to know
    for bottle_number in range(input_number, 0, -1):
        new_bottle_number = bottle_number - 1
        if bottle_number == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        elif bottle_number == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.")
        elif bottle_number > 2:
            print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.")
            print(f"Take one down, pass it around, {new_bottle_number} bottles of beer on the wall.")
            

