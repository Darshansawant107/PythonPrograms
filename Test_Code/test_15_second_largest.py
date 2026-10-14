
import runpy

program = runpy.run_path("Code/15_second_largest.py")
second_largest = program["second_largest"]

assert second_largest([10, 20, 5, 8, 25]) == 20
assert second_largest([5, 5, 3]) == 3
assert second_largest([-1, -5, -3]) == -3
assert second_largest([1, 2]) == 1
assert second_largest([7, 7, 7]) is None
assert second_largest([10]) is None

print("All test cases passed.")
