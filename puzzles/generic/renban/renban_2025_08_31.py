"""PuzzleMadness Renban Sudoku — 2025-08-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 6, 5, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 7, 0, 9],
        [0, 5, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3, 4, 0, 7, 0],
        [0, 2, 0, 0, 0, 8, 6, 1, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(8, 5), (7, 4), (6, 3), (7, 2), (8, 1)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8), (5, 7), (5, 6)])
    puzzle.add_renban([(3, 1), (3, 2), (3, 3), (2, 3), (1, 3)])
    puzzle.add_renban([(2, 6), (1, 6), (0, 6), (0, 5)])
    puzzle.add_renban([(6, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_renban([(5, 3), (4, 2), (5, 1), (6, 0)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(3, 8), (4, 8)])
    puzzle.add_renban([(3, 4), (4, 4)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(0, 2), (1, 2)])

    return puzzle
