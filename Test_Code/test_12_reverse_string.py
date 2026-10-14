
import runpy

program = runpy.run_path("Code/12_reverse_string.py")
reverse_string = program["reverse_string"]

assert reverse_string("Python") == "nohtyP"
assert reverse_string("hello") == "olleh"
assert reverse_string("a") == "a"
assert reverse_string("") == ""
assert reverse_string("12345") == "54321"
assert reverse_string("hello world") == "dlrow olleh"

print("All test cases passed.")
