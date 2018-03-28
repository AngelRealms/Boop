from boop import misc


def getLine(tokens, line):
    data = []
    for token in tokens:
        if token.line == line:
            data.append(token)
    return data


def parse(tokens):
    program = misc.Program()
    variables = {}
    queue = []
    for token in tokens:
        if token.type == "PRINT":
            line = getLine(tokens, token.line)
            if line[0] == token:
                line.pop(0)
                string = ""
                for part in line:
                    if line.index(part) == len(line) - 1:
                        if part.type == "STRING":
                            string += "'{string}'".format(string=part.value)
                        elif part.type == "ID":
                            string += "program.variables['{var}']".format(var=part.value)
                        elif part.type == "INT":
                            string += part.value
                        else:
                            raise misc.BoopError("Error!")
                    else:
                        if line.index(part) % 2 == 0:
                            if part.type == "STRING":
                                string += "'{string}'".format(string=part.value)
                            elif part.type == "ID":
                                string += "program.variables['{var}']".format(var=part.value)
                            elif part.type == "INT":
                                string += part.value
                            else:
                                raise misc.BoopError("Error!")
                        else:
                            if part.type == "PLUS":
                                string += "+"
                            elif part.type == "MINUS":
                                string += "-"
                            elif part.type == "TIMES":
                                string += "*"
                            elif part.type == "DIVIDE":
                                string += "//"
                            else:
                                raise misc.BoopError("Unknown Operator")
                queue.append("print({string})".format(string=string))
        elif token.type == "ID":
            line = getLine(tokens, token.line)
            if line[0] == token:
                line.pop(0)
                if line[0].type != "EQUALS":
                    raise misc.BoopError("Syntax Error!")
                else:
                    line.pop(0)
                    event = "program.variables['{id}'] = ".format(id=token.value)
                    for part in line:
                        if line.index(part) == len(line) - 1:
                            if part.type == "STRING":
                                event += "'{string}'".format(string=part.value)
                            elif part.type == "INT":
                                event += part.value
                            elif part.type == "ID":
                                event += "program.variables['{id}']".format(id=part.value)
                            else:
                                raise TypeError("[1]Invalid Type {type} on Line {line}[{num}]".format(line=token.line, type=part.type, num=line.index(part)))
                        else:
                            if line.index(part) % 2 == 0:
                                if part.type == "STRING":
                                    event += "'{string}'".format(string=part.value)
                                elif part.type == "INT":
                                    event += part.value
                                elif part.type == "ID":
                                    event += "program.variables['{id}']".format(id=part.value)
                                else:
                                    raise TypeError("[2]Invalid Type {type} on Line {line}[{num}]".format(line=token.line, type=part.type, num=line.index(part)+1))
                            else:
                                if part.type == "PLUS":
                                    event += "+"
                                elif part.type == "MINUS":
                                    event += "-"
                                elif part.type == "TIMES":
                                    event += "*"
                                elif part.type == "DIVIDE":
                                    event += "//"
                                else:
                                    raise TypeError(
                                        "[3]Invalid Type {type} on Line {line}[{num}]".format(line=token.line,
                                                                                              type=part.type,
                                                                                              num=line.index(part) + 1))
                    queue.append(event)
    program.variables = variables
    program.events = queue
    return program
