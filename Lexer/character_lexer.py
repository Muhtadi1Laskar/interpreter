class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"
    
    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self, value):
        self.text = value
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.result = []
    
    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def tokenize(self):
        while self.current_char is not None:
            if self.current_char is not None and self.current_char.isdigit():
                self.result.append(Token('Integer', int(self.current_char)))
                self.advance()

            if self.current_char is not None and self.current_char.isspace():
                self.advance()
            
            if self.current_char == '+':
                self.result.append(Token('Plus', '+'))
                self.advance()
            
            if self.current_char == '-':
                self.result.append(Token('Minus', '-'))
                self.advance()
        
        self.result.append(Token('EOF', None))
        return self.result

lexer = Lexer('3.3 + 2')

token = lexer.tokenize()

print(token)