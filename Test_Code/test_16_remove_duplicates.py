
import runpy

program = runpy.run_path("Code/16_remove_duplicates.py")
remove_duplicates = program["remove_duplicates"]

assert remove_duplicates([1, 2, 2, 3, 4, 3, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([3, 2, 3, 1, 2]) == [3, 2, 1]
assert remove_duplicates([0, 0, -1, -1]) == [0, -1]

print("All test cases passed.")

