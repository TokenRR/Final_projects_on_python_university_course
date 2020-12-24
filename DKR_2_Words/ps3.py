# Name          : Romanetskiy Nikita
# Time spent    : did a little every night, it's hard to say how long it took
# I'm not sure about the whole code, but most of all I doubt about problem 6
import math
import random
import string
import copy


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCORE = 0
WILDCARD = "*"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Возвращает список допустимых слов. Слова представляют собой строки из строчных букв.
    
    В зависимости от размера списка слов эта функция может
    потребуется время, чтобы закончить.
    """
    
    print("\nЗавантаження списку слів з файлу ...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print(len(wordlist), "слів завантажено.\n")
    return wordlist


def get_frequency_dict(sequence):
    """
    Возвращает словарь, в котором ключи являются элементами последовательности
    и значения являются целыми числами, сколько раз
    элемент повторяется в последовательности.

    последовательность: строка или список
    возврат: словарь
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def get_word_score(word, n):
    """
    Возвращает оценку слова. Предполагает, что это слово
    допустимое слово.
    word: string
    n: int >= 0
    returns: int >= 0
    """
    words = word.lower()  #Переводимо у нижній регістр літери
    One = 0
    for key in words:
        One += SCRABBLE_LETTER_VALUES.get(key, 0)  #беремо елемент словника за допомогою ключа
    Two = HAND_SIZE*len(word)-3*(n-len(word))  #Знаходимо очки другої компоненти
    if Two<1:
        Two=1
    return One*Two


def display_hand(hand):
    """
    Отображает буквы в руке.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Следует принтануть что-то вроде:
       a x x l l l e
    Порядок букв не важен.

    hand: dictionary (string -> int)
    """

    print("Поточна рука: ", end="")
    for letter in hand.keys():
        letters = letter.lower()
        for j in range(hand[letter]):
            print(letters, end=' ')      # print all on the same line
    print()                              # print an empty line


def deal_hand(n):
    """
    Возвращает случайную руку, содержащую n строчных букв.
    ceil (n / 3) буквы в руке должны быть гласными (примечание,
    ceil (n / 3) означает наименьшее целое число не менее n / 3).

    Руки представлены в виде словарей. Ключи
    буквы и значения - это количество раз
    конкретная буква повторяется в этой руке.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand[WILDCARD] = 1
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand


def update_hand(hand, word):
    """
    НЕ предполагает, что рука содержит каждую букву слова не менее
    столько раз, сколько буква встречается в слове. Буквы в слове, которые не
    Появление в руке следует игнорировать. Буквы, которые встречаются в слове больше раз
    чем в руке, никогда не должно приводить к отрицательному счету; вместо этого установите
    сосчитайте в возвращенной руке до 0 (или удалите букву из
    словарь, в зависимости от того, как структурирован ваш код).

    Обновляет руку: использует буквы в данном слове
    и возвращает новую руку без этих букв.

    Не имеет побочных эффектов: не видоизменяет руку.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = {}
    word1 = word.lower()
    for letter_in_hand in hand.keys():
        counter = 0
        if letter_in_hand in word1:
            for letter_in_word in word1:
                if letter_in_word == letter_in_hand:
                    counter += 1
        if hand[letter_in_hand] == counter:
            pass
        else:
            new_hand[letter_in_hand] = hand[letter_in_hand] - counter

    return new_hand


def is_valid_word(word, hand, word_list):
    """
    Возвращает True, если слово находится в word_list и полностью
    состоит из букв в руке. В противном случае возвращает False.
    Не изменяет hand или word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    test = True
    word1 = word.lower()
    check_l = []
    hand_letters = [letter for letter in hand.keys()]

    if "*" in word1:
        position = []
        for letter in range(len(word1)):
            if word1[letter] == "*":
                position.append(letter)
        if len(position) >= 2:
            test = False
        else:
            pos = position[0]
            test = False
            for var_vow in VOWELS:
                word2 = word1[:pos] + var_vow + word1[pos + 1:]
                hand1 = copy.deepcopy(hand)
                hand1[var_vow] = hand1.get(var_vow, 0) + 1
                if is_valid_word(word2, hand1, word_list):
                    return True

    if word1 not in word_list:
        test = False

    if test:
        for letter_in_word in word1:
            if letter_in_word not in check_l:
                if letter_in_word in hand_letters:
                    counter = 0
                    for letter in word1:
                        if letter == letter_in_word:
                            counter += 1
                    if hand[letter_in_word] - counter < 0:
                        test = False
                    check_l.append(letter_in_word)
                else:
                    test = False
            if not test:
                break
    return test


def calculate_handlen(hand):
    """ 
    Возвращает длину (количество букв) в текущей руке.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    return sum(hand.values())


def play_hand(hand, word_list):

    """
    Позволяет пользователю разыграть данную руку следующим образом:

    * Показана рука.
    
    * Пользователь может ввести слово.

    * Когда вводится любое слово (действительное или недействительное), используются буквы
      из рук.

    * Недействительное слово отклоняется, и отображается сообщение с вопросом
      пользователь выбирает другое слово.

    * После каждого допустимого слова: отображается оценка этого слова,
      отображаются оставшиеся буквы в руке, и пользователь
      предлагается ввести другое слово.

    * Сумма очков отображается, когда рука заканчивает.

    * Рука заканчивается, когда больше нет неиспользованных букв.
      Пользователь также может закончить игру рукой, введя два
      восклицательный знак (строка '!!') вместо слова.

    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: the total score for the hand
      
    """
    score = 0
    # As long as there are still letters left in the hand:
    while hand != {}:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        word = input("Введіть слово або «!!» щоб вказати, що ви закінчили: ")
        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            print()
            break

            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):
                # Updated total score
                word_score = get_word_score(word, calculate_handlen(hand))
                score += word_score
                # Tell the user how many points the word earned
                print(f"За “{word}” ти отримав(ла) {word_score} балів. Загалом: {score} бала")

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("Це невірне слово. Виберіть інше слово.")
                
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)
            print()
            

    if hand == {}:
        print("закінчилися букви")
    # so tell user the total score
    print(f"Загальний бал за цю руку: {score}")
    # Print hand separator
    print("--------")
    # Return the total score as result of function
    return score


def substitute_hand(hand, letter):
    """ 
    Разрешить пользователю заменять все копии одной буквы в руке (выбранной пользователем)
    с новой буквой, выбранной случайным образом из ГЛАВНЫХ и СОГЛАСНЫХ. Новое письмо
    должно отличаться от выбора пользователя и не должно быть ни одной из букв
    уже в руке.

    Если пользователь предоставляет письмо, которого нет в руке, рука должна быть такой же.

    Не имеет побочных эффектов: рука не мутирует.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_letter = letter
    while new_letter in [letters for letters in hand.keys()]:
        new_letter = random.choice(VOWELS + CONSONANTS)
    hand[new_letter] = hand[letter]
    del hand[letter]
    return hand
       
    
def play_game(word_list):
    """
    Разрешить пользователю разыграть серию рук

    *Просит пользователя ввести общее количество рук

    *Суммирует счет для каждой руки в общий счет для
      вся серия
 
    *Для каждой руки перед игрой спросите пользователя, хотят ли они заменить
      одно письмо за другим. Если пользователь вводит «да», попросите его ввести
      желаемое письмо. Это можно сделать только один раз за игру. Однажды
      используется опция замены, пользователя не следует спрашивать, хотят ли они
      заменить буквы в будущем.

    *Для каждой руки спросите пользователя, не хотят ли он переиграть руку.
      Если пользователь вводит «да», он повторяет раздачу и сохраняет
      лучший из двух очков для этой руки. Это можно сделать только один раз
      во время игры. После использования опции воспроизведения пользователь не должен
      спросить, хотят ли они переиграть будущие руки. Воспроизведение руки делает
      не засчитывается как одна из общего количества рук, которые пользователь изначально
      хотел поиграть.

            *Примечание: если вы переиграете руку, у вас не будет возможности заменить
                    письмо - вы должны разыграть ту руку, которая у вас только что была.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    global SCORE
    run1 = True
    while run1:
        try:
            HANDS = input('\nВведіть загальну кількість рук: ')
            HANDS = int(HANDS)
            assert 1 <= HANDS
            run1 = False
        except ValueError:
            print('Помилка вводу!')
        except AssertionError:
            print('Ви повинні ввести кількість рук (натуральне число)!')

    hand = deal_hand(HAND_SIZE)
    set_hand = [letter for letter in hand.keys()]

    while HANDS != 0:

        display_hand(hand)
        run2 = True
        while run2:
            choose = str(input('Хочете замінити букву (yes / no)? '))
            if choose == 'yes':
                run3 = True
                while run3:
                    substitute_letter = str(input('Яку букву ви хочете замінити, або «!!» Повернутися назад: '))
                    if substitute_letter == '!!':
                        choose = '!!'
                        run3 = False
                    elif substitute_letter in set_hand and substitute_letter != "*":
                        substitute_hand(hand, substitute_letter)
                        run3 = False
                    else:
                        print("У поточній руці такої літери немає!")

            elif choose == 'no':
                run2 = False
            else:
                print('Будь ласка, введіть «yes» або «no»!')
                continue
            if choose == '!!':
                continue
            run2 = False

        score = play_hand(hand, word_list)
        run4 = False
        while run4:
            choice_3 = str(input('Хотіли б ви переграти руку (yes / no)? '))
            if choice_3 == 'yes':
                score += play_hand(hand, word_list)
            elif choice_3 == 'no':
                run4 = False
            else:
                print('Будь ласка, введіть «yes» або «no»!')
                continue
            run4 = False
        SCORE += score
        hand = deal_hand(HAND_SIZE)
        set_hand = [letter for letter in hand.keys()]
        HANDS -= 1

    print(f'Загальний рахунок за всіма раздачам:    {SCORE}\n')

    if SCORE / HAND_SIZE <= 50:
        print('Ти можеш краще')
    elif SCORE / HAND_SIZE <= 100:
        print('Це хороший результат')
    else:
        print('Ви молодець. Так тримати')

    run = True
    while run:
        choice_2 = str(input('\nБажаєте знову ("yes" або "no") ?: '))
        if choice_2.lower() == 'yes':
            print('\n')
            play_game(word_list)
        elif choice_2.lower() == 'no':
            run = False
        else:
            print('Введіть "yes" або "no"')


if __name__ == '__main__':
    word_list = load_words()
    print("УВАГА ")
    print("\n'*' може замінити одну з цих букв: ", end="")
    for letter in VOWELS:
        letter_up = letter.upper()
        print(letter_up, end=" ", )
    print("\n\nУвага\n\n")
    start_program = True
    while start_program:
        choice_1 = str(input('\nВведіть'
                             '\nPLAY or QUIT'
                             '\n=>'))
        if choice_1.lower() in ['play']:
            play_game(word_list)
            continue
        elif choice_1.lower() in ['quit']:
            print('До побачення! Гарного дня!')
            start_program = False
        else:
            print('Оберіть один з варіантів (play or quit)')