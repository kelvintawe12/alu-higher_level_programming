#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed_count = 0
    try:
        while count < x:
            if isinstance(my_list[count], int):
                print("{:d}".format(my_list[count]), end="")
                printed_count += 1
            count += 1
    except IndexError:
        raise
    print()
    return printed_count

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, 7)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, 9)
    print("nb_print: {:d}".format(nb_print))
