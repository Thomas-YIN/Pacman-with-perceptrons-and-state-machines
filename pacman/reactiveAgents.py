# reactiveAgents.py
# ---------------
# Licensing Information: You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC
# Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from sympy import N
from game import Directions
from game import Agent
from game import Actions
import util
import time
import search
import pandas as pd
import numpy as np

class NaiveAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        sense = state.getPacmanSensor()
        if sense[7]:
            action = Directions.STOP
        else:
            action = Directions.WEST
        return action

class PSAgent(Agent):
    "An agent that follows the boundary using production system."

    def getAction(self, state):
        sense = state.getPacmanSensor()
        x = [sense[1] or sense[2] , sense[3] or sense[4] ,
        sense[5] or sense[6] , sense[7] or sense[0]]
        if x[0] and not x[1]:
            action = Directions.EAST
        elif x[1] and not x[2]:
            action = Directions.SOUTH
        elif x[2] and not x[3]:
            action = Directions.WEST
        elif x[3] and not x[0]:
            action = Directions.NORTH
        else:
            action = Directions.NORTH
        return action

class ECAgent(Agent):
    "An agent that follows the boundary using error-correction."
    def __init__(self):
        self.weights = pd.read_csv("~/Desktop/COMP3211 hw1/pacman/weights.csv", index_col=0)
    def getAction(self, state):
        ''' @TODO: Your code goes here! '''
        labels = [0,0,0,0]
        inputs = state.getPacmanSensor()
        inputs.append(-1)
        #print("sensor", inputs)
        #print(self.weights)
        for i in range(4):
            labels[i] = np.dot(self.weights.iloc[i], inputs)
        #print("label value", labels)
        if labels[0]>=0 & inputs[1] == 0:
            #print("instructed north")
            return Directions.NORTH
        elif labels[1]>=0 & inputs[3] == 0:
            #print("instructed east")
            return Directions.EAST
        elif labels[2]>=0 & inputs[5] == 0:
            return Directions.SOUTH
        elif labels[3]>=0 & inputs[7] == 0:
            return Directions.WEST
        else: 
            #print("all 0")
            return Directions.NORTH
        #return Directions.NORTH

class SMAgent(Agent):
    "An sensory-impaired agent that follows the boundary using state machine."
    def registerInitialState(self,state):
        "The agent receives the initial GameState (defined in pacman.py)."
        sense = state.getPacmanImpairedSensor() 
        self.prevAction = Directions.STOP
        self.prevSense = sense

    def getAction(self, state):
        '''@TODO: Your code goes here! '''        
        w = np.zeros(8, dtype=int)
        sense = state.getPacmanImpairedSensor() 
        for i in range(1, 8, 2):
            w[i] = sense[int(i/2)]
        prevSense = self.prevSense
        prevAction = self.prevAction

        w[0] = 1 if (self.prevSense[0]==1)&(self.prevAction==Directions.EAST) else 0
        w[2] = 1 if (self.prevSense[1]==1)&(self.prevAction==Directions.SOUTH) else 0
        w[4] = 1 if (self.prevSense[2]==1)&(self.prevAction==Directions.WEST) else 0
        w[6] = 1 if (self.prevSense[3]==1)&(self.prevAction==Directions.NORTH) else 0

        #Production system
        if w[1] & (not w[3]): action = Directions.EAST
        elif w[3] & (not w[5]): action = Directions.SOUTH
        elif w[5] & (not w[7]): action = Directions.WEST
        elif w[7] & (not w[1]): action = Directions.NORTH

        elif w[0]: action = Directions.NORTH
        elif w[2]: action = Directions.EAST
        elif w[4]: action = Directions.SOUTH
        elif w[6]: action = Directions.WEST
        else: action = Directions.NORTH
        
        self.prevSense = sense
        self.prevAction = action

        #return Directions.NORTH
