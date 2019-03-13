"""CS50x Problem Set 6 - Bleep.py

Implement a program that censors messages that contain words that appear on a list of supplied "banned words."

Adam DeCaria

"""

import sys
from cs50 import get_string


def main():

    # check for proper input from the user
    if len(sys.argv) != 2:
        sys.exit("Please include a dictionary file of words to ban.")

    dictionary = sys.argv[1]  # dictionary file for banned words

    banned = set()  # set() of banned words from dictionary

    # import the list of banned words from the file into a set

    file = open(dictionary, "r")
    for line in file:
        banned.add(line.rstrip('\n'))
    file.close()

    # prompt user for message

    message = get_string("Please enter a message: ")
    tokens = message.split()

    # check for uppercase version of banned words
    banned_upper = set()
    for word in banned:
        banned_upper.add(word.upper())

    print(banned_upper)

    # check for banned words and replace with * (one * for each letter in banned word)

    for token in tokens:
        if token in banned:
            index = tokens.index(token)
            ban = tokens[index]
            cover = ""
            for _ in range(len(ban)):
                cover = cover + "*"
            tokens[index] = cover

    # check for uppercase version of banned words

    for token in tokens:
        if token in banned_upper:
            index = tokens.index(token)
            ban = tokens[index]
            cover = ""
            for _ in range(len(ban)):
                cover = cover + "*"
            tokens[index] = cover

    # create the output message and print

    output_message = ""

    for item in tokens:
        output_message = output_message + " " + item

    print(output_message)


if __name__ == "__main__":
    main()
