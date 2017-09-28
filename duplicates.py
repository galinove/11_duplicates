import os
import sys

def get_files_collection(dir,dict):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path):
        dict[str(path)] = str(name) + ";" + str(os.path.getsize(path))
    else:
        get_files_collection(path,dict)
  return dict

def print_duplicates(dir, dict):
    try:
        get_files_collection(dir, dict)
    except PermissionError:
        print("Ошибка доступа")
    dict_unique_files=dict.fromkeys(set(dict.values()),0)
    for name_size_agr, cnt_name_size in dict_unique_files.items():
        for path, name_size in dict.items():
            if name_size_agr == name_size:
                cnt_name_size=cnt_name_size+1
        dict_unique_files[name_size_agr] = cnt_name_size

    for name_size_agr, cnt_name_size in dict_unique_files.items():
        if cnt_name_size > 1:
            print()
            print("Найдены дубликаты файла " + name_size_agr.split(";")[0] + " размером " + str(int(name_size_agr.split(";")[1])//1024+1) + " Кбайт:")
            for path, name_size in dict.items():
                if name_size_agr == name_size:
                    print(path)

def find_duplicates (dir):
    dict = {}
    print_duplicates(dir,dict)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        filepath = (sys.argv[1])
    else:
        print("Введите директорию, в которой будем искать дубли файлов (по имени и размеру)")
        filepath = input()
    find_duplicates (filepath)