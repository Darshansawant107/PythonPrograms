
import runpy

program = runpy.run_path("Code/17_common_elements.py")
common_elements = program["common_elements"]

assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
assert common_elements([1, 2], [3, 4]) == []
assert common_elements([], [1, 2]) == []
assert common_elements([1, 1, 2], [1, 2]) == [1, 2]
assert common_elements([5, 3, 1], [1, 5]) == [5, 1]

print("All test cases passed.")
