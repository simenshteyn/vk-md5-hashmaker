import hashlib
import re

def make_md5_hash(string: str):
    """
        Makes MD5 hash from a given string
    """
    h = hashlib.md5(string.encode('UTF-8'))
    result = h.hexdigest()
    return result

def clear_phone(string: str):
    """
        Clears phone humber from other symbols, like «)(-.»
        Returns phone in 7XXXXXXXXXX format.
    """
    result = ''
    for letter in string:
        if letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result += letter
    if result[0] == '8' and len(result) == 11:
        result = '7' + result[1:]
    if len(result) == 10:
        result = '7' + result
    return result

def clear_email(string: str):
    """
        Makes email address low case format. Returns string.
    """
    result = string.lower()
    return result

def read_file(file_name: str):
    """
        Read file to list - one item per line. Removes \n from end.
    """
    foo = []
    with open(file_name, 'r') as file:
        for i in file.readlines():
            if i[-1:] == '\n':
                foo.append(i[:-1])
            else:
                foo.append(i)
    return foo

def email_or_phone(string: str):
    """
        Checks if given string is email or phone number.
        Returns 1 for phone number, 2 for email, 3 for other.
    """
    email_pattern = r"[a-z0-9]+[_a-z0-9\.-]*[a-z0-9]+@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})"
    phone_pattern = r"^\+?(7|8)?\D?[9][0-9]{2}\D?[0-9]\D?[0-9]\D?[0-9]\D?[0-9]\D?[0-9]\D?[0-9]\D?[0-9]\D?\b"
    if bool(re.fullmatch(email_pattern, string.lower())):
        return 2
    elif bool(re.fullmatch(phone_pattern, string)):
        return 1
    else:
        return 3

def correct_list(list: list):
    """
        Changes items from list to the right format.
        Returns list
    """
    result = []
    for item in list:
        data_type = email_or_phone(item)
        if data_type == 1:
            result.append(clear_phone(item))
        elif data_type == 2:
            result.append(clear_email(item))
        else:
            pass
    return result

def md5_hash_list(list: list):
    """
        Makes list of emails and phones MD5-hashed list. Returns list..
    """
    result = []
    for item in list:
        result.append(make_md5_hash(item))
    return result

def save_file(file_name:str, list:list):
    """
        Save list of strings to file
    """
    with open(file_name, 'w') as file:
        for item in list:
            file.write(item+'\n')

while True:
    file_in = str(input('Enter file name to MD5-hash-it: '))
    try:
        md5_hashed_list = md5_hash_list(correct_list(read_file(file_in)))
        save_file(file_in + 'md5-hashed.txt', md5_hashed_list)
        print(str(len(md5_hashed_list)), 'items MD5-hashed to', file_in + '_md5-hashed.txt')
    except:
        print('Something wrong. Try again')