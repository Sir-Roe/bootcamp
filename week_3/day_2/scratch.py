import csv
import numpy as np

with open(r"C:\Users\logan\Documents\GitHub\bootcamp\week_3\day_2\redsox_2017_hitting.txt") as f:
    data2017 = f.read()
    f.close()

with open(r"C:\Users\logan\Documents\GitHub\bootcamp\week_3\day_2\redsox_2018_hitting.txt") as f:
    data2018 = f.read()
    f.close()

shape = (3,3)
arr_1 = np.array([1,2,3])



print(arr2)