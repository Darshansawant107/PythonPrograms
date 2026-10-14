
import runpy

program = runpy.run_path("Code/20_word_frequency.py")
word_frequency = program["word_frequency"]

assert word_frequency("python is easy and python is powerful") == {
    "python": 2,
    "is": 2,
    "easy": 1,
    "and": 1,
    "powerful": 1
}
assert word_frequency("hello hello world") == {
    "hello": 2,
    "world": 1
}
assert word_frequency("") == {}
assert word_frequency("Python python PYTHON") == {
    "python": 3
}
assert word_frequency("one") == {"one": 1}

print("All test cases passed.")
