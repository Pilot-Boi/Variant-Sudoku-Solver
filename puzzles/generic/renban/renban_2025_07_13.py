"""PuzzleMadness Renban Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 2, 0, 0, 0, 0],
        [4, 1, 0, 0, 0, 3, 0, 0, 0],
        [0, 3, 0, 0, 4, 0, 9, 5, 0],
        [3, 0, 0, 1, 0, 9, 2, 0, 4],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 4, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 7), (6, 6), (5, 5), (6, 4), (7, 3)])
    puzzle.add_renban([(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(4, 5), (4, 6), (4, 7), (3, 7), (2, 7)])
    puzzle.add_renban([(1, 5), (1, 4), (2, 4), (3, 4)])
    puzzle.add_renban([(1, 1), (1, 0), (2, 0), (3, 0)])
    puzzle.add_renban([(4, 2), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(0, 7), (1, 6), (2, 5)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(3, 5), (4, 4), (5, 3)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(0, 4), (0, 5)])
    puzzle.add_renban([(4, 8), (5, 7)])
    puzzle.add_renban([(8, 0), (8, 1)])

    return puzzle
