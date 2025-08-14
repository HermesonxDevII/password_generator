import random
import string

has_uppercase = lambda s: any(c.isupper() for c in s)
has_lowercase = lambda s: any(c.islower() for c in s)
has_digit = lambda s: any(c.isdigit() for c in s)
has_symbol = lambda s: any(c in string.punctuation for c in s)

def create_validator(min_length, criteria):
    def validator(p):
        return len(p) >= min_length and all(c(p) for c in criteria)
    return validator

def validate_password(p, validators):
    return all(v(p) for v in validators)

def generate_password(length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    chars = ""
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not chars:
        raise ValueError("No character sets selected.")
    return ''.join([random.choice(chars) for _ in range(length)])