from time import perf_counter

from puzzles.ctc_002 import SOLUTION, create_puzzle
from sudoku.validator import validate_solution

puzzle = create_puzzle()

start = perf_counter()
solution, solver = puzzle.solve()
elapsed = perf_counter() - start

print(f"Elapsed: {elapsed:.4f}s")
print(f"Decisions: {solver.nodes}")
print(f"Backtracks: {solver.backtracks}")
print(f"Propagation rounds: {solver.propagation_rounds}")

if solution is None:
    print("No solution found.")
else:
    errors = validate_solution(puzzle, solution)
    print(f"Validation: {'PASS' if not errors else errors}")

    embedded = {
        (r, c): int(SOLUTION[r * 9 + c])
        for r in range(9)
        for c in range(9)
    }

    print(f"Matches SudokuPad solution: {solution == embedded}")