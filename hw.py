""" 

Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

import os

def rename_files(target_name, num_digits, original_ext, final_ext, name_range):
    # Получаем список всех файлов в текущем каталоге
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(original_ext)]
    
    # Применяем диапазон к именам файлов
    for index, file in enumerate(files):
        # Извлекаем оригинальное имя без расширения
        base_name = os.path.splitext(file)[0]
        
        # Получаем символы из оригинального имени в указанном диапазоне
        # Обратите внимание, что Python использует 0-индексацию
        start, end = name_range
        extracted_part = base_name[start:end]  # Необходимо учитывать, что end не включается
        
        # Формируем новое имя файла
        new_file_name = f"{extracted_part}{target_name}{str(index + 1).zfill(num_digits)}.{final_ext}"
        
        # Переименовываем файл
        os.rename(file, new_file_name)
        print(f"Переименован: {file} -> {new_file_name}")

if __name__ =='__main__':
    rename_files(target_name='new_file', num_digits=3, original_ext='.txt', final_ext='txt', name_range=(3, 6))
