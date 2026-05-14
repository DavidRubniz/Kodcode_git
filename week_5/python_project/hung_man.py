import random

WORDS_LIST = ['red', 'blue', 'green', 'grey']
guess = []
score = 0

def random_word() -> str:
    return random.choice(WORDS_LIST)


def get_valid_input() -> str|None:
    while True:
        gues = input('Enter your gues: ').lower()
        if ('a' <= gues <= 'z' or 'A' <= gues <= 'Z') and len(gues) == 1:
            return gues
        print('you must enter one letter in English')


def check_gues(word: str, gues: str) -> tuple[bool, int] | bool:
    if gues in word:
        indexes = [i for i, letter in enumerate(word) if letter == gues]
        return True, indexes
    return False


def check_finish(_status: list, _turns: int) -> bool:
    global score
    if _turns == 0:
        print(f'you failed the word is: {''.join(_status)}')
        return True
    if '_' not in _status:
        print(f'well done the word is: {''.join(_status)}')
        score += 10
        print(f'your score is {score}')
        return True
    return False

def main() -> None:
    print('wellcome to hung-man game')
    word = random_word()
    status = ['_' for i in range(len(word))]
    turns = 5
    while True:
        print(''.join(status))
        print(f'you left {turns} turns to play')
        print(f'guessed: {guess}')
        val_inp = get_valid_input()
        sec = check_gues(word, val_inp)
        guess.append(val_inp)
        if sec and sec[0]:
            for idx in sec[1]:
                status[idx] = val_inp
        else:
            turns -= 1
        if check_finish(status, turns):
             break

if __name__ == "__main__":
    while True:
        main()
        _choice = input('press 0 for exit and 1 to play again: ')
        if _choice == '0':
            break
        guess = []
        print()
        print()