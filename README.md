# Beehive Evolution Simulation

Welcome to the Beehive Evolution Simulation project, where we take inspiration from the fascinating behavior of bees in a flower-rich environment. In this README, we will provide a comprehensive overview of the project, its requirements, usage, and key components.

## Table of Contents

- [Project Introduction](#project-introduction)
- [Project Requirements](#project-requirements)
- [How to Use](#how-to-use)
  - [Genetic Algorithm](#genetic-algorithm)
  - [Project Components](#project-components)
- [Conclusion](#conclusion)

## Project Introduction

In this project, we simulate the evolution of a colony of bees residing in a wild apple tree, surrounded by a lush field of melliferous flowers. The colony initially comprises 101 bees, including a queen bee. Their primary objective is to forage for pollen, a vital food source for the queen and bee larvae.

As the bees venture into the flower-filled meadow, their foraging decisions are crucial. The bees with the fastest pollen-gathering strategies will have the opportunity to pass on their knowledge to the next generation. Meanwhile, slower bees will be replaced, maintaining the colony's size at 100 individuals, including the queen.

With the help of a genetic algorithm, we computationally represent the evolution of the bee colony's knowledge of the flower field over generations. We aim to fine-tune the algorithm parameters through comparative analysis, including mutation rate, fixed vs. evolving mutation rates, reproduction rate, reproduction system, and fitness calculation metrics.

## Project Requirements

Before you begin, please ensure you have the following dependencies installed:

- Python (version 3.7 or higher)
- NumPy (version 1.23.5)
- Random (standard library)
- Matplotlib (version 3.7.1)
- Pandas (version 2.0.2)

You can easily install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## How to Use

To utilize this bee colony evolution simulation, follow these steps:

### Genetic Algorithm

1. Execute the `main.py` file to initiate the genetic algorithm simulation.

### Project Components

This project comprises several essential components:

- **Simulation of Bee Behavior**: The genetic algorithm simulates the bees' behavior in collecting pollen from flowers. Bees represent potential solutions, while flowers serve as attractive points.

- **Bee Population**: The population consists of bees, each with a unique strategy represented as an array of flowers. The initial population is randomly generated.

- **Evolutionary Process**: Bees evolve across generations through selection of the best-performing bees. Breeding occurs to create the next generation, with the possibility of mutation based on performance differences between generations.

- **Performance Evaluation**: The fitness of each bee is evaluated according to a specific problem or objective function. The ultimate goal is to optimize this function over multiple generations.

- **Data Logging**: The simulation records performance data, such as average scores, for each generation. The data is stored in CSV files for further analysis.

## Conclusion

The Beehive Evolution Simulation project offers a computational exploration of a bee colony's evolution as it interacts with a rich field of flowers. By running the `main.py` script, users can observe the gradual improvement of the colony's foraging strategies across multiple generations. This project provides a valuable tool for studying the dynamics of evolution in complex systems.