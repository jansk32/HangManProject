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

def print_board(category, arr, wrong):
    print("Your Category: "+ category)
    print(" ".join(arr))
    print("Guessed wrong letters:", wrong)

def updateBoard(letter, word, board):
        for i in range(0, len(word)):
            if(letter == word[i]):
                board[i] = letter

def hangMan(mistake):
    ## using a formatter; width = 10
    
    return 0
    

def main():
    ## mistakes
    mistake = []

    ## Generate list
    listing = developList()

    ##Pick random key
    pickedInd = random.randint(0,2)

    ##Category
    category = list(listing.keys())[pickedInd]

    ## pick word
    wordInd = random.randint(0,len(list(listing[category])))
    word = listing[category][wordInd].upper()

    ##convert to empty strings
    display = formBoard(word)

    while("".join(display) != word):
        ## print a display
        print_board(category,display, mistake)

        playerInput = input("Pick a letter: ")
        playerInput = playerInput.upper()

        ## update the board
        if playerInput in word:
            updateBoard(playerInput, word, display)
        else:
            mistake.append(playerInput)

        if len(mistake) == 5:
            print("Game Over.")
            print("The word was:",word)
            break
        print_board(category,display, mistake)



if __name__ == "__main__":
    main()