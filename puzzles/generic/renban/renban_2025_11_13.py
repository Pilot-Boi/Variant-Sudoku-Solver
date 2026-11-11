"""PuzzleMadness Renban Sudoku — 2025-11-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 9, 0, 0, 4, 0],
        [0, 9, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 2, 3, 0],
        [8, 0, 0, 4, 0, 6, 0, 9, 5],
        [0, 0, 4, 3, 0, 0, 0, 2, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(5, 5), (6, 5), (7, 5), (7, 6), (7, 7)])
    puzzle.add_renban([(4, 1), (5, 2), (6, 3), (5, 4), (4, 5)])
    puzzle.add_renban([(0, 3), (0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(2, 4), (1, 4), (1, 3), (1, 2)])
    puzzle.add_renban([(5, 6), (4, 7), (3, 8), (2, 7)])
    puzzle.add_renban([(6, 7), (6, 8), (5, 8)])
    puzzle.add_renban([(4, 8), (5, 7), (6, 6)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(2, 0), (3, 1), (4, 2)])
    puzzle.add_renban([(1, 7), (1, 6)])
    puzzle.add_renban([(3, 3), (4, 3)])
    puzzle.add_renban([(2, 6), (3, 6)])
    puzzle.add_renban([(7, 1), (7, 2)])
    puzzle.add_renban([(8, 5), (7, 4)])

    return puzzle
