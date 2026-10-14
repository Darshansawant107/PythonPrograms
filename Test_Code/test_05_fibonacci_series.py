
import runpy

program = runpy.run_path("Code/05_fibonacci_series.py")
fibonacci_series = program["fibonacci_series"]

assert fibonacci_series(0) == []
assert fibonacci_series(1) == [0]
assert fibonacci_series(2) == [0, 1]
assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
assert fibonacci_series(5) == [0, 1, 1, 2, 3]

print("All test cases passed.")
