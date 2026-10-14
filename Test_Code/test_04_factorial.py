
import runpy

program = runpy.run_path("Code/04_factorial.py")
factorial = program["factorial"]

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(4) == 24
assert factorial(-2) is None

print("All test cases passed.")
