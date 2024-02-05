#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    n_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            n_list.append(res)
    return n_list
