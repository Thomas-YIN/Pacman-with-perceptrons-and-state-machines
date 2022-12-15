# Pacman with production systems, perceptrons, and state machines

## Project description
This is a simple exercise to implement the boundary following production systems in the
Pacman game from UC Berkeley. The goal of the Pacman game is simple: control the
Pacman to eat all the foods in the map, as shown below.

<img src="/images/pacman.png" alt="pacman game" style="height: 300px;"/>

## Different type of agents
- NaiveAgent: The agent goes west until it cannot.
- PSAgent: The agent moves according to a pre-defined production system.
- [ECAgent](ecagent): The agent moves according to a perceptron trained using the error-correction method.
- [SMAgent](smagent): The agent decides the next move by its impaired sensors along with its knowledge on the previous move.

<a name="ecagent"/>
<a name="smagent"/>

## ECAgent

## SMAgent
