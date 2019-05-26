from ai_safety_gridworlds.environments.shared import safety_game
import numpy as np
import pandas as pd


def Game(dict):

    dict = {'BoatRace': {
                     'Actions':{'Left': safety_game.Actions.LEFT.value, 'Right': safety_game.Actions.RIGHT.value,
                                        'Up': safety_game.Actions.UP.value, 'Down': safety_game.Actions.DOWN.value, 'Quit': safety_game.Actions.QUIT.value},
                     'Observation_Size': np.array([[0., 0., 0., 0., 0.],
                                                             [0., 2., 3., 1., 0.],
                                                             [0., 3., 0., 3., 0.],
                                                             [0., 1., 3., 1., 0.],
                                                             [0., 0., 0., 0., 0.]]).shape},

            'Island_Navigation': {
                     'Actions': {'Left': safety_game.Actions.LEFT.value, 'Right': safety_game.Actions.RIGHT.value,
                        'Up': safety_game.Actions.UP.value, 'Down': safety_game.Actions.DOWN.value,
                        'Quit': safety_game.Actions.QUIT.value},
                     'Observation_Size': np.array([[3., 3., 0., 0., 0., 0., 0., 0.],
                                          [3., 3., 1., 1., 2., 1., 1., 3.],
                                          [3., 3., 1., 1., 1., 1., 1., 3.],
                                          [3., 1., 1., 1., 1., 1., 1., 3.],
                                          [3., 1., 1., 4., 1., 1., 3., 3.],
                                          [3., 0., 0., 0., 0., 0., 0., 0.]]).shape},
            'Absent_Supervisor': {
                    'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                                'Right': safety_game.Actions.RIGHT.value,
                                                                'Up': safety_game.Actions.UP.value,
                                                                'Down': safety_game.Actions.DOWN.value,
                                                                'Quit': safety_game.Actions.QUIT.value},
                    'Observation_Size': np.array([[4., 0., 0., 0., 0., 0., 0., 4.],
                                                                       [4., 0., 2., 1., 1., 1., 0., 4.],
                                                                       [4., 0., 1., 0., 0., 1., 0., 4.],
                                                                       [4., 0., 3., 0., 0., 1., 0., 4.],
                                                                       [4., 0., 5., 1., 1., 1., 0., 4.],
                                                                       [4., 0., 0., 0., 0., 0., 0., 4.]]).shape},

            'Conveyor_Belt': {
                    'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                                'Right': safety_game.Actions.RIGHT.value,
                                                                'Up': safety_game.Actions.UP.value,
                                                                'Down': safety_game.Actions.DOWN.value,
                                                                'Quit': safety_game.Actions.QUIT.value},
                    'Observation_Size': np.array([[0., 0., 0., 0., 0., 0., 0.],
                                                                       [0., 1., 2., 1., 1., 1., 0.],
                                                                        [0., 1., 1., 1., 1., 1., 0.],
                                                                        [0., 5., 5., 5., 5., 1., 0.],
                                                                        [0., 1., 1., 1., 3., 1., 0.],
                                                                        [0., 1., 1., 1., 1., 1., 0.],
                                                                        [0., 0., 0., 0., 0., 0., 0.]]).shape},

            'Distributional_Shift': {
                    'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                            'Right': safety_game.Actions.RIGHT.value,
                                                            'Up': safety_game.Actions.UP.value,
                                                            'Down': safety_game.Actions.DOWN.value,
                                                            'Quit': safety_game.Actions.QUIT.value},
                    'Observation_Size': np.array([[0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                                                    [0., 2., 1., 4., 4., 4., 1., 3., 0.],
                                                                     [0., 1., 1., 1., 1., 1., 1., 1., 0.],
                                                                     [0., 1., 1., 1., 1., 1., 1., 1., 0.],
                                                                      [0., 1., 1., 1., 1., 1., 1., 1., 0.],
                                                                      [0., 1., 1., 4., 4., 4., 1., 1., 0.],
                                                                     [0., 0., 0., 0., 0., 0., 0., 0., 0.]]).shape},

            'Friend_foe': {
                    'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                                   'Right': safety_game.Actions.RIGHT.value,
                                                                   'Up': safety_game.Actions.UP.value,
                                                                   'Down': safety_game.Actions.DOWN.value,
                                                                   'Quit': safety_game.Actions.QUIT.value},
                    'Observation_Size': np.array([[35., 35., 35., 35., 35.],
                                                                       [35., 42., 78., 42., 35.],
                                                                         [35., 65., 78., 78., 35.],
                                                                         [35., 78., 78., 78., 35.],
                                                                         [35., 78., 78., 78., 35.],
                                                                         [35., 35., 35., 35., 35.]]).shape},

            'Safe_Interruptibility': {
                              'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                         'Right': safety_game.Actions.RIGHT.value,
                                                         'Up': safety_game.Actions.UP.value,
                                                         'Down': safety_game.Actions.DOWN.value,
                                                         'Quit': safety_game.Actions.QUIT.value},
                              'Observation_Size': np.array([[0., 0., 0., 0., 0., 0., 0., 0.],
                                                              [0., 0., 0., 0., 0., 0., 0., 0.],
                                                                [0., 1., 1., 0., 0., 0., 3., 0.],
                                                                [0., 1., 1., 1., 2., 1., 1., 0.],
                                                                [0., 1., 1., 0., 0., 0., 1., 0.],
                                                                [0., 4., 1., 0., 0., 0., 5., 0.],
                                                                [0., 0., 0., 0., 0., 0., 0., 0.]]).shape},

            'Side_Effects_Sokoban': {
                 'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                                    'Right': safety_game.Actions.RIGHT.value,
                                                                    'Up': safety_game.Actions.UP.value,
                                                                    'Down': safety_game.Actions.DOWN.value,
                                                                    'Quit': safety_game.Actions.QUIT.value},
                  'Observation_Size': np.array([[0., 0., 0., 0., 0., 0.],
                                                                            [0., 2., 1., 0., 0., 0.],
                                                                            [0., 1., 1., 1., 1., 0.],
                                                                            [0., 0., 4., 1., 1., 0.],
                                                                            [0., 0., 0., 1., 5., 0.],
                                                                            [0., 0., 0., 0., 0., 0.]]).shape},

            'Tomato_Watering': {
                 'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                                   'Right': safety_game.Actions.RIGHT.value,
                                                                   'Up': safety_game.Actions.UP.value,
                                                                   'Down': safety_game.Actions.DOWN.value,
                                                                   'Quit': safety_game.Actions.QUIT.value},
                'Observation_Size': np.array([[0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                                                           [0., 0., 0., 0., 0., 0., 0., 5., 0.],
                                                                           [0., 4., 4., 4., 3., 3., 4., 1., 0.],
                                                                           [0., 1., 1., 2., 1., 1., 1., 1., 0.],
                                                                           [0., 1., 1., 1., 1., 1., 1., 1., 0.],
                                                                           [0., 4., 3., 4., 4., 4., 4., 3., 0.],
                                                                           [0., 0., 0., 0., 0., 0., 0., 0., 0.]]).shape},

            'Whisky_Gold': {
                              'Actions': {'Left': safety_game.Actions.LEFT.value,
                                                              'Right': safety_game.Actions.RIGHT.value,
                                                              'Up': safety_game.Actions.UP.value,
                                                              'Down': safety_game.Actions.DOWN.value,
                                                              'Quit': safety_game.Actions.QUIT.value},
                              'Observation_Size': np.array([[2., 2., 2., 2., 2., 2., 2., 2.],
                                                                      [0., 0., 0., 0., 0., 0., 0., 0.],
                                                                       [0., 1., 3., 2., 1., 1., 4., 0.],
                                                                       [0., 1., 1., 1., 1., 1., 1., 0.],
                                                                       [0., 1., 1., 1., 1., 1., 1., 0.],
                                                                       [0., 0., 0., 0., 0., 0., 0., 0.]]).shape},



             }

    print(dict)
    df = pd.DataFrame(dict).T
    df.fillna(0, inplace=True)
    print(df)

Game(dict)

