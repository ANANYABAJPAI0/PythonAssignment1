def count_occurrences(lst, element):
    
    return lst.count(element)


my_list = [1, 2, 3, 4, 2, 2, 3, 1, 2]
element_to_count = 2

occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")
