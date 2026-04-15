from collections import deque
import copy
import os
import time

# ----------------------------
# Utility Functions
# ----------------------------

def ReadBoard(FilePath):
    Board = []
    with open(FilePath, 'r') as F:
        for Line in F:
            Board.append([int(C) for C in Line.strip()])
    return Board


def PrintBoard(Board):
    for Row in Board:
        print(" ".join(map(str, Row)))
    print()


def GetNeighbors():
    Neighbors = {}
    for R in range(9):
        for C in range(9):
            Cell = (R, C)
            Neighbors[Cell] = set()

            # Row & Column
            for I in range(9):
                Neighbors[Cell].add((R, I))
                Neighbors[Cell].add((I, C))

            # Box
            Br, Bc = 3 * (R // 3), 3 * (C // 3)
            for I in range(Br, Br + 3):
                for J in range(Bc, Bc + 3):
                    Neighbors[Cell].add((I, J))

            Neighbors[Cell].remove(Cell)

    return Neighbors


# ----------------------------
# AC-3 Algorithm
# ----------------------------

def AC3(Domains, Neighbors):
    Queue = deque([(Xi, Xj) for Xi in Domains for Xj in Neighbors[Xi]])

    while Queue:
        Xi, Xj = Queue.popleft()
        if Revise(Domains, Xi, Xj):
            if len(Domains[Xi]) == 0:
                return False
            for Xk in Neighbors[Xi]:
                if Xk != Xj:
                    Queue.append((Xk, Xi))
    return True


def Revise(Domains, Xi, Xj):
    Revised = False
    ToRemove = set()

    for X in Domains[Xi]:
        if all(X == Y for Y in Domains[Xj]):
            ToRemove.add(X)

    if ToRemove:
        Domains[Xi] -= ToRemove
        Revised = True

    return Revised


# ----------------------------
# Forward Checking
# ----------------------------

def ForwardCheck(Domains, Var, Value, Neighbors):
    for N in Neighbors[Var]:
        if Value in Domains[N]:
            Domains[N] = Domains[N] - {Value}
            if len(Domains[N]) == 0:
                return False
    return True


# ----------------------------
# Variable Selection (MRV)
# ----------------------------

def SelectUnassignedVariable(Domains, Assignment):
    Unassigned = [V for V in Domains if V not in Assignment]
    return min(Unassigned, key=lambda Var: len(Domains[Var]))


# ----------------------------
# Backtracking with FC + AC-3
# ----------------------------

class SolverStats:
    def __init__(self):
        self.calls = 0
        self.failures = 0


def Backtrack(Assignment, Domains, Neighbors, Stats):
    Stats.calls += 1

    if len(Assignment) == 81:
        return Assignment

    Var = SelectUnassignedVariable(Domains, Assignment)

    for Value in sorted(Domains[Var]):
        NewAssignment = Assignment.copy()
        NewAssignment[Var] = Value

        NewDomains = copy.deepcopy(Domains)
        NewDomains[Var] = {Value}

        # Forward Checking
        if not ForwardCheck(NewDomains, Var, Value, Neighbors):
            Stats.failures += 1
            continue

        # AC-3
        if not AC3(NewDomains, Neighbors):
            Stats.failures += 1
            continue

        Result = Backtrack(NewAssignment, NewDomains, Neighbors, Stats)
        if Result:
            return Result

    Stats.failures += 1
    return None


# ----------------------------
# Initialize Domains
# ----------------------------

def InitializeDomains(Board):
    Domains = {}
    for R in range(9):
        for C in range(9):
            if Board[R][C] == 0:
                Domains[(R, C)] = set(range(1, 10))
            else:
                Domains[(R, C)] = {Board[R][C]}
    return Domains


# ----------------------------
# Solve Function
# ----------------------------

def SolveSudoku(FilePath):
    Board = ReadBoard(FilePath)
    Neighbors = GetNeighbors()
    Domains = InitializeDomains(Board)

    Stats = SolverStats()

    # Initial AC-3
    if not AC3(Domains, Neighbors):
        print("No solution exists.")
        return

    Assignment = {}
    for Var in Domains:
        if len(Domains[Var]) == 1:
            Assignment[Var] = next(iter(Domains[Var]))

    Result = Backtrack(Assignment, Domains, Neighbors, Stats)

    if Result:
        Solved = [[0]*9 for _ in range(9)]
        for (R, C), Val in Result.items():
            Solved[R][C] = Val

        print("Solved Sudoku:")
        PrintBoard(Solved)
        print(f"Backtrack Calls: {Stats.calls}")
        print(f"Failures: {Stats.failures}")
    else:
        print("No solution found.")


# ----------------------------
# Run for Multiple Boards
# ----------------------------

if __name__ == "__main__":
    BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PuzzleDir = os.path.join(BaseDir, "puzzles")
    Files = ["easy.txt", "medium.txt", "hard.txt", "veryhard.txt"]

    for F in Files:
        print(f"\nSolving {F}...")
        SolveSudoku(os.path.join(PuzzleDir, F))
        time.sleep(2)  # 2-second delay between boards