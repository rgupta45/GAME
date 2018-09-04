# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print wordlist
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    total_matched=0
    for letters in letters_guessed:
        if letters in secret_word:
            total_matched = total_matched+1
            if total_matched == len(secret_word):
                return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match_list=[]
    for words in letters_guessed:
        for char in range(0,(len(secret_word))):
            if words == secret_word[char]:
                if len(match_list)!= len(secret_word):
                    match_list.append(words)
                else:
                    match_list[char]= words
            else:
                if len(match_list) != len(secret_word):
                    match_list.append('_ ')
    word = " ".join(str(x) for x in match_list)
    return word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    avail_letter = string.ascii_lowercase
    for letters in letters_guessed:
       avail_letter = avail_letter.replace(letters,'')
    return avail_letter


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Greetings
    print 'Welcome to the game Hangman !'
    print 'I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.'
    print '--------------------------'
    print 'You have six gusess left.'
    print 'You have 3 warnings!'
    print 'Available Letters : ' + string.ascii_lowercase
    print 'Lets start All the best! :-)'
    #print(secret_word, type(secret_word))
    count = len(secret_word)
    guess = 6
    warnings = 3
    words_count = 0
    letters_guessed = []
    while is_word_guessed(secret_word, letters_guessed) == False:
        letters_guessed_string = raw_input('Please guess a letter :')

        if letters_guessed_string in letters_guessed:
            warnings = warnings - 1
            print 'WARNING !! You have already guessed this letter : ' + ' ' + 'Warning left :' + ' ' + str(warnings)
            print '----------------------------------------------------------------'
            if warnings <= 0:
                guess = guess-1
                print "Number of gusses left :"+' '+str(guess)
                print '----------------------------------------------------------------'
                if guess == 0:
                    print 'Game over!! Hard Luck'
                    print 'The word was :'+ secret_word
                    break

        else:
            letters_guessed.append(letters_guessed_string.lower())
            guessed_word_result = get_guessed_word(secret_word, letters_guessed)
            if str.count(guessed_word_result,'_') < count:
                print 'Good Guess '+ guessed_word_result
                print 'Guess left :'+str(guess)
                print'Available letters :' + get_available_letters(letters_guessed)
                print '----------------------------------------------------------------'
                count = str.count(guessed_word_result,'_')
            elif str.count(guessed_word_result,'_')==0:
                 print 'You Nailed it. GOOD JOB... BRAVOO.....!!!!!!'
                 break
            else:
                guess = guess - 1
                if guess == 0:
                    print 'GAME OVER HARD LUCK NEXT TIME!!'
                    print 'The word was :' + secret_word
                    break

                else:
                    print 'Guessed wrong. :' + guessed_word_result
                    print 'Guess left :'+ str(guess)
                    print'Available letters :'+ get_available_letters(letters_guessed)
                    print '----------------------------------------------------------------'



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
