#Test functions written in an attempt to detect possible input calls - migh be useful

#patterns used in regex search
PATTERNS = {
    'def':re.compile(r'\bdef '),
    'import':re.compile(r'\bimport '),
    'input':re.compile(r'\binput\('),
    '(':re.compile(r'\(')
    }

def get_indexes(character, string):
    """ Get all indexes of character in string | str, str --> list[int] """
    return [i for i, c in enumerate(string) if c == character]

def get_previous_index(character, index, string, max_length=100):
    """ Find closest previous index of character | str, int, str, int --> int """
    return string.rfind(character, index-max_length, index)

def get_function_names(source_filepath):
    """ Get list of all possible function names | file --> list(str)

    This list includes many false positives by design. They will be weeded out
    later by other functions.
    """
    with open(source_filepath, 'r') as source_file:
        source_string = source_file.read()
        parenthesis_indexes = get_indexes('(', source_string)
        space_indexes = []
        for index in parenthesis_indexes:
            space_indexes.append(get_previous_index(' ', index, source_string))
        function_names = []
        combined_indexes = zip(space_indexes, parenthesis_indexes)
        function_names = []
        for space, parenthesis in combined_indexes:
            function_name = source_string[space+1:parenthesis]
            function_names.append(function_name)
        function_names = list(set(function_names))
        return function_names

def get_defined_functions(function_names, source_filepath):
    """ Get defined functions from possibilities | list(str), file --> list(str) """
    with open(source_filepath, 'r') as source_file:
        source_string = source_file.read()
