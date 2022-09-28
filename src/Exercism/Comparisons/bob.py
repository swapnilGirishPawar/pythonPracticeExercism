

def response(hey_bob):

    2 == "Whoa, chill out!"
    3 == "Calm down, I know what I'm doing!"
    4 == "Fine. Be that way!"
    5 == "Whatever."

    str = hey_bob

    if not str:  # need to write
        return print("Fine. Be that way!")

    if not str.isupper() and ("?" in str):
        return print("Sure")
    elif '?' not in str and str.isupper():
        return print("Whoa, chill out!")
    elif str.isupper() and (("?" in str)):
        return print("Calm down, I know what I'm doing!")
    else:
        return print("Whatever.")


response("")
