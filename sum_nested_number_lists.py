def sum_nested_number_lists(list_of_lists_of_numbers):
    total = 0

    for list_of_numbers in list_of_lists_of_numbers:
        total += sum_number_list(list_of_numbers)

    return total


def sum_number_list(list_of_numbers):
    total = 0

    if len(list_of_numbers) < 1:
        return total

    for value in list_of_numbers:
        total += value

    return total
