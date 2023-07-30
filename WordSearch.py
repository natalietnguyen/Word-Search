#  File: WordSearch.py

#  Description: A program to search for a list of words within a grid of letters

#  Student Name: Natalie Nguyen

#  Student UT EID: ntn687

#  Partner Name: Ethan Harris

#  Partner UT EID: ejh2947

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 01/17/2023

#  Date Last Modified: 01/20/2023

import sys

# function to test other functions
def test_cases ():
    grid = [['E', 'R', 'T', 'B', 'O'],
            ['R', 'T', 'Q', 'U', 'B'],
            ['I', 'U', 'H', 'S', 'O'],
            ['C', 'I', 'B', 'A', 'Y'],
            ['E', 'J', 'J', 'D', 'N']]

    words = ['ICE', 'BOY', 'BUS', 'RUB', 'ETHAN']

    # test get_up_left()
    assert get_up_left((2, 2), grid) == (1, 1)
    assert get_up_left((1, 0), grid) == None

    # test get_up()
    assert get_up((2, 2), grid) == (1, 2)
    assert get_up((0, 2), grid) == None

    # test get_up_right()
    assert get_up_right((2,2), grid) == (1, 3)
    assert get_up_right((0, 0), grid) == None

    # test get_right()
    assert get_right((2, 2), grid) == (2, 3)
    assert get_right((4, 4), grid) == None

    # test get_left()
    assert get_left((2, 2), grid) == (2, 1)
    assert get_left((2, 0), grid) == None

    # test get_down_left()
    assert get_down_left((2, 2), grid) == (3, 1)
    assert get_down_left((4, 0), grid) == None

    # test get_down_right
    assert get_down_right((2, 2), grid) == (3, 3)
    assert get_down_right((3, 4), grid) == None

    # test get_down()
    assert get_down((2, 2), grid) == (3, 2)
    assert get_down((4, 0), grid) == None

    # test check_word()
    assert check_word(words[2], (0, 3), grid) == True
    assert check_word(words[1], (3, 2), grid) == None

    # test find_word()
    assert find_word(grid, words[4]) == (1, 1)
    assert find_word(grid, 'TUB') == (0, 0)
    assert find_word(grid, words[3]) == (2, 1)

    return "all test cases passed"



# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    # reads the number of lines of the word grid
    number_of_lines = int(sys.stdin.readline())
    
    # creates the grid array
    grid = []

    # reads the blank line
    line = sys.stdin.readline()

    # iterate across the number of lines
    for i in range(number_of_lines):
        # reads line and gets rid of whitespace
        line = sys.stdin.readline().replace(" ", "").strip()

        # turns line into a list
        line = list(line)

        # add line to array
        grid.append(line)

    # creates list of words to find
    words = []

    # reads the blank line
    line = sys.stdin.readline()

    # reads the number of words to find
    number_of_words = int(sys.stdin.readline())

    # iterates across the number of words
    for i in range(number_of_words):

        # reads the word
        line = sys.stdin.readline().strip()

        # adds word to list
        words.append(line)

    return grid, words


# Input: a tuple of the location of the letter given, 
#        a string of the letter we are looking for, 
#        a 2-D list representing the grid of letters
# Output: returns a tuple of the location of the adjacent letter 
#         or returns None if location is valid

# gets location of top left letter in reference to the input location
def get_up_left (location, grid):

    # check if location is valid
    if (location[0] == 0) or (location[1] == 0):
        return None

    # gets new location
    new_row = location[0] - 1
    new_column = location[1] - 1

    return (new_row, new_column)

# gets location of top letter in reference to the input location
def get_up (location, grid):

    # check if location is valid
    if (location[0] == 0):
        return None

    # gets new location
    new_row = location[0] - 1
    new_column = location[1]

    return (new_row, new_column)

# gets location of top right letter in reference to the input location
def get_up_right (location, grid):

    # check if location is valid
    if (location[0] == 0) or (location[1] == len(grid) - 1):
        return None

    # gets new location
    new_row = location[0] - 1
    new_column = location[1] + 1

    return (new_row, new_column)

# gets location of right letter in reference to the input location
def get_right (location, grid):

    # check if location is valid
    if (location[1] == len(grid) - 1):
        return None

    # gets new location
    new_row = location[0]
    new_column = location[1] + 1

    return (new_row, new_column)

# gets location of bottom right letter in reference to the input location
def get_down_right (location, grid):

    # check if location is valid
    if (location[0] == len(grid) - 1) or (location[1] == len(grid) - 1):
        return None

    # gets new location
    new_row = location[0] + 1
    new_column = location[1] + 1

    return (new_row, new_column)

# gets location of bottom letter in reference to the input location
def get_down (location, grid):

    # check if location is valid
    if (location[0] == len(grid) - 1):
        return None

    # gets new location
    new_row = location[0] + 1
    new_column = location[1]

    return (new_row, new_column)

# gets location of bottom left letter in reference to the input location
def get_down_left (location, grid):

    # check if location is valid
    if (location[0] == len(grid) - 1) or (location[1] == 0):
        return None

    # gets new location
    new_row = location[0] + 1
    new_column = location[1] - 1

    return (new_row, new_column)

# gets location of left letter in reference to the input location
def get_left (location, grid):

    # check if location is valid
    if (location[1] == 0):
        return None

    # gets new location
    new_row = location[0]
    new_column = location[1] - 1

    return (new_row, new_column)

def check_word (word, location, grid):

    # initialize skip variable - skips return True value if word is not found
    skip = False

    # test direction
    if get_up_left(location, grid) != None:

        # sets new location
        new_location = get_up_left(location, grid)
        
        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_up_left(new_location, grid)

                # exits loop and sets skip to True
                else:
                    skip = True
                    break

            # exits loop and sets skip to True
            else:
                    skip = True
                    break

        # checks if word is found
        if skip != True:
            # word is found
            return True

        # resets skip to False
        skip = False

    # test direction
    if get_up(location, grid) != None:

        # sets new location
        new_location = get_up(location, grid)

        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_up(new_location, grid)

                # exits loop and sets skip to True
                else:
                    skip = True
                    break

            # exits loop and sets skip to True
            else:
                    skip = True
                    break

        # checks if word is found
        if skip != True:
            # word is found
            return True

        # resets skip to False
        skip = False

    # test direction
    if get_up_right(location, grid) != None:

        # sets new location
        new_location = get_up_right(location, grid)

        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_up_right(new_location, grid)
                
                # exits loop and sets skip to True
                else:
                    skip = True
                    break

            # exits loop and sets skip to True
            else:
                    skip = True
                    break
        
        # checks if word is found
        if skip != True:
            # word is found
            return True

        # resets skip to False
        skip = False

    # test direction
    if get_right(location, grid) != None:

        # sets new location
        new_location = get_right(location, grid)

        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_right(new_location, grid)

                # exits loop and sets skip to True
                else:
                    skip = True
                    break

            # exits loop and sets skip to True
            else:
                    skip = True
                    break

        # checks if word is found
        if skip != True:
            # word is found
            return True

         # resets skip to False
        skip = False

    # test direction
    if get_down_right(location, grid) != None:

        # sets new location
        new_location = get_down_right(location, grid)

        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_down_right(new_location, grid)
                
                # exits loop and sets skip to True
                else:
                    skip = True
                    break

            # exits loop and sets skip to True
            else:
                    skip = True
                    break

        # checks if word is found
        if skip != True:
            # word is found
            return True

        # resets skip to False
        skip = False

    # test direction
    if get_down(location, grid) != None:

        # sets new location
        new_location = get_down(location, grid)

        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_down(new_location, grid)

                # exits loop and sets skip to True
                else:
                    skip = True
                    break

            # exits loop and sets skip to True
            else:
                    skip = True
                    break

        # checks if word is found
        if skip != True:
            # word is found
            return True

        # resets skip to False
        skip = False

    # test direction
    if get_down_left(location, grid) != None:

        # sets new location
        new_location = get_down_left(location, grid)

        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_down_left(new_location, grid)

                # exits loop and sets skip to True
                else:
                    skip = True
                    break

            # exits loop and sets skip to True
            else:
                    skip = True
                    break
        
         # checks if word is found
        if skip != True:
            # word is found
            return True

        # resets skip to False
        skip = False

    # test direction
    if get_left(location, grid) != None:

        # sets new location
        new_location = get_left(location, grid)

        # iterate across the word
        for i in range(1, len(word)):

            # checks if new location is found
            if new_location != None:

                # checks if letter in new location matches letter in word
                if word[i] == grid[new_location[0]][new_location[1]]:

                    # sets new location
                    new_location = get_left(new_location, grid)
                
                # exits loop and sets skip to True
                else:
                    skip = True
                    break
            
            # exits loop and sets skip to True
            else:
                    skip = True
                    break

        # checks if word is found
        if skip != True:
            # word is found
            return True

        # resets skip to False
        skip = False

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

def find_word (grid, word):

    # iterate across grid
    for x_loc, row in enumerate(grid):
        for y_loc, column in enumerate(row):

            # checks if letter in grid matches first letter of word
            if column == word[0]:

                # if word is a single letter
                if len(word) == 1:
                    return (x_loc + 1, y_loc + 1)

                # check rest of word
                if check_word(word, (x_loc, y_loc), grid) == True:

                    # returns location of first letter
                    return (x_loc + 1, y_loc + 1)
    
    # returns (0,0) if word is not in grid
    return (0,0)


def main():
    # test all functions
    # test_cases()

    # read the input file from stdin
    word_grid, word_list = read_input()

    # find each word and print its location
    for word in word_list:
        location = find_word (word_grid, word)
        print (word + ": " + str(location))

if __name__ == "__main__":
    main()
