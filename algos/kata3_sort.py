def descending_order(num):
    temp = ''
    temp_key = 0
    item_key = -1
    comp_key = -1
    curr_max = 0

    string_list = [i for i in str(num)]

    # loop 1: items
    for item in string_list:
        item_key += 1

        # loop 2: compare vs others
        for comp in string_list:
            comp_key += 1
            if item < comp and item_key < comp_key: # needs to be swapped
                if int(comp) > curr_max: # check to find greatest swap
                    temp = comp
                    temp_key = comp_key
                    curr_max = int(temp)
        # reset for next loop 2 iteration
        comp_key = -1
        curr_max = 0

        if temp: # modify list in-place
            string_list[temp_key] = item
            string_list[item_key] = temp
            temp = '' # reset temp

    print(string_list)
    return int(''.join(string_list))



descending_order(14652637)
