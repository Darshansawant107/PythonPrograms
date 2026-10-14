
import runpy

program = runpy.run_path("Code/19_duplicate_elements.py")
find_duplicates = program["find_duplicates"]

assert find_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2]
assert find_duplicates([1, 1, 1]) == [1]
assert find_duplicates([1, 2, 3]) == []
assert find_duplicates([]) == []
assert find_duplicates([4, 3, 4, 3, 2]) == [4, 3]
assert find_duplicates([0, 0, -1, -1]) == [0, -1]

print("All test cases passed.")
