

def my_var():
    my_list = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42, ), set()]
    for li in my_list:
        print(format(li) + " est de type", type(li))


if __name__ == '__main__':
    my_var()
