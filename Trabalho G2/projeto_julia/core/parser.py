from sly import Parser
from core.lexer import JuliaLexer


class JuliaParser(Parser):

    tokens = JuliaLexer.tokens

    debugfile = 'parser.out'

    @_('comandos')
    def programa(self, p):
        pass

    @_('comandos comando')
    def comandos(self, p):
        pass

    @_('comando')
    def comandos(self, p):
        pass

    # x = 10
    @_('ID "=" NUMBER')
    def comando(self, p):
        print(f'Atribuição: {p.ID} = {p.NUMBER}')

    # println("Olá")
    @_('PRINTLN "(" STRING ")"')
    def comando(self, p):
        print(p.STRING)

    # if x > 5
    @_('IF ID GT NUMBER comandos END')
    def comando(self, p):
        print("Comando IF reconhecido")

    # for i in 1:5
    @_('FOR ID IN NUMBER ":" NUMBER comandos END')
    def comando(self, p):
        print("Comando FOR reconhecido")

    def error(self, p):
        if p:
            print(f'Erro de sintaxe em {p.value}')
        else:
            print('Erro de sintaxe')