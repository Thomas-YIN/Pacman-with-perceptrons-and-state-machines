import pandas as pd
import numpy as np

dfEast = pd.read_csv("~/Desktop/COMP3211 hw1/east.csv", header=None)
dfWest = pd.read_csv("~/Desktop/COMP3211 hw1/west.csv", header=None)
dfNorth = pd.read_csv("~/Desktop/COMP3211 hw1/north.csv", header=None)
dfSouth = pd.read_csv("~/Desktop/COMP3211 hw1/south.csv", header=None)

def clean(df):
    data = np.array(df)
    threshold = np.full(shape=7, dtype=float, fill_value=-1)
    data = np.insert(data, 8, threshold, axis=1)
    return data

east = clean(dfEast)
west = clean(dfWest)
north = clean(dfNorth)
south = clean(dfSouth)

def func(x):
    if(x >= 0): return 1
    else: return 0

#Assign initial weight
#initWeight = np.zeros(shape=8, dtype=int)
#weight = np.full(shape=8, dtype=float, fill_value=1/8)
#initWeight = np.append(initWeight ,-1)
#print(weight)

#Learning rate
c = 1
MAX_ITER = 5000

def train(data, weight):

    iter = 0
    while(iter<MAX_ITER):
        correct = 0
        for i in range(data.shape[0]):
            d = data[i, -1]
            X = data[i,:-1]
            f = func(np.inner(weight, X))
            if(f == d): correct += 1
            #print("Iteration", iter)
            weight += c*(d - f)*X
            #print(weight, '\n')
            
        if correct == data.shape[0]: 
            #break
            return weight
        iter+=1
        
    #print("Final:",weight)
    #return weight

north_w = train(north, [0,0,0,0,0,0,0,0,-1])
#north_w = train(north, [1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8,-1])
east_w = train(east, [0,0,0,0,0,0,0,0,-1])
#east_w = train(east, [1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8,-1])
south_w = train(south, [0,0,0,0,0,0,0,0,-1])
#south_w = train(south, [1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8,-1])
west_w = train(west, [0,0,0,0,0,0,0,0,-1])
#west_w = train(west, [1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8,-1])

weights = np.array([north_w, east_w, south_w, west_w])
pd.DataFrame(weights).to_csv("~/Desktop/COMP3211 hw1/pacman/weights.csv")


