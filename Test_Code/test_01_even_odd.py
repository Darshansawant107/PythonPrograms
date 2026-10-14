
import runpy

program = runpy.run_path("Code/01_even_odd.py")
check_even_odd = program["check_even_odd"]

assert check_even_odd(4) == "Even"
assert check_even_odd(7) == "Odd"
assert check_even_odd(0) == "Even"
assert check_even_odd(-2) == "Even"

print("All test cases passed.")
