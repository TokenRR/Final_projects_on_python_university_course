# Problem Set 2, hangman.py                            !
# Name: Nikita Romanetskiy                             !
# Group: KM-01                                         !
# Hangman Game                                         !
# Time spent: Did little by little throughout the week !
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
import string
import time # To delay the output of the program code


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    time.sleep(3)
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: список строк
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Загрузить список слов в переменный список слов
# чтобы к нему можно было получить доступ из любой точки программы
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if set(secret_word).issubset(letters_guessed):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    Secret_list = [secret_word[i:i + 1] for i in range(0, len(secret_word))]
    compared_list = []
    for i in secret_word:
        if i in letters_guessed:
            compared_list.append(i)
        elif i not in letters_guessed:
            compared_list.append("_ ")
    compared_word = ""
    return compared_word.join(compared_list)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet_list = [string.ascii_lowercase[i:i + 1] for i in range(0, len(string.ascii_lowercase))]
    compared_list = [i for i in alphabet_list if i not in letters_guessed]
    compared_alphabet = ""
    return compared_alphabet.join(compared_list)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    Secret_list = [secret_word[i:i + 1] for i in range(0, len(secret_word))]
    tries = 6
    warnings = 3
    letters_guessed_list = []
    letters = []
    text = ""
    vowels_list = ["a", "e", "i", "o", "u"]
    check = "_ " * len(secret_word)
    print("Welcome to the game Hangman!")
    time.sleep(1)
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")
    IsRunning = True
    while IsRunning:
        print("-------------------------")
        print("You have", tries, "guesses left.")
        print("Available letters:", get_available_letters(letters))
        letters_guessed = str(input("Please guess a letter: ")).lower()
        if len(letters_guessed) == 1:
            if letters_guessed in letters:
                if warnings > 0:
                    warnings -= 1
                else:
                    warnings = "no"
                    text = " so you lose one guess"
                    tries -= 1
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left" + text + ":",
                      check)
            elif letters_guessed not in string.ascii_lowercase:
                if warnings > 0:
                    warnings -= 1
                else:
                    warnings = "no"
                    text = " so you lose one guess"
                    tries -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:", check)
            elif letters_guessed in Secret_list:
                letters_guessed_list.append(letters_guessed)
                check = get_guessed_word(secret_word, letters_guessed_list)
                print("Good guess:", check)
            elif letters_guessed not in Secret_list:
                if letters_guessed in vowels_list:
                    tries -= 2
                else:
                    tries -= 1
                check = get_guessed_word(secret_word, letters_guessed_list)
                print("Oops! That letter is not in my word:", check)
            letters.append(letters_guessed)
        elif len(letters_guessed) < 1:
            if warnings > 0:
                warnings -= 1
            else:
                warnings = "no"
                text = " so you lose one guess"
                tries -= 1
            print("Oops! Don't leave a blank line. You have", warnings, "warnings left:", check)
        else:
            if warnings > 0:
                warnings -= 1
            else:
                warnings = "no"
                text = " so you lose one guess"
                tries -= 1
            print("Oops! Don't enter more than one symbol. You have", warnings, "warnings left:", check)
        print(display_hangman(tries))
        if tries == 0:
            print("-------------------------")
            print('Sorry, you ran out of guesses. The word was "' + secret_word + '".')
            IsRunning = False
        if secret_word == check:
            score = tries * len(set(secret_word))
            print("-------------------------")
            print("Congratulations, you won! Your total score for this game is:", score)
            IsRunning = False


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
            corresponding letters of other_word, or the letter is the special symbol
            _ , and my_word and other_word are of the same length; 
    False otherwise: 
    '''
    my_word = "".join(my_word.split())
    if len(my_word) == len(other_word):
        i = 0
        while i < len(my_word):
            if my_word[i] == "_":
                i += 1
            else:
                if my_word[i] != other_word[i]:
                    return False
                else:
                    i += 1
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matches = [word for word in wordlist if match_with_gaps(my_word, word) == True]
    if not matches:
        print("No matches found.\n")
    else:
        print("Possible word matches are: " + ", ".join(matches), end="." + "\n")
    return


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    Secret_list = [secret_word[i:i + 1] for i in range(0, len(secret_word))]
    tries = 6
    warnings = 3
    letters_guessed_list = []
    letters = []
    text = ""
    vowels_list = ["e", "u", "i", "o", "a"]
    check = "_ " * len(secret_word)
    print("Welcome to the game Hangman!")
    time.sleep(1)
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")
    time.sleep(1)
    print('You have also 1 hint. Enter "*" to use it.')
    IsRunning = True
    while IsRunning:
        print("-------------------------")
        print("You have", tries, "guesses left.")
        print("Available letters:", get_available_letters(letters))
        letters_guessed = str(input("Please guess a letter: ")).lower()
        if len(letters_guessed) == 1:
            if letters_guessed in letters:
                if warnings > 0:
                    warnings -= 1
                else:
                    warnings = "no"
                    text = " so you lose one guess"
                    tries -= 1
                if letters_guessed == "*":
                    print("Oops! You've already used your hint. You have", warnings, "warnings left" + text + ":",
                          check)
                else:
                    print("Oops! You've already guessed that letter. You have", warnings, "warnings left" + text + ":",
                          check)
            elif letters_guessed == "*":
                show_possible_matches(check)
            elif letters_guessed not in string.ascii_lowercase:
                if warnings > 0:
                    warnings -= 1
                else:
                    warnings = "no"
                    text = " so you lose one guess"
                    tries -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:", check)
            elif letters_guessed in Secret_list:
                letters_guessed_list.append(letters_guessed)
                check = get_guessed_word(secret_word, letters_guessed_list)
                print("Good guess:", check)
            elif letters_guessed not in Secret_list:
                if letters_guessed in vowels_list:
                    tries -= 2
                else:
                    tries -= 1
                check = get_guessed_word(secret_word, letters_guessed_list)
                print("Oops! That letter is not in my word:", check)
            letters.append(letters_guessed)
        elif len(letters_guessed) < 1:
            if warnings > 0:
                warnings -= 1
            else:
                warnings = 0
                tries -= 1
            print("Oops! Don't leave a blank line. You have", warnings, "warnings left:", check)
        else:
            if warnings > 0:
                warnings -= 1
            else:
                warnings = 0
                tries -= 1
            print("Oops! Don't enter more than one symbol. You have", warnings, "warnings left:", check)
        print(display_hangman(tries))
        if tries == 0:
            print("-------------------------")
            print('Sorry, you ran out of guesses. The word was "' + secret_word + '".')
            IsRunning = False
        if secret_word == check:
            score = tries * len(set(secret_word))
            print("-------------------------")
            print("Congratulations, you won! Your total score for this game is:", score)
            IsRunning = False


def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]


def main():
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    while input("Again? (Y/N) ").upper() == "Y":
        secret_word = choose_word(wordlist)
        hangman_with_hints(secret_word)

if __name__ == "__main__":
    

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    #####################################################################
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
    #####################################################################
    main() #program start function