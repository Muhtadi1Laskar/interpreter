import re

class Lexer:
    def __init__(self, input):
        self.input = input
        self.tokens = []
        self.pos = 0

        # Define token types and their corresponding regex patterns
        self.token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),   # Integer or decimal number
            ('ADD',      r'\+'),            # Addition operator
            ('SUB',      r'-'),             # Subtraction operator
            ('MUL',      r'\*'),            # Multiplication operator
            ('DIV',      r'/'),             # Division operator
            ('LPAREN',   r'\('),            # Left parenthesis
            ('RPAREN',   r'\)'),            # Right parenthesis
            ('EQUAL', r'='),
            ('SKIP',     r'[ \t]+'),        # Skip over spaces and tabs
            ('MISMATCH', r'.'),             # Any other character
        ]

        self.token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification)
        self.get_token = re.compile(self.token_regex).match

    def tokenize(self):
        while self.pos < len(self.input):
            match = self.get_token(self.input, self.pos)
            if not match:
                raise SyntaxError(f'Unexpected character: {self.input[self.pos]}')
            kind = match.lastgroup
            value = match.group(kind)
            if kind == 'SKIP':
                self.pos = match.end()
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Unexpected character: {value}')
            else:
                self.tokens.append((kind, value))
                self.pos = match.end()
        return self.tokens

# Example usage:
input = '3 + 5 * = (10 - 4) / 2'
lexer = Lexer(input)
tokens = lexer.tokenize()

for token in tokens:
    print(token)
