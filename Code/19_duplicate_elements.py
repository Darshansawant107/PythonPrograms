
def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))
