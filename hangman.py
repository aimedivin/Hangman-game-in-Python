#Names For Members 

# IHIMBAZWE Igor      | Reg No: 223006775
# IKIREZI Dina        | Reg No: 223014467
# IRAGENA Aime Divin  | Reg No: 223015506


import random
import string

guess = 6
warning = 3

# Words to be guessed
s_words = ['apple','banana','car','dog','elephant','fish','guitar','house',
        'ice cream','jump','kite','lemon','mountain','notebook','orange','piano',
        'quilt','rainbow','star','tiger','butterfly','candle','diamond','fireworks',
        'giraffe','hen','island','jungle','kangaroo','lighthouse']

#initial assignments 
word = s_words[random.randint(0, 29)]
loop = len(word)
new_word = []
used_letter = []
breaker = 0

# building up dashed(-) word of same length as original 
while loop > 0:
    new_word.append('-')
    loop -= 1

def info_update():
    print("------------------------------------------------------------------------------------------")
    print("|  Word: ","".join(str(i) for i in new_word), )
    print(f"|  Guesses remaing: {guess}")
    print(f"|  Letters not used: {', '.join(i for i in string.ascii_lowercase if i not in used_letter)}")
    print("------------------------------------------------------------------------------------------  \n")

def letter_check_1(chr):
    global warning
    global guess
    if chr in string.ascii_lowercase or chr == ' ' :
        if chr in used_letter:
            if warning == 0:
                guess -= 1
                return False
            warning = warning - 1
            return False
        return True
    
    else:
        print("Invalid Input, please enter a valid letter")
        
        if warning == 0:
            guess -= 1
        else:
            warning -= 1
        return False

def letter_check_2(chr, secret_word):
    global guess
    count = 0
    index_list = []
    if chr in secret_word:
        for i in secret_word:
            if i == chr:
                index_list.append(count)
            count += 1
        return index_list
    else:
        print("Incorrect guess")
        if chr not in "aiueo":
            guess -= 1
        else:
            guess -= 2
            return[]

def guess_check():
    if guess > 0 :
        return True
    return False

def end():
    if not (guess_check()):
        print(f"\n--- You loose!, You've exhausted your guesses\n--- The word was: {word}")
    if breaker == len(new_word):
        score = guess * len(set(new_word))
        print(f"\n--- Congratulations, You Won!\n--- The word: {word}\n--- Your score: {score}")
    

# Starter Message
print("\n--- Hello! Welcome to Hangman Game ---")
print("You know the rules for the game")
print("You got 6 Guesses and 3 Warning at start")
print("You must Enter one character at a time\n\n ------ Let's Start ------\n")


# main loop where all logic rotates

while breaker != len(new_word) :
    if guess_check():
        info_update()
        char = input("Enter any letter for the guess: ")
        if letter_check_1(char):
            index = letter_check_2(char, word)

            if index:
                count = 0
                for i in word:
                    if count in index and char not in used_letter:
                        new_word[count] = char
                        breaker += 1
                        count += 1
                        continue
                    count += 1
        used_letter.append(char)
    else:
        break

end()