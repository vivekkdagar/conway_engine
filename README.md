<div align='center'>

# Game Of Life

Welcome to the `conway_engine`, a visual representation of Conway's Game of Life—a cellular automaton designed by mathematician John Conway. This package showcases a grid of cells that evolve over time based on specific rules, resulting in intriguing patterns and behaviors.

<h4> <span> · </span> <a href="https://github.com/vivekkdagar/conway_engine/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/vivekkdagar/conway_engine/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/vivekkdagar/conway_engine/issues"> Request Feature </a> </h4>

</div>

# :notebook_with_decorative_cover: Table of Contents

1. [Screenshots](#demo-screenshot)
2. [Requirements](#requirements)
3. [Features](#dart-features)
4. [Usage](#toolbox-usage)
5. [Keyboard Commands](#keyboard-commands)
6. [FAQ](#grey_question-faq)
7. [Acknowledgements](#gem-acknowledgements)

# 📷 Demo Screenshot
<div align="center"> <a href="#demo-screenshot"><img src="https://github.com/vivekkdagar/conway_engine/blob/main/assets/Demo%202.png" alt='image' width='600'/></a> </div>

## :star2: Requirements

Ensure you meet the following requirements before installation:

- **Python**: The simulation is written in Python. Download and install Python from [python.org](https://www.python.org/).
- **Pygame**: The Pygame library is used for graphics and interaction. Install it using:

  ```bash
  pip install pygame
  ```

## :dart: Features

- **Gosper Glider Gun**: Experience the inclusion of the renowned Gosper Glider Gun, a pattern triggering gliders in a repeating sequence, resulting in explosive growth.
- **Dynamic Visualization**: Observe a window displaying the evolving patterns of cells over time, creating visually striking designs.
- **Interactive Controls**: Interact with the simulation by toggling cell states with mouse clicks and using keyboard commands to control the simulation.

## :toolbox: Usage

### :running: Run Locally

Clone the project
```bash
git clone <repository_url>
```

Navigate to the root directory of the cloned repository.
```bash
cd conway_engine
```

Build the package using the commands below.
```bash
python3 setup.py sdist bdist_wheel
```
Install the package using pip.
```bash
pip install dist/*.tar.gz
```

## :keyboard: Keyboard Commands

- Spacebar: Start/Pause the simulation.
- 'c' Key: Clear the grid.
- 'g' Key: Generate a random set of cells for explosive growth.
- Mouse Left Click: Toggle the state of a cell.
- Mouse Right Click: Remove a cell.

## :grey_question: FAQ

- #### Q1: What is the Game of Life by John Conway?
  - The Game of Life is a cellular automaton created by mathematician John Conway. It consists of a two-dimensional grid where each cell can be alive or dead. The evolution of the grid is determined by simple rules, including underpopulation, survival, overpopulation, and reproduction.

- #### Q2: What are the rules of the Game of Life?
  - The rules of the Game of Life are: Underpopulation, Survival, Overpopulation, and Reproduction. These simple rules give rise to a variety of patterns, including stable structures, oscillators, and gliders, making the Game of Life a fascinating and widely studied cellular automaton.

## :gem: Acknowledgements

- [Pygame Library](https://pypi.org/project/pygame/): Leveraging the Pygame library for graphics and user interaction streamlines the development of the Game of Life simulation, providing a robust framework for handling events, drawing the grid, and creating an engaging visual experience for users.

- [John Conway's Game of Life](https://en.wikipedia.org/wiki/John_Horton_Conway/): The entire codebase is built upon the principles of John Conway's Game of Life. The rules governing cell evolution, the grid-based structure, and the concept of cellular automata are all inspired by Conway's seminal work in the field of mathematical games and automata theory.

- [Gosper Glider Gun Pattern](https://conwaylife.com/wiki/Gosper_glider_gun): The implementation of the Gosper glider gun pattern, a well-known configuration in Conway's Game of Life, adds complexity and visual interest to the simulation. The Gosper glider gun is famous for generating gliders, which contribute to the emergence of diverse patterns and behaviors.

- [GenReadme](https://www.genreadme.cloud/): Used GenReadme to generate documentation effectively and efficiently.

