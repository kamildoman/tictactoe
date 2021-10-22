POSSIBLE_NUMBERS = "123456789"
PLAYER_ONE = "o"
PLAYER_TWO = "x"

ai_playground = [" 1 | 2 | 3 ", "-----------", " 4 | 5 | 6 ", "-----------", " 7 | 8 | 9 "]
playground = [" - | - | - ", "-----------", " - | - | - ", "-----------", " - | - | - "]


#checking if there's already o or x on the field. Returns False if the field is already taken.
#if a number is aleady taken it doesn't exist in the ai_playground
#I need to check if the number is between 1 and 9 before calling this function
def repeated_number(number):
    for row in ai_playground:
        for character in row:
            if str(number) == character:
                return False
    return True

#the function checks if there are 3 x or o in the same line
def vertical_win(*args):
    for column_number in args:
        if column_number.count(" x ") == 3 or column_number.count(" o ") == 3:
            return True

#the function returns True if a player has won
def winning_conditions():
    #horizontal
    for i in range(0, 5):
        if playground[i].split("|").count(" x ") == 3 or playground[i].split("|").count(" o ") == 3:
            return True

    #creating columns
    rows_with_values = [0, 2, 4]
    column_one = []
    column_two = []
    column_three = []
    for i in rows_with_values:
        column_one.append(playground[i].split("|")[0])
        column_two.append(playground[i].split("|")[1])
        column_three.append(playground[i].split("|")[2])

    #vertical
    if vertical_win(column_one, column_two, column_three):
        return True
        
    #diagonal, if diagonals have 3 x or o, exclude character "-"
    if column_one[0] == column_two[1] == column_three[2] and column_one[0] != " - ":
        return True
    elif column_one[2] == column_two[1] == column_three[0] and column_one[2] != " - ":
        return True


def restart_game():
    break_or_not = input("Do you want to continue? (y/n): ").lower()
    if break_or_not == "y":
        global ai_playground
        global playground
        global which_player
        ai_playground = [" 1 | 2 | 3 ", "-----------", " 4 | 5 | 6 ", "-----------", " 7 | 8 | 9 "]
        playground = [" - | - | - ", "-----------", " - | - | - ", "-----------", " - | - | - "]
        which_player = 1
        return True
    else:
        return False

#which player plays. If the number is odd the x player plays. If it's even the o player plays
which_player = 1
player_symbol = ""

#the game ui
while True:

    #this one shows which number user has to input
    for line in ai_playground:
        print(line)

    print("\n")
    print("=======================")
    print("\n")

    for line in playground:
        print(line)

    if winning_conditions():
        print("End game!")
        if restart_game():
            continue
        else:
            break

    #if players played 10 times already it means it's a draw
    if which_player == 10:
        print("Draw!")
        if restart_game():
            continue
        else:
            break

    print("\n")

    choice = input("write your number (1 to 9): ") 

    #if it's in the possible numbers
    if choice in POSSIBLE_NUMBERS and choice != "":
        choice = int(choice)
    else:
        print("Please write a number from 1 to 9")
        continue

    #only numbers from 1 to 9 are allowed
    if choice not in range(1, 10):
        print("Invalid number!")

    elif repeated_number(choice):
        print("It's already taken! Please choose a different number")


    #checking which row should be replaced
    else:
        if  0 < choice < 4:
            row_number = 0
        elif 3 < choice < 7:  
            row_number = 2
        elif 6 < choice < 10: 
            row_number = 4

        #choosing which player to play
        if which_player % 2 == 0:
            player_symbol = PLAYER_ONE
        else:
            player_symbol = PLAYER_TWO

        #replace chosen number with "o" or "x" in ai playground 
        replacement = ai_playground[row_number].replace(str(choice), player_symbol)
        ai_playground[row_number] = replacement

        #updates the main playground. Replaces numbers from ai playground to "-"
        for character in replacement:
            if character in POSSIBLE_NUMBERS:
                replacement = replacement.replace(character, "-")
        playground[row_number] = replacement

        #next player's turn
        which_player += 1







