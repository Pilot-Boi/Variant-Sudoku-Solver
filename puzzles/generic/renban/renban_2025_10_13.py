"""PuzzleMadness Renban Sudoku — 2025-10-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 5, 3, 0, 0, 0, 6, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 7],
        [6, 8, 5, 0, 7, 0, 0, 0, 9],
        [1, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 9, 0, 0, 0],
        [0, 7, 9, 0, 0, 0, 3, 5, 0],
        [0, 0, 0, 0, 0, 2, 0, 8, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6), (6, 7), (7, 8)])
    puzzle.add_renban([(2, 7), (1, 6), (2, 5), (3, 4)])
    puzzle.add_renban([(1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(4, 0), (5, 0), (5, 1)])
    puzzle.add_renban([(3, 2), (4, 2), (4, 3)])
    puzzle.add_renban([(2, 6), (3, 5), (4, 6)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(7, 0), (7, 1)])
    puzzle.add_renban([(6, 6), (6, 5)])
    puzzle.add_renban([(7, 7), (7, 6)])

    return puzzle
