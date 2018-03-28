from boop import lexer
from boop import parser


def load(file, debug=False):
    tokens = lexer.lex(file)
    if debug:
        for token in tokens:
            print("VALUE:" + token.value)
            print("TYPE:" + token.type)
            print("LINE:" + str(token.line))
            print("NUM:" + str(token.num))
            print("STRING:" + str(token.isString))
        print(len(tokens))
        exit(0)
    program = parser.parse(tokens)
    for event in program.events:
        exec(event)