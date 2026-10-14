
import runpy

program = runpy.run_path("Code/08_reverse_number.py")
reverse_number = program["reverse_number"]

assert reverse_number(12345) == 54321
assert reverse_number(123) == 321
assert reverse_number(100) == 1
assert reverse_number(7) == 7
assert reverse_number(0) == 0
assert reverse_number(-123) == -321

print("All test cases passed.")
