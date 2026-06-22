from core.lexer import JuliaLexer
from core.parser import JuliaParser

lexer = JuliaLexer()
parser = JuliaParser()

with open("examples/invalido2.txt", "r", encoding="utf-8") as arquivo:
    codigo = arquivo.read()

parser.parse(lexer.tokenize(codigo))