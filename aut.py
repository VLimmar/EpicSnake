import string
def tip(str):
    a = string.ascii_lowercase
    str = str.lower()
    TF = True
    for temp in a:
        if not temp in str:
            TF = False
    return TF



print(tip("aqzwsedcrtfvgbyuhnjmilqwuetirop"))
