from sly import Lexer


class JuliaLexer(Lexer):

    tokens = {
        ID, NUMBER, STRING,
        PRINTLN, IF, END, FOR, IN,
        GT, LT, EQ
    }

    literals = {'(', ')', '=', ':'}

    ignore = ' \t'

    PRINTLN = r'println'
    IF = r'if'
    END = r'end'
    FOR = r'for'
    IN = r'in'

    GT = r'>'
    LT = r'<'
    EQ = r'=='

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'"[^"]*"'
    NUMBER = r'\d+'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        print(f'Caractere inválido: {t.value[0]}')
        self.index += 1