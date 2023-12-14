while True:
    str_num = input()
    if str_num == "0": break
    else:
        if str_num[:] == str_num[::-1]: print("yes")
        else: print("no")
