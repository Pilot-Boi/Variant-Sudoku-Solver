"""PuzzleMadness Renban Sudoku — 2025-08-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 5, 0, 2, 3, 4, 0],
        [2, 0, 0, 0, 0, 0, 8, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 2, 6, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 8, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(5, 7), (4, 7), (3, 7), (3, 6)])
    puzzle.add_renban([(5, 2), (5, 1), (6, 1)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6)])
    puzzle.add_renban([(6, 7), (6, 6), (7, 6)])
    puzzle.add_renban([(2, 1), (3, 1), (3, 2)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(6, 4), (5, 5)])
    puzzle.add_renban([(1, 4), (1, 5)])
    puzzle.add_renban([(5, 0), (4, 1)])
    puzzle.add_renban([(1, 0), (2, 0)])

    return puzzle
