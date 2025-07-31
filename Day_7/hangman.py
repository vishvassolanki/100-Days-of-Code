import random



stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']




lives = 6

print("Hint: The word is an animal name")
word_list = ["lion", "tiger", "camel", "buffalo", "zebra", "cow", "horse", "elephant", "dog", "cat"]
chosen_word = random.choice(word_list)
# print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
        placeholder += "_"
print(placeholder)



game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    # print(guess)

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win!")


    print(stages[lives])