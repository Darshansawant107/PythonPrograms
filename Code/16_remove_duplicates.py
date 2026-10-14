
def remove_duplicates(numbers):
    result = []

    for number in numbers:
        if number not in result:
            result.append(number)

    return result


print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))
