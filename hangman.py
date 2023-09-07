import random
import string

guess = 6
warning = 3

s_words = ['apple','banana','car','dog','elephant','fish','guitar','house',
        'ice cream','jump','kite','lemon','mountain','notebook','orange','piano',
        'quilt','rainbow','star','tiger','butterfly','candle','diamond','fireworks',
        'giraffe','hen','island','jungle','kangaroo','lighthouse']

word = s_words[random.randint(0,29)]
loop = len(word)
new_word = []
used_letter = []
breaker = 0
print(word)

while loop > 0:
    new_word.append('-')
    loop -= 1

def info_update():
    print("---------------------------------------------------------------------------------------")
    print("|  Word","".join(str(i) for i in new_word), )
    print(f"|  Guesses remaing: {guess}")
    print(f"|  Letters not used: {', '.join(i for i in string.ascii_lowercase if i not in used_letter)}")
    print("---------------------------------------------------------------------------------------  \n")

def letter_check_1(chr):
    global warning
    if chr in string.ascii_lowercase :
        if chr in used_letter:
            warning = warning - 1

    else:
        print("Invalid Input")
        if not g_w_check():
            end()

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
        if chr not in "aiueo":
            guess -= 1
        else:
            guess -= 2
            return[]

def g_w_check():
    if guess > 0 :
        if warning == 0:
            return False
        return True
    return False

def end():
    print('you loose')
    

print("--- Hello! Welcome to Hangman Game ---")
print("You know the rules for the game")
print("You must Enter one character at a time\n\n ------ Let's Start ------\n")

#info updates
info_update()



while breaker != len(new_word) :
    if g_w_check():
        char = input("Enter any letter for the guess: ")
        used_letter.append(char)
        letter_check_1(char)
        index = letter_check_2(char, word)
        print(index,'\n')

        if index:
            count = 0
            for i in word:
                if count in index:
                    new_word[count] = char
                    breaker += 1
                    count += 1
                    continue
                count += 1

        info_update()
    else:
        break


print('\n Thanks For Playing')