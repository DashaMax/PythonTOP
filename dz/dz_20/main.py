''' Объединение двух файлов. '''


import os


if not os.path.exists('folder'):
    os.mkdir('folder')

text = ('Первый файл.', 'Второй файл.')
path_files = ('folder/file1.txt', 'folder/file2.txt')
path_file_result = 'folder/file3.txt'

with open(path_file_result, 'w', encoding='utf-8') as file_result:
    for i in range(len(path_files)):
        with open(path_files[i], 'w+', encoding='utf-8') as file:
            file.write(text[i])
            file.seek(0)
            file_result.write(file.read())





''' Напишите программу, осуществляющую проверку, существует ли указанный файл.
    Если файл существует, выведите на экран имя этого файла и имя его директории, 
    а также время последнего доступа к файлу. 
    Если файл не существует, выведите соответствующее сообщение. '''


# import os
# import time
#
#
# path = r'folder/file1.txt'
#
# if os.path.exists(path):
#     fail_name = os.path.basename(path)
#     dir_name = os.path.dirname(path)
#     time_last_access = os.path.getatime(path)
#     print(f'Имя файла: {fail_name}')
#     print(f'Имя директории файла: {dir_name}')
#     print(f'Время последнего доступа к файлу: {time.ctime(time_last_access)} ({time_last_access} с)')
# else:
#     print(f'Файла по заданному пути "{path}" не существует')

