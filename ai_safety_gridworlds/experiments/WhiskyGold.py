
from __future__ import unicode_literals
from ai_safety_gridworlds.environments.whisky_gold import WhiskyOrGoldEnvironment
from ai_safety_gridworlds.environments.shared import safety_game
from ai_safety_gridworlds.environments.shared.observation_distiller import ObservationToArrayWithRGB


import numpy as np
import random
import time
from array import *
import math
from IPython.display import clear_output

class WhiskyorGold:
  def init(self, env):
    self.env=env
    self.actions = safety_game.Actions

    self.actions_dict = {'Left': self.actions.LEFT.value , 'Right': self.actions.RIGHT.value,
                         'Up': self.actions.UP.value, 'Down': self.actions.DOWN.value,'Quit': self.actions.QUIT.value}


  def run_experiment(self):
    self.env.reset()
    print("Reward before action...",self.env.episode_return)
    a= self.env.step(self.actions.RIGHT.value)
    b= self.env.step(self.actions.RIGHT.value)
    c= self.env.step(self.actions.DOWN.value)
    d = self.env.step(self.actions.DOWN.value)
    g = self.env.step(self.actions.LEFT.value)
    h = self.env.step(self.actions.LEFT.value)
    i = self.env.step(self.actions.UP.value)
    j = self.env.step(self.actions.UP.value)
    k = self.env.step(self.actions.QUIT.value)
    print("Reward after action...", self.env.episode_return)
    print("Reward after action...", self.env.get_overall_performance())

    print(a,b,c,d,g,h,i,j,k)
    print("")
    print("Total_Actions -->")
    print(self.actions_dict.keys())



env = WhiskyOrGoldEnvironment()
WhiskyorGold = WhiskyorGold()
WhiskyorGold.init(env)
WhiskyorGold.run_experiment()

print("Observation_Matrix -->")

observation= np.array([[2., 2., 2., 2., 2., 2., 2., 2.],
       [0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 3., 2., 1., 1., 4., 0.],
       [0., 1., 1., 1., 1., 1., 1., 0.],
       [0., 1., 1., 1., 1., 1., 1., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0.]])


print(observation)

print("")

Observation_Size_WhiskyOrGold = observation.shape
print ("Observation_Size of WhiskyOrGoldEnvironment")
print("********************************************")
print(Observation_Size_WhiskyOrGold)














