import random

def wordGen():
  with open('\wlist_match6.txt') as wordList:
    #select and scramble word
    global x, word
    word = [line[0:-1] for line in wordList if len(line) > 5]
    scrambledWord = random.choice(word)
    print(scrambledWord)    #confirmation print
    random.shuffle(x := list(scrambledWord))
    print("".join(x)) #

def guessWord():
  print("Welcome to the guessing game.  A word has been selected from our master list of", len(word), "items.")
  print("You will have three tries to descramble the word.  Good Luck")
  
  print("".join(x))

wordGen()
guessWord()