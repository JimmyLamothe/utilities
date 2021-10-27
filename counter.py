counters = {}

def get_new_counter():
    counter = input('Enter name for new counter, or press Enter when done\n')
    if counter == '':
        return 'break'
    else: counters[counter] = 0    

def results():
    for counter in counters:
        print(f'{counter} : {str(counters[counter])}')

def valid_counters(string):
    return [counter for counter in counters
            if counter[:len(string)].lower() == string.lower()]

def get_new_count():
    string = input()
    if string == ' ':
        return 'break'
    return string

def valid_input(string):
    counter_list = valid_counters(string)
    if not counter_list:
        print ('No matches were found. Try again or type a single space to exit')
        return False
    elif not len(counter_list) == 1:
        print('More than one matching counter was found. Enter more letters.')
        return False
    return True

def count():
    string = get_new_count()
    if string == 'break':
        return 'break'
    if string == '#':
        results()
        return
    if not valid_input(string):
        count()
    counter = valid_counters(string)[0] #Yes it's a double call - No it doesn't matter
    counters[counter] += 1
    return
    
def main():
    while not get_new_counter() == 'break':
        continue
    print('Please type first letter of counter (or more if needed).')
    print("Type # at any time to get current count")
    print('Type a single space to exit')
    while not count() == 'break':
        count()
    print('\n\nHere is the final count:\n\n')
    results()

main()
