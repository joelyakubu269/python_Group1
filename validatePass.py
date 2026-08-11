def validate_pass(pass_code):
    if "pass_code" == "":
        return "no pass"
    if len("Pass_code") < 5:
        return "too short"
    if "Pass_code"[0] != "P":
        return "Invalid prefix"
    for x in "Pass_code":
        if x == " " :
            return "invalid format"
