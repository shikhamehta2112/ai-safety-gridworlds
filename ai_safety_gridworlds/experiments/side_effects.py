from ai_safety_gridworlds.environments.side_effects_sokoban import SideEffectsSokobanEnvironment
from ai_safety_gridworlds.environments.shared import safety_game
import numpy as np
import random
import time
from IPython.display import clear_output

class Side_effects:
  def init(self, env):
    self.env=env
    self.actions = safety_game.Actions

    self.actions_dict = {'Left': self.actions.LEFT.value, 'Right': self.actions.RIGHT.value,
                         'Up': self.actions.UP.value, 'Down': self.actions.DOWN.value, 'Quit': self.actions.QUIT.value}

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

    print(self.actions_dict)
    print(self.actions_dict.keys())

#engine = boat_race.make_game({})
env = SideEffectsSokobanEnvironment()
Side_effects = Side_effects()
Side_effects.init(env)
Side_effects.run_experiment()

print("Observation_Matrix -->")

observation= np.array([[0., 0., 0., 0., 0., 0.],
       [0., 2., 1., 0., 0., 0.],
       [0., 1., 1., 1., 1., 0.],
       [0., 0., 4., 1., 1., 0.],
       [0., 0., 0., 1., 5., 0.],
       [0., 0., 0., 0., 0., 0.]])


print(observation)

print("")

Observation_Size_SideEffectsSokoban = observation.shape
print ("Observation_Size of SideEffectsSokobanEnvironment")
print("********************************************")
print(Observation_Size_SideEffectsSokoban)

























