import os, sys

type = 'series'

test = False

source_dir = '/Users/jimmy/Downloads/'

insert_string = 'vol'

def insert_point_func(filename):
    return filename.find('_') + 1

def condition_func(filename):
    if filename[:5] == 'ca_hd':
        return True
    return False
    
def get_filenames(dir):
    filenames = os.listdir(source_dir)
    filenames = [filename for filename in filenames if filename[0] != '.']
    return filenames

def insert(source_dir, condition_func, insert_point_func, insert_string):
    for filename in get_filenames(source_dir):
        condition = condition_func(filename)
        insert_point = insert_point_func(filename)
        if filename[0] == '.':
            continue
        if not condition:
            continue
        new_filename = filename[:insert_point] + 'vol' + filename[insert_point:]
        if test:
            print(new_filename)
        else:
            os.rename(source_dir + '/' + filename, source_dir + '/' + new_filename)
base_string = 'RTA_03_'

def order_func(filename):
    return os.path.getctime(source_dir + '/' + filename)

def num_to_string(number, list_length):
    def num_to_string_10(number):
        if number > 9:
            return str(number)
        else:
            return '0' + str(number)
    def num_to_string_100(number):
        if number > 99:
            return str(number)
        elif number > 9:
            return '0' + str(number)
        else:
            return number
    if list_length < 10:
        return number
    if list_length < 100:
        return num_to_string_10(number)
    return num_to_string_100(number)

#NOTE: to update for more than 100 files
def series(source_dir, condition_func, order_func, base_string):
    filenames = get_filenames(source_dir)
    filenames = [filename for filename in filenames if condition_func(filename)]
    filenames = sorted(filenames, key=order_func)
    length = len(filenames)
    extension = filenames[0][-4:]
    if test:
        for number, filename in enumerate(filenames):
            old_filename = filename
            new_filename = base_string + num_to_string(number, length) + extension  
            print('old_filename = ' + filename)
            print('new_filename = ' + new_filename)
    else:
        for number, filename in enumerate(filenames):
            old_filename = filename
            new_filename = base_string + num_to_string(number, length) + extension  
            os.rename(source_dir + '/' + filename, source_dir + '/' + new_filename)

if type == 'insert':
    insert(source_dir, condition_func, insert_point_func, insert_string)

if type == 'series':
    series(source_dir, condition_func, order_func, base_string)
