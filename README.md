# Sudoko-Solver

A Python Sudoku solver that combines:

A Python Sudoku solver that combines:

- AC-3 constraint propagation
- Forward checking
- Backtracking search
- MRV (Minimum Remaining Values) variable ordering

It solves multiple boards in sequence and includes a short delay between boards so results are easier to read.

## Project Structure

23F-0711-AI-05/

- src/
  - Sudoko.py
- puzzles/
  - easy.txt
  - medium.txt
  - hard.txt
  - veryhard.txt
- README.md
- .gitignore

## Requirements

- Python 3.8+
- No external packages required

## Input Format

Each puzzle file must contain exactly 9 lines, each line with 9 digits.
Use 0 for empty cells.

Example line:
530070000

## Run

From the repository root:

python src/Sudoko.py

The script will solve:

- easy.txt
- medium.txt
- hard.txt
- veryhard.txt

from the puzzles folder and print:

- solved board
- backtrack calls
- failures

## Notes

- File name is currently Sudoko.py to match your original file.
- You can rename it to Sudoku.py later if you want a spelling cleanup.
- Delay between boards is currently 2 seconds.
