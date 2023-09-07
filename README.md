# Hangman-game-in-Python
 Program is going to randomly select an English word  from a list and display a string of – of the same length as the word and ask the user to guess the word  one character at a time.


Programming Assignment 1

Implement the simplified version of the Hangman game as follows:
    • Your program is going to randomly select an English word  from a list and display a string of – of the same length as the word and ask the user to guess the word  one character at a time. 
    • The user starts with 6 guesses available to him/her.
    • At each step of the game the program notifies the user about the guesses remaining, and the letters not yet used. After each guess, the program displays the word the user’s guess with the characters already guessed displayed, and the characters not yet guessed replaced by -
    • If the user inputs a symbol other than a letter, notify and give him/her a warning. At the start of the game, the user has 3 warnings available. If a user inputs a non-letter symbol and has no warnings left, he/she should lose a guess.
    • If the player inputs an already used character, he/she should lose a warning or a guess, depending on whether there are any warnings available.
    • If the player inputs a letter that is in the secret word and has not been already guessed, the player does not lose a guess.
    • If the player input a consonant not in the secret word, he/she should lose one guess.
    • If the player inputs a vowel (a,e,i,o,u), he/she should lose 2 guesses.
    • The game ends when the player guesses the entire word before exhausting his guesses ( WIN) or when the player exhausts his guesses(LOSS)
    • In case of a win , the score for the player is computed as the number of guesses remaining times the  number of unique letters in the secret word.
