
import runpy

program = runpy.run_path("Code/10_sum_of_digits.py")
sum_of_digits = program["sum_of_digits"]

assert sum_of_digits(1234) == 10
assert sum_of_digits(555) == 15
assert sum_of_digits(0) == 0
assert sum_of_digits(9) == 9
assert sum_of_digits(1001) == 2
assert sum_of_digits(-123) == 6

print("All test cases passed.")
