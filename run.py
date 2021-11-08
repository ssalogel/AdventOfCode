from AoC2015 import Days as d2015
from time import time


t0 = time()
for day in d2015.get_fast_days():
    day().run()
t1 = time()
print(f"2015 done in : {t1 - t0:.3} seconds\n")
