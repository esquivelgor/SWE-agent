import sys
from parser import Parser, lex  # Import the new Parser class and lex function

def is_oop_code(parse_tree):
    """
    Recursively check if parse_tree contains any 'class_def' nodes.
    """
    if isinstance(parse_tree, tuple):
        if parse_tree[0] == 'class_def':
            return True
    elif isinstance(parse_tree, list):
        for item in parse_tree:
            if is_oop_code(item):
                return True
    return False

def OOP_filter(code):

    # Tokenize and parse the code
    tokens = lex(code)
    parser = Parser(tokens)
    try:
        parse_result = parser.parse()
    except Exception as e:
        #print(f"Parsing failed: {e}")
        return -1

    if parse_result is None:
        #print("Parsing failed or no parse tree generated.")
        return -1

    if is_oop_code(parse_result):
        return 1
        #print(f"File '{filename}' contains OOP constructs (class definitions).")
    else:
        return 0
        #print(f"File '{filename}' does NOT contain OOP constructs.")
