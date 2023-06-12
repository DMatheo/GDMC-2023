import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

LOOTS_IN_BARRELS = {"dirt":0.85, "iron":0.08, "gold":0.02, "diamond":0.0025, "emerald":0.0025, "coal":0.03, "redstone":0.0025, "lapis":0.0025, "quartz":0.005, "obsidian":0.004, "netherite":0.001}
    

total_probability = sum(LOOTS_IN_BARRELS.values())

print("The sum of all probabilities is:", total_probability)