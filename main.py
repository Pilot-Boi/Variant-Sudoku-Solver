from time import perf_counter
from puzzles.ctc.ctc_002 import NAME, create_puzzle
from sudoku.validator import validate_solution

def main():
    puzzle = create_puzzle()

    print(f"PUZZLE: {NAME}")
    print("Checking solution uniqueness...\n")

    start = perf_counter()
    status, solutions, solver = puzzle.check_uniqueness()
    elapsed = perf_counter() - start

    print(f"Status: {status.upper()}")
    print(f"Solutions found: {len(solutions)}")
    print(f"Elapsed time: {elapsed:.6f} seconds")
    print(f"Search decisions: {solver.nodes}")
    print(f"Backtracks: {solver.backtracks}")
    print(f"Propagation rounds: {solver.propagation_rounds}")

    for i, solution in enumerate(solutions, 1):
        print(f"\nSOLUTION {i}:")
        puzzle.print_grid(solution)

        errors = validate_solution(puzzle, solution)

        if errors:
            print("\nVALIDATION FAILED:")
            for error in errors:
                print(f"  - {error}")
        else:
            print("\nVALIDATION PASSED")
            print("All standard and variant constraints are satisfied.")


if __name__ == "__main__":
    main()
