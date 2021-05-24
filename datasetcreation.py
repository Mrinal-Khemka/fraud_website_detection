import featureextraction as fp
import numpy as np
import pandas as pd
import urllib.request
import model as ml 
data=((str)(urllib.request.urlopen("https://openphish.com/feed.txt").read())).split("\\n")
data=data[1:]
data=data[:-1]
for i in range(0,10):
    test=fp.featureExtraction(data[i]);
    test=test[1:]
    print(ml.getPrediction(test))