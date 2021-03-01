"""
    1. Нарисовать границу из * в списке.
    [in]    ['python',
             'django']

    [out]   ['********',
             '*python*',
             '*django*',
             '********']

    [in]    ['abc',
             'def']

    [out]   ['*****',
             '*abc*',
             '*def*',
             '*****']

    Покрыть несколькими тестами.
"""

def draw_border(original_list):
    new_list = []
    for i in original_list:
        new_list.append("*" + i + "*")
    new_list.append((len(new_list[0])) * "*")
    new_list.insert(0, (len(new_list[0])) * "*")

    print(new_list)
    return new_list
    

t_1 = ['python',
        'django']
assert draw_border(t_1) == ['********',
            '*python*',
            '*django*',
            '********']

t_2 = ['abc',
        'def']
assert draw_border(t_2) == ['*****',
            '*abc*',
            '*def*',
            '*****']

t_3 = ['hi',
        'by']
assert draw_border(t_3) == ['****',
            '*hi*',
            '*by*',
            '****']

print("All tests passed successfully!")