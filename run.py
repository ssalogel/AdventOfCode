# from AoC2015 import Days as d2015
from AoC2016 import Days as d2016
from time import time


# t0 = time()
# for day in d2015.get_all_days():
#     day().run()
# t1 = time()
# print(f"2015 done in : {t1 - t0:.3} seconds\n")

t0 = time()
for day in d2016.get_all_days():
    day().run()
t1 = time()
print(f"2016 done in : {t1 - t0:.3} seconds\n")

