import datetime
import torch
import numpy as np
import matplotlib.pyplot as plt
from load import Trailer

def get_ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000)

SENSORS = ["ACCELEROMETER", "GYROSCOPE", "TEMPERATURE", "MAGNETOMETER", "LIGHT"] # ["BAROMETER"]
MEANCENTER = set(["MAGNETOMETER"])
NORM = set(["MAGNETOMETER"])
LOGSENS = set(["LIGHT"])

jsonfiles = ["../data/trailer-A.json", "../data/trailer-D.json"]
splits = [[(0.00, 228.00), (228.00, 434.00)], [(0.00, 212.00), (212.00, 418.00)]]
trailers = Trailer(jsonfiles)
data = trailers.load_and_split(splits)
print([len(d) for d in data])
