#!/usr/bin/python3

def no_c(my_string):

    my_string_nw = ''

    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue

        my_string_nw += my_string[i]

    return my_string_nw
