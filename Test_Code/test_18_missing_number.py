
import runpy

program = runpy.run_path("Code/18_missing_number.py")
find_missing_number = program["find_missing_number"]

assert find_missing_number([1, 2, 4, 5], 5) == 3
assert find_missing_number([2, 3, 4, 5], 5) == 1
assert find_missing_number([1, 2, 3, 4], 5) == 5
assert find_missing_number([1, 3], 3) == 2
assert find_missing_number([], 1) == 1

print("All test cases passed.")
