def sum_number_list(list_of_numbers):
    total = 0

    if len(list_of_numbers) < 1:
        return total

    for value in list_of_numbers:
        total += value

    return total
