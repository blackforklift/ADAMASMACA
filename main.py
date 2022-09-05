import random
from replit import clear
from hangman_words import word_list

chosen_word = random.choice(word_list)
#print(f'the chosen world is {chosen_word}.')
word_length = len(chosen_word)
gameover = bool(False)
lives = 6
from hangman_art import logo, stages

print(logo)
display = []

for x in range(word_length):
    display += "_"

while gameover == False:

    print(" ")
    guess = input("Bir Harf Söyle: ").lower()
    clear()

    if guess in display:
        print(f"Bunu daha önce söyledin {guess}")

    for index in range(word_length):
        letter = chosen_word[index]

        if guess == letter:
            display[index] = letter

    finale = print(f"{''.join(display)}")

    #final_word=''.join(map(str,display))
    #if final_word==chosen_word:
    if not guess in chosen_word:
        print(f"Tahminin: {guess} Kelime bu harfi içermiyor. Can Kaybettin.")
        lives -= 1

        if lives == 0:
            print("Canların bitti oyunu kaybettin. Bir dahakine iyi şanslar")
            print(f"doğru kelime : {chosen_word} idi.")
            gameover = bool(True)

    print(stages[lives])
    if not '_' in display:
        print(" Yaşasın! Kazandınn! ")
        gameover = bool(True)
