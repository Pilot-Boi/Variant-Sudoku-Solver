
from puzzles.renban_001 import NAME, create_puzzle
from visualization.html_renderer import show_puzzle


def main():
    puzzle = create_puzzle()

    print("Solving puzzle...")

    status, solutions, solver = puzzle.check_uniqueness()

    if not solutions:
        print("No solution found.")
        return

    # Get the first solution.
    solution = solutions[0]

    # Convert the assignment dictionary to a 9x9 grid.
    solution_grid = [
        [
            solution[(r, c)]
            for c in range(9)
        ]
        for r in range(9)
    ]

    path = show_puzzle(
        puzzle,
        title=NAME,
        output="output/renban_001.html",
        solution=solution_grid
    )

    print(f"Puzzle status: {status}")
    print(f"Puzzle visualization saved to: {path}")


if __name__ == "__main__":
    main()
