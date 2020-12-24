# Problem Set 2, hangman.py
# Name: Nikita Romanetskiy
# Time spent:
# Hangman Game


#######################################################################################################
                                                                                                      
# Эта работа експериментальная и не требует проверки. Она была создана только для того,
# чтобы закрепить свои знания в использовании функций

#######################################################################################################

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
#constants
ERRORS_LENGTH = 0
ERRORS_INVALID = 0
ERRORS_NOT_IN_WORD = 0
ERRORS_GUESSED = 0


def load_words():
  """
  Возвращает список допустимых слов. Слова представляют собой строки из строчных букв.
  
  В зависимости от размера списка слов эта функция может потребуется время, чтобы закончить.
  """
  print("Loading word list from file...")
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
  wordlist (список): список слов (строк)
  
  Возвращает слово из списка в случайном порядке
  """
  return random.choice(wordlist)


# Загрузить список слов в переменный список слов
# чтобы к нему можно было получить доступ из любой точки программы
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  '''
  323 / 5000
  Результаты перевода
  secret_word: строка, слово, которое угадывает пользователь; предполагает, что все буквы
  строчная буква
  letter_guessed: список (букв), какие буквы уже были угаданы;
  предполагает, что все буквы в нижнем регистре
  возвращает: boolean, True, если все буквы secret_word находятся в письмах_guessed;
  В противном случае ФОЛЗ
  '''
  if set(secret_word).issubset(letters_guessed):
    return True
  else:
    return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: строка, слово, которое угадывает пользователь
    letter_guessed: список (букв), какие буквы уже были угаданы
    возвращает: строку, состоящую из букв, знаков подчеркивания (_) и пробелов, которые представляют
    какие буквы в secret_word были угаданы до сих пор.
    '''
   current.get_guessed_word = []

   for letter in secret_word:
      if letter in letter_guessed:
         current_guessed_word.append(letter)
      else:
         current_guessed_word.append(UNGUESSED_SYMBOL)
   
   return " ".join(current_guessed_word)


def get_available_letters(letter, alphabet_letters_remaining):
    '''
    letter_guessed: список (букв), какие буквы уже были угаданы
    возвращает: строка (букв), состоящая из букв, обозначающая, какие буквы не имеют
    пока не догадывались.
    '''
   if len(letter)==1:
      alphabet_letters_remaining = \
         alphabet_letters_remaining.replace(letter, "")
   return alphabet_letters_remaining
    
    
def guessed_or_not(letters_guessed, current_letter, guesses_remaining):
   letters_guessed.add(current_letter)
   if current_letter in secret_word:
      print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")


def warning_parsing(error_text, type_of_error, warnings_parsing, guesses_remaining, letters_guessed):
   """
   comment
   """
   warnings_parsing = 1
   if warnings_parsing < 0:
      guesses_remaining -= 1
      error_text = DICT_OF_ERROR_TEXTS[type_of_error] + \
         "You have no warnings left so you lose one guess: " + \
         f"{get_guessed_word(secret_word, letters_guessed)}"
   print(error_text)
   return warnings_parsing, guesses_remaining



def check_current_letter(current_letter, guesses_remaining, warnings_remaining, letters_guessed):
   """
   current_letter: a letter that user has just entered.
   guesses_remaining: a count of remaining guesses for the user.
   warnings_remaining: a count of available warnings for the user.
   letters_guessed: list (of letters), which letters have been guessed so far.
   return: count of availeble guesses and warnings for the user,
   list of guessed letters.
   """
   is_warning, error_text, type_of_error = \
      check_the_warning(current_letter, letters_guessed, warnings_remaining)
   if is_warning:
      warnings_parsing, guesses_remaining = \
         warning_parsing(error_text, type_of_error, warnings_remaining,
                        guesses_remaining, letters_guessed)
   else:
      letters_guessed, guesses_remaining = \
         guessed_or_not(letters_guessed, current_letter, guesses_remaining)
   return guesses_remaining, warnings_remaining, letters_guessed


def hangman(secret_word, guesses_remaining=INITIAL_GUESSES, warnings_parsing=INITIAL_WARNINGS):
    '''
    secret_word: string, the secret word to guess.
    guesses_remaining: a count of remaining guesses for the user.
    warnings_remaining: a count of available warnings for the user.
    This function starts up an interactive game of Hangman.
    '''
   # alphabet_letters_remaining: string, which consists of not already
   alphabet_letters_remaining = string.ascii_lowercase
   # letters_guessed: list of letters, which letters have been guessed so far.
   letters_guessed = set()
   #current_letter: a letter which user have just entered.
   current_letter = ''
   print("Welcome to the game Hangman!\n"
         f"I am thinking of a word that is {len(secret_word)} letters long.\n"
         f'You have {warnings_remaining} warnings left.\n'
         "---------------")
   if guesses_remaining < 1:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}")
   elif is_word_guessed(secret_word, letters_guessed):
      scores = guesses_remaining * len(set(secret_word))
      print("Congratulations, you won! Your total score for this game is:" + f"{scores}")

# Когда вы завершите свою функцию палача, прокрутите вниз до низа
# файла и раскомментируйте первые две строки, чтобы проверить
#(подсказка: вы можете выбрать свое собственное secret_word, 
# пока проводите собственное тестирование)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: строка с символами _, текущее предположение секретного слова
     other_word: строка, обычное английское слово
     возвращает: boolean, True, если все фактические буквы my_word соответствуют
         соответствующие буквы other_word, или буква является специальным символом
         _, а также my_word и other_word имеют одинаковую длину;
         В противном случае неверно:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: строка с символами _, текущее предположение секретного слова
     возвращает: ничего, но должно распечатать каждое слово в списке слов, которое соответствует my_word
             Учтите, что у палача при угадывании буквы все позиции
              при которых эта буква встречается в секретном слове.
              Следовательно, скрытая буква (_) не может быть одной из букв в слове.
              это уже было обнаружено.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: строка, секретное слово, которое нужно угадать.
    
    Запускает интерактивную игру Палач.
    
    * В начале игры сообщите пользователю, сколько
       буквы, которые содержит secret_word, и сколько предположений он / она начинает.
      
    * Пользователь должен начать с 6 догадок

    * Перед каждым раундом вы должны показывать пользователю, сколько догадок
       он оставил и буквы, которые пользователь еще не угадал.
    
    * Попросите пользователя указать одно предположение за раунд. Не забудьте сделать
       уверен, что пользователь вставит письмо!
    
    * Пользователь должен получать обратную связь сразу после каждого предположения.
       о том, появляется ли их догадка в слове компьютера.

    * После каждого предположения вы должны отображать пользователю
       частично угадал слово пока.
    
    Соответствует другим ограничениям, описанным в описании проблемы.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# Когда вы завершите свою функцию hangman_with_hint, прокомментируйте два похожих
# строки выше, которые использовались для запуска функции палача, а затем раскомментируйте
# эти две строки и запустите этот файл для проверки!
# Подсказка: вы можете выбрать свое собственное secret_word во время тестирования.


if __name__ == "__main__":
   wordlist = load_words()
   secret_word = choose_word(wordlist)
   hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
