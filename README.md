<div align='center'>

<h1>Game Of Life</h1>
<p>Welcome to the conway_engine, a visual representation of Conway's Game of Life—a cellular automaton designed by mathematician John Conway. This package showcases a grid of cells that evolve over time based on specific rules, resulting in intriguing patterns and behaviors.</p>

<h4> <span> · </span> <a href="https://github.com/vivekkdagar/conway_engine/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/vivekkdagar/conway_engine/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/vivekkdagar/conway_engine/issues"> Request Feature </a> </h4>


</div>

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
- [Roadmap](#compass-roadmap)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)


## Requirements

Ensure you meet the following requirements before installation:

- **Python**: The simulation is written in Python. Download and install Python from [python.org](https://www.python.org/).

- **Pygame**: The Pygame library is used for graphics and interaction. Install it using:

  ```bash
  pip install pygame


## :star2: About the Project

### :camera: Screenshots
<div align="center"> <a href=""><img src="https://github.com/vivekkdagar/conway_engine/blob/main/assets/Demo%201.png" alt='image' width='800'/></a> </div>
<div align="center"> <a href=""><img src="https://github.com/vivekkdagar/conway_engine/blob/main/assets/Demo%202.png" alt='image' width='800'/></a> </div>



### :dart: Features
- Gosper Glider Gun: Experience the inclusion of the renowned Gosper Glider Gun, a pattern triggering gliders in a repeating sequence, resulting in explosive growth.


### :art: Color Reference
| Color | Hex |
| --------------- | ---------------------------------------------------------------- |
| Primary Color | ![#5c9b09](https://via.placeholder.com/10/5c9b09?text=+) #5c9b09 |
| Secondary Color | ![#04047c](https://via.placeholder.com/10/04047c?text=+) #04047c |
| Accent Color | ![#00ADB5](https://via.placeholder.com/10/00ADB5?text=+) #00ADB5 |
| Text Color | ![#EEEEEE](https://via.placeholder.com/10/EEEEEE?text=+) #EEEEEE |

### :key: Environment Variables
To run this project, you will need to add the following environment variables to your .env file
`asdasd`



## :toolbox: Getting Started

### :bangbang: Prerequisites

- Python3<a href="https://www.python.org/"> Here</a>
- Pygame<a href="https://pypi.org/project/pygame/"> Here</a>
```bash
pip install pygame
```


### :running: Run Locally

Clone the project

```bash
https://github.com/vivekkdagar/conway_engine
```
Install the package using pip.
```bash
pip install dist/*.tar.gz
```
Build the package using the commands below.
```bash
python3 setup.py sdist bdist_wheel
```
Navigate to the root directory of the cloned repository.
```bash
cd conway_engine
```
Clone the Git repository.
```bash
git clone <repository_url>
```


## :compass: Roadmap

* [x] aSIJASDOI


## :wave: Contributing

<a href="https://github.com/vivekkdagar/conway_engine/graphs/contributors"> <img src="https://contrib.rocks/image?repo=Louis3797/awesome-readme-template" /> </a>

Contributions are always welcome!

see `contributing.md` for ways to get started

### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/vivekkdagar/conway_engine/blob/master/CODE_OF_CONDUCT.md)

## :grey_question: FAQ

- Q1: What is the Game of Life by John Conway?
- The Game of Life is a cellular automaton created by mathematician John Conway. It consists of a two-dimensional grid where each cell can be alive or dead. The evolution of the grid is determined by simple rules, including underpopulation, survival, overpopulation, and reproduction. Starting with an initial configuration of cells, these rules are applied iteratively to create new generations, leading to complex and interesting patterns.
- What are the rules of the Game of Life?
- The rules of the Game of Life are: Underpopulation: A live cell with fewer than two live neighbors dies. Survival: A live cell with two or three live neighbors continues to live. Overpopulation: A live cell with more than three live neighbors dies. Reproduction: A dead cell with exactly three live neighbors becomes alive. These simple rules give rise to a variety of patterns, including stable structures, oscillators, and gliders, making the Game of Life a fascinating and widely studied cellular automaton.


## :warning: License

Distributed under the no License. See LICENSE.txt for more information.

## :handshake: Contact

Vivek Dagar - - vivekdagar2023@gmail.com

Project Link: [https://github.com/vivekkdagar/conway_engine](https://github.com/vivekkdagar/conway_engine)

## :gem: Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

- [IJI](IJK)
- [Pygame Library Integration: Leveraging the Pygame library for graphics and user interaction streamlines the development of the Game of Life simulation, providing a robust framework for handling events, drawing the grid, and creating an engaging visual experience for users.](https://pypi.org/project/pygame/)
- [John Conway's Game of Life: The entire codebase is built upon the principles of John Conway's Game of Life. The rules governing cell evolution, the grid-based structure, and the concept of cellular automata are all inspired by Conway's seminal work in the field of mathematical games and automata theory.](https://en.wikipedia.org/wiki/John_Horton_Conway)
- [Gosper Glider Gun Pattern: The implementation of the Gosper glider gun pattern, a well-known configuration in Conway's Game of Life, adds complexity and visual interest to the simulation. The Gosper glider gun is famous for generating gliders, which contribute to the emergence of diverse patterns and behaviors.](https://conwaylife.com/wiki/Gosper_glider_gun)
