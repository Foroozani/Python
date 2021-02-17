## run.py
print('------------ run says hi --------------------\n')
import timing
code = "[x**2 for x in range(1_000)]"
results = timing.timeit(code, repeats= 100)
print(results)