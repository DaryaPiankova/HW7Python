import random

MAX_LEN = 7
MIN_LEN = 4
MIN_LETTER = ord('a')
MAX_LETTER = ord('z')
VOWELS = {'a','o','y','i','u','e'}


def generate_name_file(filename: str, count_name: int):
    """Генерация псевдоимен."""
    with open(filename, 'w', encoding='utf-8') as f:
        for j in range(count_name):
            len_name = random.randint(MIN_LEN, MAX_LEN)
            name = []
            for i in range(len_name):
                name.append(chr(random.randint(MIN_LETTER, MAX_LETTER)))
            has_vowels = False
            for letter in name:
                if letter in VOWELS:
                    has_vowels = True
                    break
            if not has_vowels:
                ind = random.randint(0, len_name-1)
                letter = random.choice(list(VOWELS))
                name[ind] = letter
            print(f'{"".join(name).capitalize()}', file=f, end='')
            f.write('\n' if j < count_name - 1 else "")


if __name__ == '__main__':
    generate_name_file("data_names.txt", 25)