def email_validator(email):
    count_at = 0
    count_period = 0
    count_space = 0
    count_email = 0
    for i in email:
        count_email = count_email + 1
        if i == "@":
            count_at = count_at + 1
        else:
            count_at = count_at
        if i == ".":
            count_period = count_period + 1
        else:
            count_period = count_period
        if i == " ":
            count_space = count_space + 1
        else:
            count_space = count_space
    if (count_period != 1) or (count_at != 1) or (count_space > 0) or (count_email > 20 or count_email < 3):
        return False
    else:
        return True