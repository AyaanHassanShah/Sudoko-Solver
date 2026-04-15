# Sudoku Solver (CSP + AC-3)

Solve Sudoku puzzles using classic AI techniques from Constraint Satisfaction Problems (CSP):

- AC-3 constraint propagation
- Backtracking search
- Forward checking
- MRV (Minimum Remaining Values) variable selection

This project solves multiple puzzle files in one run and reports search stats, so you can compare puzzle difficulty by actual solver effort.

## Why This Project Is Interesting

Instead of brute force, this solver uses reasoning:

- AC-3 reduces domains early by enforcing arc consistency.
- Forward checking catches dead-ends quickly after each assignment.
- MRV chooses the most constrained variable first to shrink the search tree.

Together, these techniques make the solver much smarter than plain backtracking.

## Project Structure

```text
23F-0711-AI-05/
|-- src/
|   `-- Sudoko.py
|-- puzzles/
|   |-- easy.txt
|   |-- medium.txt
|   |-- hard.txt
|   `-- veryhard.txt
|-- README.md
`-- .gitignore
```

## Requirements

- Python 3.8+
- No external dependencies

## Puzzle Input Format

Each puzzle file must follow this exact format:

- Exactly 9 lines
- Each line has exactly 9 digits (`0-9`)
- `0` means an empty cell

Example row:

```text
004030050
```

## Run the Solver

From the project root:

```bash
python src/Sudoko.py
```

The program reads and solves:

- easy.txt
- medium.txt
- hard.txt
- veryhard.txt

For each puzzle, it prints:

- solved grid (if solvable)
- number of backtrack calls
- number of backtrack failures

## What You Can Learn From Output

The solver statistics show how puzzle difficulty affects search complexity:

- low calls/failures: puzzle was heavily reduced by constraints
- high calls/failures: puzzle needed deeper search

This makes the project useful both as a solver and as an AI/CSP learning demo.

## Notes

- Script filename is `Sudoko.py` to match the current repository files.
- There is a 2-second delay between puzzles for readable console output.
