# cython_ass
# Pong Game

This is a simple implementation of the classic Pong game using Python's Turtle graphics library. The game features two paddles that can be controlled by players, and a ball that bounces off the paddles and the screen boundaries.

## Requirements

- Python 3.x
- Turtle graphics library (comes pre-installed with Python)

## Files

1. `ball.py`: This file contains the `Ball` class responsible for creating and moving the ball.
2. `new_player.py`: This file contains the `NewPlayer` class responsible for creating and controlling the paddles.
3. `player(1st version,inferior).py`: This file contains an older version of the `Player` class, which is an inferior implementation compared to `NewPlayer`.
4. `pong_game.py`: This is the main file that sets up the game screen, creates instances of the `Ball` and `NewPlayer` classes, and handles the game loop and collision detection.

## How to Run

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the game:

```
python pong_game.py
```

## Controls

- Player 1 (left paddle):
  - Move up: `w`
  - Move down: `s`

- Player 2 (right paddle):
  - Move up: `Up Arrow`
  - Move down: `Down Arrow`

## Game Rules

- The ball moves back and forth between the two paddles.
- If a player misses the ball, the other player scores a point.
- The game continues until one player scores a predetermined number of points (not implemented in this version).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

# Factorial Calculation

This repository contains two implementations of a function to calculate the factorial of a given number: one in Python and one in Cython.

## Python Version

The Python version, `factorial(n: int) -> int`, is a straightforward implementation of the factorial calculation using a for loop:

```python
def factorial(n: int) -> int:
    """
    Vanilla Python function to calculate the factorial of a given number.
    """
    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

This function takes an integer `n` as input and returns the factorial of `n`. It initializes `result` to 1 and then iterates from 1 to `n`, multiplying `result` by each number in the range.

## Cython Version

The Cython version, `factorial_cython(int n)`, is a translation of the Python version with explicit type declarations:

```cython
cpdef int factorial_cython(int n):
    """
    Cythonized version of the factorial function with types added.
    """
    cdef int result = 1
    cdef int i
    for i in range(1, n + 1):
        result *= i
    return result
```

In this version, the `cdef` keyword is used to declare the types of variables `result` and `i` as integers. The `cpdef` keyword is used to make the function callable from both Cython and Python code.

When compiled with Cython, this function should run faster than the pure Python version due to the static type declarations and other optimizations performed by the Cython compiler.

## Requirements

- Python 3.x
- Cython (if you want to compile and use the Cython version)

## Usage

To use the Python version, simply import the `factorial` function:

```python
from factorial import factorial

print(factorial(5))  # Output: 120
```

To use the Cython version, you'll need to first compile the Cython code:

```
$ cython -a factorial.pyx
$ python setup.py build_ext --inplace
```

Then, you can import and use the `factorial_cython` function:

```python
from factorial import factorial_cython

print(factorial_cython(5))  # Output: 120
```

Note that the Cython version may require additional setup and configuration depending on your environment.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
