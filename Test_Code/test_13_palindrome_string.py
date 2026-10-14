
import runpy

program = runpy.run_path("Code/13_palindrome_string.py")
is_palindrome = program["is_palindrome"]

assert is_palindrome("madam") == True
assert is_palindrome("hello") == False
assert is_palindrome("Racecar") == True
assert is_palindrome("a") == True
assert is_palindrome("") == True
assert is_palindrome("Python") == False

print("All test cases passed.")
