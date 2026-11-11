"""PuzzleMadness Renban Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 6, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [7, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 8],
        [0, 7, 0, 0, 0, 0, 0, 0, 6],
        [9, 0, 0, 3, 0, 8, 0, 0, 7],
        [0, 5, 6, 0, 4, 0, 0, 0, 0],
        [0, 3, 2, 8, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(1, 4), (2, 4), (3, 4), (3, 5), (3, 6)])
    puzzle.add_renban([(4, 2), (5, 2), (6, 2), (6, 3), (6, 4)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (2, 1)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (6, 8)])
    puzzle.add_renban([(2, 3), (1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(8, 2), (8, 3), (7, 3)])
    puzzle.add_renban([(5, 3), (5, 4), (4, 4)])
    puzzle.add_renban([(4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(0, 7), (1, 6)])
    puzzle.add_renban([(6, 6), (5, 6)])
    puzzle.add_renban([(3, 2), (3, 3)])
    puzzle.add_renban([(1, 1), (1, 2)])
    puzzle.add_renban([(8, 7), (7, 6)])

    return puzzle
