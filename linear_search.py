def linear_search(list, value):
    new_list = []
    for item in range(len(list)):
        if list[item] == value:
            new_list.append(item)
        
    return new_list


my_list = [11, 423, 10, 172, 30, 910, 9, 2, 45, 172, 10, 172, 10]

print("Values found at Indices: " + str(linear_search(my_list, 10)))