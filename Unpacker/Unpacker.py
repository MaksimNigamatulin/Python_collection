# coding: utf-8-sig
# -----------------------------------#
#       Maksim Nigamatulin           #
#           29/09/2020               #
#  Скрипт для распаковки архивов в   #
#  заданный каталог.                 #
# -----------------------------------#

# импорт модулей
import os
import zipfile

# каталог, в котором будем искать архивы
zip_folder_path = r'C:\Users\User\Downloads'

if not os.path.exists(r'C:\Users\User\Downloads\unpack files'):
    # каталог, в который будем распаковывать архивы
    unpack_folder_path = os.mkdir(r'C:\Users\User\Downloads\unpack files')
for files in os.walk(zip_folder_path):
    for file in files:
        for item in file:
            if item.lower().endswith('.zip')\
                or item.lower().endswith('.rar'):
                print(item)


#print(f'Архив {} успешно распакован.')