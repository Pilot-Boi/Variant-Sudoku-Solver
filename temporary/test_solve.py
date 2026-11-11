
from pprint import pprint

from puzzles.generic.killer.killer_2025_03_06 import create_puzzle
from sudoku.validator import validate_solution

puzzle = create_puzzle()

solution, solver = puzzle.solve(instrument=True)

print("Solved:", solution is not None)
print("Instrumentation enabled:", solver.instrument)

if solution is not None:
    print("Validation:", validate_solution(puzzle, solution))

print("\nExisting statistics:")
print("Search decisions:", solver.nodes)
print("Backtracks:", solver.backtracks)
print("Propagation rounds:", solver.propagation_rounds)

print("\nNew statistics:")
for key, value in solver.metrics.items():
    if key != "constraint_types":
        print(f"{key}: {value}")

print("\nStatistics by constraint type:")
pprint(solver.metrics["constraint_types"])

print("\nContradictions by constraint type:")

for name, stats in solver.metrics["constraint_types"].items():
    print(
        f"{name}: "
        f"{stats['contradictions']} propagation, "
        f"{stats['validation_contradictions']} validation"
    )

# Verify contradiction counts are consistent
assert (
    sum(
        stats["contradictions"]
        for stats in solver.metrics["constraint_types"].values()
    )
    == solver.metrics["constraint_contradictions"]
)

assert (
    sum(
        stats["validation_contradictions"]
        for stats in solver.metrics["constraint_types"].values()
    )
    == solver.metrics["validation_contradictions"]
)

print("\nAll instrumentation checks passed!")