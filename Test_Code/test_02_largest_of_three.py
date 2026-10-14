
import runpy

program = runpy.run_path("Code/02_largest_of_three.py")
largest_of_three = program["largest_of_three"]

assert largest_of_three(10, 25, 15) == 25
assert largest_of_three(50, 20, 30) == 50
assert largest_of_three(10, 20, 30) == 30
assert largest_of_three(-5, -2, -10) == -2
assert largest_of_three(7, 7, 3) == 7

print("All test cases passed.")

