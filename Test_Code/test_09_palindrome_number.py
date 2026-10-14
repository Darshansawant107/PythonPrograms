
import runpy

program = runpy.run_path("Code/09_palindrome_number.py")
is_palindrome = program["is_palindrome"]

assert is_palindrome(121) == True
assert is_palindrome(123) == False
assert is_palindrome(1221) == True
assert is_palindrome(7) == True
assert is_palindrome(0) == True
assert is_palindrome(-121) == False

print("All test cases passed.")
