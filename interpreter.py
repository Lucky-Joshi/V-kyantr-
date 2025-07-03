from tokenizer import tokenize

variables = {}

def evaluate_expression(expr_tokens):
    expr = ""
    for token in expr_tokens:
        val = token["value"]
        if val in variables:
            expr += str(variables[val])
        else:
            expr += val
    try:
        return eval(expr)
    except Exception as e:
        raise Exception(f"त्रुटिः: गणना विफलम् ({e})")

def execute_line(tokens):
    if tokens[0]["value"] == "वद":
        value = " ".join([t["value"] for t in tokens[1:] if t["type"] != "DELIMITER"])
        print(eval(value) if value.startswith('"') else variables.get(value, value))

    elif tokens[0]["type"] == "IDENTIFIER" and tokens[1]["value"] == "=":
        var_name = tokens[0]["value"]
        expr_value = evaluate_expression(tokens[2:])
        variables[var_name] = expr_value

    elif tokens[0]["value"] == "यदि":
        condition = evaluate_expression(tokens[1:-1])
        return bool(condition)

    elif tokens[0]["value"] == "अन्यथा":
        return "ELSE"

def run_code(lines):
    i = 0
    skip_else = False
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        tokens = tokenize(line)
        if not tokens:
            i += 1
            continue
        result = execute_line(tokens)
        if result is True:
            i += 1
        elif result is False:
            skip_else = True
            i += 2
        elif result == "ELSE":
            if skip_else:
                i += 2
                skip_else = False
            else:
                i += 1
        else:
            i += 1
