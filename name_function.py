#这部分相当于一个应用

def get_formated_name(first,last,middle=''):

    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()