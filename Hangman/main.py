def get_word():
    word = input("Enter a word: ").lower()
    return word


def get_initial_positions(word):
    length = len(word)
    positions = [True if x == 0 or x == length - 1 else False for x in range(length)]
    return positions


def hide_word(word, positions):
    revealed = word[0]
    for i in range(1, len(word) - 1):
        revealed += "-" if not positions[i] else word[i]
    revealed += word[-1]
    return revealed


def check_guess(word, letter, positions):
    updated_positions = positions.copy()
    for i, v in enumerate(word):
        if word[i] == letter:
            updated_positions[i] = True
    return updated_positions


def check_for_win(word, positions):
    length = len(word)
    winning_positions = [True for _ in range(length)]
    if positions == winning_positions:
        return True
