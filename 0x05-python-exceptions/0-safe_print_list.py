#!/usr/phython3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            print(i, end="")
            count += 1
            if count == x:
                break
        print()
    except IndexError:
        pass

    return (count)
