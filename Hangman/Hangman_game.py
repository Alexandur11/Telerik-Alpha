from main import (get_word,
                  get_initial_positions,
                  hide_word,
                  check_guess,
                  check_for_win)


def play_hangman():
    word = get_word()
    lives = 3
    positions = get_initial_positions(word)
    hidden = hide_word(word, positions)

    print(hidden)

    while True:  # we will check for win or loss in the loop and break accordingly
        letter = input("Please Enter a letter: ")
        new_positions = check_guess(word, letter, positions)

        # Option 1 - both lists are the same - the next_letter is not a correct guess
        if new_positions == positions:
            print('No such letter or already guessed')
            print(f'Lives remaining: {lives - 1}')
            lives = lives - 1

            if lives == 0:  # no more lives - break
                print('You lose!')
                break

        # Option 2 - if the lists are not the  same, all values in new_positions may be True
        #    we use the check_for_win function to validate
        elif check_for_win(word, new_positions):
            print('You win!')
            # print(F"The word is '{word}!'")
            break

        # Option 3 - the two lists are not the same, and new_positions is not all True - this means that another
        # letter is guessed. We need to print it.
        else:
            print('Another letter guessed!')
            print(hide_word(word, new_positions))
            positions = new_positions


play_hangman()
