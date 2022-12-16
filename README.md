# Boundary-following Pacman with perceptrons and state machines

## Project description
This is a simple exercise to implement the boundary following production systems in the
Pacman game from UC Berkeley. The goal of the Pacman game is simple: control the
Pacman to eat all the foods in the map, as shown below.

<img src="/images/pacman.png" alt="pacman game" style="height: 300px;"/>

## Different types of agents
- NaiveAgent: The agent goes west until it cannot.
- PSAgent: The agent moves according to a pre-defined production system.
- [ECAgent](#ecagent): The agent moves according to a perceptron trained using the error-correction method.
- [SMAgent](#smagent): The agent decides the next move by its impaired sensors along with its knowledge on the previous move.

<a name="ecagent"/>

## ECAgent (error-correction agent)
The `ECAgent`'s action is determined by a single layer perceptron  trained on the four training sets named `north.csv`, `east.csv`, `south.csv`, and `west.csv`. Each file stores the environment states when moving north, east, south, and west. Each vector in the training set is in the form of $(s_1,...,s_8,d)$, where the first $8$ elements are the Pacman’s sensor readings, and $d$ is the label of this input, with $d = 1$ meaning a positive, and $0$ a negative example.

<a name="smagent"/>

## SMAgent (state machine agent)
The `SMAgent` is sensory-impaired and can only received only 4 sensor inputs from the 4 directions: north, east, south, west. The agent receives sensor values from the `getPacmanImpairedSensor` function. The sensory input $(s_2, s_4, s_6, s_8)$ corresponds to the sensor values from the north, east, south, and west respectively. The `SMAgent` can remember the previous action `prevAction` and the previous sensory input `prevSense`. The agent moves according to a production system based on previous and current senses, as well as the previous move.

## How to run the game



