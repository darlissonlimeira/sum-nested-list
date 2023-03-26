from sum_number_list import sum_number_list

def sum_nested_number_lists(list_of_lists_of_numbers):
    total = 0

    for list_of_numbers in list_of_lists_of_numbers:
        total += sum_number_list(list_of_numbers)

    return total
