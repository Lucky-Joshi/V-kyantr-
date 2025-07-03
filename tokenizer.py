import re

KEYWORDS = {"यदि", "अन्यथा", "तर्हि", "वद"}
OPERATORS = {"+", "-", "*", "/", ">", "<", ">=", "<=", "==", "!="}
DELIMITERS = {"(", ")", ":", "="}

def tokenize(code):
    tokens = []
    lines = code.strip().split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        words = re.findall(r"[\w\u0900-\u097F]+|==|!=|<=|>=|[=+\-*/()><:]", line)
        for word in words:
            if word in KEYWORDS:
                token_type = "KEYWORD"
            elif word in OPERATORS:
                token_type = "OPERATOR"
            elif word in DELIMITERS:
                token_type = "DELIMITER"
            elif word.isdigit():
                token_type = "NUMBER"
            else:
                token_type = "IDENTIFIER"
            tokens.append({"type": token_type, "value": word})
    return tokens
