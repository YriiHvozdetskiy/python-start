import re

my_string = 'My name is Bogdan'

res = re.search(r'^M.*name', my_string)
print(res)  # <re.Match object; span=(0, 7), match='My name'>

print(r'B....n\n.$')

my_patern = re.compile(r'B....n\n.$')


# validate password
def validate_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    numper_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, password):
        return False, 'No whitespaces allowed in the password'

    if not re.fullmatch(length_pattern, password):
        return False, 'Password must have at least 8 symbols'

    if not re.fullmatch(lowercase_pattern, password):
        return False, 'Password must have at least one lowercase letter'

    if not re.fullmatch(uppercase_pattern, password):
        return False, 'Password must have at least one uppercase letter'

    if not re.fullmatch(numper_pattern, password):
        return False, 'Password must have at least one number'

    if not re.fullmatch(special_symbol_pattern, password):
        return False, 'Password must have at least one special symbol @%#!&*^'

    return True, 'Password is valid'


print(validate_password('123sdfssdfas23  ASDAD  ^&*'))
print(validate_password('1234567'))
print(validate_password('12345678'))
print(validate_password('1234567a'))
print(validate_password('asdfgBSDFSDF'))
print(validate_password('123sdfsASDAD'))
print(validate_password('123sdfsASDAD^&*'))
