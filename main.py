print("Welcome!")

answer_word = "ABCDEFG"
guess_correct_list = ""

while True:
    guess = input("Please guess one letter:")
    if len(guess) != 1:
        print("Input incorrect!")
        continue

    if answer_word.find(guess) != -1 and guess_correct_list.find(guess) == -1:
        guess_correct_list = guess_correct_list += guess

    hint = ""
    for char in answer_word:
        if guess_correct_list.find(char) != -1:
            hint = hint + char + " "
        else:
            hint = hint + "_" + " "

    print(hint)
    if hint.find("_") == -1:
        print("You win!")
        break
