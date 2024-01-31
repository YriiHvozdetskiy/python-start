import sys

print(sys.argv)  # ['/Users/rasty/Python/python-examples/pythonPyCharm/my_sys.py']

"""terminal"""
# python3 my_sys.py username
# python3 my_sys.py username password

if len(sys.argv) < 3:
    raise IOError('You must provide password')

# username = sys.argv[1]
# password = sys.argv[2]

filename, username, password = sys.argv

print(f"print {username, password}")  # print ('dima,', '1234')
