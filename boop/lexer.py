from boop import misc
import shlex
import re


def lex(value,type="File"):
    if type == "File":
        lineno = 0
        return_data = []
        tokeno = 0
        for line in value:
            strings = shlex.split(line)
            lineno += 1
            for string in strings:
                tokeno += 1
                for token in misc.token_types:
                    if re.match(misc.token_types[token], string):
                        new_token = misc.Token()
                        new_token.setType(token)
                        new_token.setLine(lineno)
                        new_token.setValue(string)
                        new_token.setNum(tokeno)
                        if re.match(misc.token_types['INT'], new_token.value):
                            new_token.setType("INT")
                        if new_token.type == "STRING":
                            new_token.setString(True)
                        else:
                            new_token.setString(False)
                        return_data.append(new_token)
                        break
        return return_data
