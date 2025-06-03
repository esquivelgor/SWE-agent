import re
# --- Lexer ---

# Token specification as regex patterns
TOKEN_SPECIFICATION = [
    ('CLASS',      r'class\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('COLON',      r':'),
    ('LPAREN',     r'\('),
    ('RPAREN',     r'\)'),
    ('COMMA',      r','),
    ('NEWLINE',    r'\n'),
    ('SKIP',       r'[ \t\r]+'),  # Skip spaces, tabs, carriage returns
    ('OTHER',      r'.'),         # Any other character
]

# Compile regex patterns
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
get_token = re.compile(token_regex).match

class Token:
    def __init__(self, type_, value, lineno, column):
        self.type = type_
        self.value = value
        self.lineno = lineno
        self.column = column

    def __repr__(self):
        return f'Token({self.type}, {self.value!r}, line={self.lineno}, col={self.column})'

def lex(text):
    """Simple lexer generator yielding tokens."""
    lineno = 1
    pos = 0
    mo = get_token(text, pos)
    while mo is not None:
        typ = mo.lastgroup
        val = mo.group(typ)
        if typ == 'NEWLINE':
            lineno += 1
            pos = mo.end()
            mo = get_token(text, pos)
            continue
        elif typ == 'SKIP':
            pos = mo.end()
            mo = get_token(text, pos)
            continue
        else:
            column = mo.start() - text.rfind('\n', 0, mo.start())
            yield Token(typ, val, lineno, column)
        pos = mo.end()
        mo = get_token(text, pos)
    yield Token('EOF', '', lineno, pos)

# --- Parser ---

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def error(self, msg='Syntax error'):
        raise ParserError(f'{msg} at line {self.current_token.lineno} col {self.current_token.column}')

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token('EOF', '', self.current_token.lineno, self.current_token.column)

    def expect(self, token_type):
        if self.current_token.type == token_type:
            val = self.current_token.value
            self.advance()
            return val
        else:
            self.error(f'Expected token {token_type}, got {self.current_token.type}')

    def parse(self):
        return self.program()

    # program : segment_list
    def program(self):
        segments = self.segment_list()
        return segments

    # segment_list : segment_list segment | segment
    def segment_list(self):
        segments = []
        while self.current_token.type != 'EOF':
            segment = self.segment()
            segments.append(segment)
        return segments

    # segment : class_def | misc
    def segment(self):
        if self.current_token.type == 'CLASS':
            return self.class_def()
        else:
            return self.misc()

    # class_def : CLASS IDENTIFIER inheritance_opt COLON
    def class_def(self):
        self.expect('CLASS')
        class_name = self.expect('IDENTIFIER')
        bases = self.inheritance_opt()
        self.expect('COLON')
        #print("Found a class definition:", class_name)  # Debug print
        return ('class_def', class_name, bases)

    # inheritance_opt : LPAREN base_classes RPAREN | empty
    def inheritance_opt(self):
        if self.current_token.type == 'LPAREN':
            self.expect('LPAREN')
            bases = self.base_classes()
            self.expect('RPAREN')
            return bases
        else:
            return []

    # base_classes : IDENTIFIER base_class_tail
    def base_classes(self):
        bases = [self.expect('IDENTIFIER')]
        bases.extend(self.base_class_tail())
        return bases

    # base_class_tail : COMMA IDENTIFIER base_class_tail | empty
    def base_class_tail(self):
        bases = []
        while self.current_token.type == 'COMMA':
            self.expect('COMMA')
            bases.append(self.expect('IDENTIFIER'))
        return bases


    def misc(self):
        """Consume tokens until next CLASS or EOF."""
        tokens = []
        while self.current_token.type not in ('CLASS', 'EOF'):
            tokens.append(self.current_token.value)
            self.advance()
        # Return a misc node with the combined token values (optional)
        return ('misc', ' '.join(tokens))

# --- Example usage ---

if __name__ == '__main__':
    code = '''
    class MyClass(Base1, Base2):
    some_other_text
    '''
    tokens = lex(code)
    parser = Parser(tokens)
    ast = parser.parse()
    print('AST:', ast)
