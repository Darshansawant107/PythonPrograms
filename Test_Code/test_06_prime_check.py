
import runpy

program = runpy.run_path("Code/06_prime_check.py")
is_prime = program["is_prime"]

assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(7) == True
assert is_prime(1) == False
assert is_prime(0) == False
assert is_prime(-5) == False
assert is_prime(17) == True

print("All test cases passed.")
