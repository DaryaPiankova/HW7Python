import os
import random as rd

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def generate_number_file(count:int, filename:str):
    """Заполняет файл случайными числами."""
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{rd.randint(MIN_NUMBER, MAX_NUMBER)}|{rd.random() * 2000 - 1000}')
            f.write('\n' if i < count - 1 else "")


if __name__ == '__main__':

        generate_number_file(10, "data.txt")