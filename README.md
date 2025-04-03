# K-map Solver

This project is a K-map (Karnaugh map) solver that simplifies Boolean expressions using the K-map method. It provides a user-friendly interface for inputting K-map data and outputs the simplified Boolean expression.

## Project Structure

```
kmap-solver
├── src
│   ├── main.py               # Entry point of the application
│   ├── solver
│   │   ├── __init__.py       # Marks the solver directory as a package
│   │   └── kmap_solver.py     # Contains the KMapSolver class
│   ├── utils
│   │   ├── __init__.py       # Marks the utils directory as a package
│   │   └── helpers.py        # Contains utility functions for input/output
│   └── tests
│       ├── __init__.py       # Marks the tests directory as a package
│       └── test_kmap_solver.py # Contains unit tests for KMapSolver
├── requirements.txt           # Lists dependencies for the project
└── README.md                  # Documentation for the project
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the K-map solver, execute the following command:

```
python src/main.py
```

Follow the prompts to input your K-map data.

## Examples

1. **Input**: `1, 1, 0, 1`
   **Output**: `A'B + AB'`

2. **Input**: `0, 1, 1, 0`
   **Output**: `A'B' + AB`

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.