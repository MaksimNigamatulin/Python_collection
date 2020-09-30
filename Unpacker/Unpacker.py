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
zip_folder_path = r'C:\Users\User\Downloads' # задать через inpyt()

# запрос пути для хранения распакованных данных
unpacked_folder_path = str(input('Укажите каталог для распаковки архивов: '))

# определяем какие архивы будут доступны для поиска
zip_file = ['.zip', '.rar', '.7z', '.tar-gz']

# проверка наличия каталога для хранения распакованных данных
if not os.path.exists(unpacked_folder_path):
    # если каталог отсутствует - создать его
    storage_folder_path = os.mkdir(unpacked_folder_path)
# поиск всех файлов в корневом каталоге
for files in os.walk(zip_folder_path):
    # выбор списка файлов
    for file in files:
        # обход всех файлов в списке
        for item in file:
            # обход всех элементов из списка с типами архивов
            for i in zip_file:
                # сопоставление расширений найденных файлов и доступных типов архивов
                if item.lower().endswith(i):
                    print(item)


#print(f'Архив {} успешно распакован.')