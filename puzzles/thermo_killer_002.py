from sudoku.puzzle import SudokuPuzzle

NAME = "Thermo Killer Sudoku #002 — Overlapping Constraints"


def create_puzzle():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    puzzle = SudokuPuzzle(grid)

    # Thermometers: bulb first, tip last.
    thermometers = [
        # Top-left horizontal thermometer
        [(0, 0), (0, 1), (0, 2)],

        # Upper-right diagonal thermometer
        [(1, 4), (1, 5), (2, 6), (2, 7), (2, 8)],

        # Middle-left diagonal thermometer
        [(5, 1), (4, 2), (3, 2)],

        # Center vertical thermometer
        [(5, 4), (4, 4), (3, 4)],

        # Middle-right diagonal thermometer
        [(3, 7), (4, 6), (5, 6)],

        # Lower-left long thermometer
        [(6, 0), (6, 1), (6, 2), (7, 3), (7, 4)],

        # Bottom-right horizontal thermometer
        [(8, 6), (8, 7), (8, 8)],
    ]

    for cells in thermometers:
        puzzle.add_thermometer(cells)

    # Killer cages: (target sum, cells)
    cages = [
        (6, [
            (0, 0), (1, 0), (2, 0),
        ]),

        (28, [
            (0, 2), (0, 3), (0, 4),
            (1, 4),
        ]),

        (14, [
            (2, 8),
            (3, 7), (3, 8),
        ]),

        (20, [
            (3, 1), (3, 2), (3, 3), (3, 4),
        ]),

        (13, [
            (5, 0), (5, 1),
            (6, 0),
        ]),

        (22, [
            (5, 4), (5, 5), (5, 6), (5, 7),
        ]),

        (8, [
            (6, 8), (7, 8), (8, 8),
        ]),

        (25, [
            (7, 4),
            (8, 4), (8, 5), (8, 6),
        ]),
    ]

    for target, cells in cages:
        puzzle.add_killer_cage(cells, target)

    return puzzle