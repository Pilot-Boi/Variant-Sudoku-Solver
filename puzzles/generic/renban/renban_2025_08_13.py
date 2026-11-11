"""PuzzleMadness Renban Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 7, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 1, 0, 0],
        [8, 5, 6, 2, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 5, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 3), (7, 3), (8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1)])
    puzzle.add_renban([(5, 5), (5, 6), (5, 7), (4, 7), (3, 7)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(6, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_renban([(4, 5), (4, 4), (4, 3), (5, 3)])
    puzzle.add_renban([(0, 3), (0, 2), (1, 2)])
    puzzle.add_renban([(0, 7), (1, 7), (2, 7)])
    puzzle.add_renban([(8, 0), (7, 1), (6, 2)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(1, 1), (2, 2)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(7, 5), (6, 5)])
    puzzle.add_renban([(2, 6), (3, 5)])
    puzzle.add_renban([(2, 0), (3, 1)])

    return puzzle
