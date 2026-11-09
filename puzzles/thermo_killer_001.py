from sudoku.puzzle import SudokuPuzzle

NAME = "Thermo Killer Sudoku #001"


def create_puzzle():
    # No given digits
    grid = [[0 for _ in range(9)] for _ in range(9)]
    puzzle = SudokuPuzzle(grid)
    
    # Thermometers: bulb first, tip last.
    thermometers = [
        [(0, 1), (0, 0), (1, 0), (1, 1)],
        [(1, 3), (1, 4)],
        [(2, 3), (2, 4), (2, 5), (2, 6), (1, 6), (0, 6)],
        [(3, 3), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6)],
        [(4, 1), (4, 0)],
        [(4, 7), (5, 7)],
        [(5, 0), (6, 0)],
        [(7, 0), (8, 0)],
        [(7, 1), (8, 1)],
    ]

    for cells in thermometers:
        puzzle.add_thermometer(cells)

    # Killer cages: (target sum, cells)
    cages = [
        (9, [(0, 2), (1, 2)]),

        (19, [(0, 8), (1, 8), (2, 8), (3, 8)]),

        (27, [
            (2, 0), (2, 1),
            (3, 0), (3, 1), (3, 2),
        ]),

        (45, [
            (4, 3), (4, 4), (4, 5),
            (5, 3), (5, 4), (5, 5),
            (6, 3), (6, 4), (6, 5),
        ]),

        (19, [(6, 7), (7, 7), (8, 7)]),

        (13, [
            (7, 2), (7, 3),
            (8, 2), (8, 3),
        ]),

        (24, [
            (7, 4), (7, 5),
            (8, 4), (8, 5),
        ]),
    ]

    for target, cells in cages:
        puzzle.add_killer_cage(cells, target)

    return puzzle