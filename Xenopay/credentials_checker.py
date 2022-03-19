def checkEmailQualification(email):
    if not ("@" in email):
        return 0
    else:
        if not (email.index("@") >= 2):
            return 0
        if not ("." in email):
            return 0
    return 1
def checkPasswordEquality(password_one, password_two):
    if (password_one != password_two):
        return 0
    return 1
def checkPasswordLength(password):
    if len(password) < 8:
        return 0
    return 1
def checkUnfilledCredentials(credentials):
    for credential in credentials:
        if credential == "":
            return 0
    return 1
def checkPasswordQualification(password_one, password_two):
    equality = checkPasswordEquality(password_one, password_two)
    length = checkPasswordLength(password_one)
    if not (equality and length):
        return 0
    return 1