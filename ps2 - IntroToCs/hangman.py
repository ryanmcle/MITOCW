# Problem Set 2, hangman.py
# Name: Ryan Mclellan
# Collaborators: N/A
# Time spent: 1.5h

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    built_string = ""

    for char in secret_word:
        if char in letters_guessed:
            built_string += char
        else:
            built_string += "_"
    return built_string
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return sorted(tuple(letters_guessed))
    

def hangman(secret_word):
	print("Welcome to hangman")
	print(f"I am thinking of a word that is {len(secret_word)} letters long.")
	print("----------\nYou have 6 guesses left.")
	print("You currently have a-z letters remaining.")
    
	warnings = 3
	guesses = 6
	letters_guessed = []
	vowels = ["a", "e", "i", "o", "u"]
      
	while guesses > 0:
		print("----------")
		while True:
			guess = input("Guess here: ").lower()
			if len(guess) == 1 and guess.isalpha():
				break
			else:
				print("Please enter 1 letter")
				warnings -= 1
				print(f"You have {warnings} remaining")
				if warnings == 0:
					guesses -= 1
					print(f"I warned you, you lose a guess, guesses remaining {guesses}")
					if guesses == 0:
						sys.exit("Next time enter letters.")
            

		letters_guessed = sorted(set(letters_guessed + [guess]))
		if is_word_guessed(secret_word, letters_guessed):
			sys.exit(f"You win! The word was {secret_word}")
		else:
			if guess in secret_word:
				print(get_guessed_word(secret_word, letters_guessed))
				print(f"Letters guessed: {get_available_letters(letters_guessed)}")
			else:
				if guess in vowels:
					guesses -= 2
				elif guesses == 0:
					sys.exit(f"You lose!\nThe word was {secret_word}")
				else:
					guesses -= 1
				print(f"The word is still {get_guessed_word(secret_word, letters_guessed)}")
				print(f"You have {guesses} lives remaining.")
				print(f"Letters guessed: {get_available_letters(letters_guessed)}")


def match_with_gaps(my_word, other_word):
	for i in range(len(my_word)):
		if my_word[i] == "_":
			continue
		elif my_word[i] != other_word[i]:
			return False
	return True



def show_possible_matches(my_word):
	counter = 0
	print("Possible matches: ")
	for word in wordlist:
		if len(word) != len(my_word):
			continue
		elif match_with_gaps(my_word, word):
			print(f"{word} ", end="")
			counter += 1
			if counter % 10 == 0:
				print()
	if counter == 0:
		print("No matches found.")
	
	print()


def hangman_with_hints(secret_word):    
	print("Welcome to hangman")
	print(f"I am thinking of a word that is {len(secret_word)} letters long.")
	print("----------\nYou have 6 guesses left.")
	print("You currently have a-z letters remaining.")
    
	warnings = 3
	guesses = 6
	letters_guessed = []
	vowels = ["a", "e", "i", "o", "u"]
      
	while guesses > 0:
		print("----------")
		while True:
			guess = input("Guess here: ").lower()
			if guess == "*":
				show_possible_matches(get_guessed_word(secret_word, letters_guessed))
				break
			elif len(guess) == 1 and guess.isalpha():
				break
			else:
				print("Please enter 1 letter")
				warnings -= 1
				print(f"You have {warnings} remaining")
				if warnings == 0:
					guesses -= 1
					print(f"I warned you, you lose a guess, guesses remaining {guesses}")
					if guesses == 0:
						sys.exit("Next time enter letters.")
            

		letters_guessed = sorted(set(letters_guessed + [guess]))
		if is_word_guessed(secret_word, letters_guessed):
			sys.exit(f"You win! The word was {secret_word}")
		else:
			if guess in secret_word:
				print(get_guessed_word(secret_word, letters_guessed))
				print(f"Letters guessed: {get_available_letters(letters_guessed)}")
			else:
				if guess in vowels:
					guesses -= 2
				elif guesses == 0:
					sys.exit(f"You lose!\nThe word was {secret_word}")
				else:
					guesses -= 1
				print(f"The word is still {get_guessed_word(secret_word, letters_guessed)}")
				print(f"You have {guesses} lives remaining.")
				print(f"Letters guessed: {get_available_letters(letters_guessed)}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
