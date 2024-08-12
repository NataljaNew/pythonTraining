from fractions import Fraction
def is_fraction(string):
    if ' ' in string:
        return False
    elif '/' in string:
        try:
           Fraction(string)
           return True
        except Exception:
            return False
    else:
        return False


print(is_fraction('1 / 1'))
