import math
import random

def developList():
    listing = {}
    listing['food'] = ['banana', 'apple', 'noodles','salmon','pasta']
    listing['people'] = ["Abraham Lincoln", 'Steve Jobs', 'Larry Page', 'Issac Newton']
    listing['instrument'] = ['guitar', 'piano','flute','cello','violin']
    return listing

def formBoard(word):
    display = []
    for i in range(len(word)):
        if word[i].isspace() :
            display.append(' ')
        else:
            display.append('_')
    return display

def print_board(category, arr):
    print("Your Category: "+ category)
    print(" ".join(arr))
    

def main():
    ## Generate list
    listing = developList()

    ##Pick random key
    pickedInd = random.randint(0,len(listing.keys()))

    ##Category
    category = list(listing.keys())[pickedInd]

    ## pick word
    wordInd = random.randint(0,len(list(listing[category])))
    word = listing[category][wordInd].lower()

    ##convert to empty strings
    display = formBoard(word)

    ## print a display
    print_board(category,display)

    playerInput = input("Pick a letter: ")

    if playerInput in word:
        for i in range(0, len(word)):
            if(playerInput == word[i]):
                display[i] = playerInput

    print_board(category,display)

if __name__ == "__main__":
    main()