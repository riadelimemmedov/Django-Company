# netice = ([(str(x)) for x in range(1,10)])
# print(netice)

import random

el = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def random_code():
    random.shuffle(el)
    code = [str(x) for x in el[:12]]#yeni 12 elemt icinden donsun butun element icinde yox bunun ucunde => el[:12]
    print(code)
    str_code = ''.join(code)#''.join yazanda ele duz birlesdirir yan yana
    print(str_code)
#random_code()