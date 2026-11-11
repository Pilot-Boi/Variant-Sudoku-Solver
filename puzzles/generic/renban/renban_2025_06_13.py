"""PuzzleMadness Renban Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 1, 9, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 9, 7, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 0],
        [0, 0, 8, 5, 0, 0, 0, 7, 0],
        [2, 0, 0, 0, 7, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 1, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])
    puzzle.add_renban([(1, 2), (2, 1), (3, 0), (4, 1), (5, 2)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (6, 6), (5, 6)])
    puzzle.add_renban([(4, 7), (4, 8), (3, 8), (2, 8)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6), (1, 6)])
    puzzle.add_renban([(4, 3), (5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 7)])
    puzzle.add_renban([(1, 4), (2, 3), (3, 2)])
    puzzle.add_renban([(2, 4), (3, 3), (4, 4)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(0, 4), (1, 3)])
    puzzle.add_renban([(7, 1), (7, 2)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(1, 8), (1, 7)])

    return puzzle
