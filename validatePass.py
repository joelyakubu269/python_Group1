def validate_pass(y):
    if y == "":
        return "no pass"
    elif len(y) < 5:
        return "too short"
    elif y[0] != "P":
        return "Invalid prefix"
    for x in y:
        if x == " " :
            return "invalid format"

    return "valid"
print(validate_pass("pass code"))
