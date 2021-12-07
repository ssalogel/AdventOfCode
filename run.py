from AoC2015 import Days as d2015
from AoC2016 import Days as d2016
from AoC2021 import Days as d2021
from time import perf_counter


# t0 = perf_counter()
# for day in d2015.get_all_days():
#     day().run()
# t1 = perf_counter()
# print(f"2015 done in : {t1 - t0:.3} seconds\n")
"""
t0 = perf_counter()
for day in d2016.get_fast_days():
    day().run()
t1 = perf_counter()
print(f"2016 done in : {t1 - t0:.3} seconds\n")
"""
t0 = perf_counter()
for day in d2021.get_fast_days():
    day().run()
t1 = perf_counter()
print(f"2021 done in : {t1 - t0:.3} seconds\n")
