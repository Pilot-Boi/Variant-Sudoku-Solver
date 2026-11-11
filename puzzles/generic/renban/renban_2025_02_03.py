"""PuzzleMadness Renban Sudoku — 2025-02-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 1, 0, 9, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 2, 8, 0],
        [0, 0, 0, 7, 8, 0, 9, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 4, 9, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 6, 4, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 3), (6, 4), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(3, 5), (4, 4), (5, 3), (6, 2), (7, 1)])
    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(1, 4), (0, 4), (0, 3), (0, 2)])
    puzzle.add_renban([(1, 7), (0, 6), (1, 5), (2, 4)])
    puzzle.add_renban([(1, 3), (2, 2), (3, 3)])
    puzzle.add_renban([(1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6)])
    puzzle.add_renban([(4, 8), (5, 7)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(0, 1), (1, 2)])
    puzzle.add_renban([(8, 2), (7, 3)])

    return puzzle
