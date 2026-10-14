import runpy

program = runpy.run_path("Code/03_positive_negative_zero.py")
check_number = program["check_number"]

assert check_number(10) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(0) == "Zero"
assert check_number(100) == "Positive"
assert check_number(-100) == "Negative"

print("All test cases passed.")