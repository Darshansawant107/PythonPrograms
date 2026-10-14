
import runpy

program = runpy.run_path("Code/11_count_vowels_consonants.py")
count_vowels_consonants = program["count_vowels_consonants"]

assert count_vowels_consonants("Hello World") == (3, 7)
assert count_vowels_consonants("AEIOU") == (5, 0)
assert count_vowels_consonants("BCDF") == (0, 4)
assert count_vowels_consonants("123 !") == (0, 0)
assert count_vowels_consonants("") == (0, 0)

print("All test cases passed.")
