import json
import os
from collections import OrderedDict

class Trailer(object):

    jsonfiles = ["../data/trailer-A.json", "../data/trailer-D.json"]
    splits = [[(0.00, 228.00), (228.00, 434.00)], [(0.00, 212.00), (212.00, 418.00)]]

    def __init__(self, jsonpaths=["../data/trailer-D.json"]):
        self.jsonpaths = jsonpaths

    def load_and_split(self, splits):
        data = []
        for i, jsonp in enumerate(self.jsonpaths):
            tmp = self.load_json(jsonp)
            start_time = min(tmp.keys())
            splt = splits[i].pop(0)
            run_data = []
            for k, v in tmp.items():
                ts = (k - start_time) / 1000
                if ts > splt[1]:
                    if len(splits[i]) > 0:
                        data.append(OrderedDict(run_data))
                        run_data = []
                        splt = splits[i].pop(0)
                    else:
                        break
                run_data.append((k, v))
            data.append(OrderedDict(run_data))
        return data


    def load_json(self, jsonpath):
        with open(jsonpath, "r") as f:
            raw = f.readlines()

        data = {}
        timestamps = []

        for item in raw:
            item = json.loads(item)
            ts = item["timestamp"]
            sen = item["sensorType"]
            if not ts in data:
                data[ts] = {}
                timestamps += [ts]
            if not sen in data[ts]:
                data[ts][sen] = {}
            data[ts][sen]["values"] = item["values"]
            data[ts][sen]["loc"] = item["sensorLocation"]
        timestamps.sort()
        data = OrderedDict([(k, data[k]) for k in timestamps])
        return data
