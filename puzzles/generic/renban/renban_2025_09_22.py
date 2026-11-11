"""PuzzleMadness Renban Sudoku — 2025-09-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 8, 3, 6, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 8],
        [6, 0, 2, 0, 0, 9, 0, 0, 0],
        [9, 0, 0, 0, 0, 5, 1, 0, 0],
        [0, 0, 0, 0, 6, 4, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 3, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (6, 5), (5, 5)])
    puzzle.add_renban([(1, 8), (2, 7), (3, 6), (4, 7), (5, 8)])
    puzzle.add_renban([(4, 1), (5, 2), (6, 3), (5, 4), (4, 5)])
    puzzle.add_renban([(6, 1), (7, 1), (8, 1), (8, 2)])
    puzzle.add_renban([(4, 3), (3, 4), (2, 5), (1, 4)])
    puzzle.add_renban([(1, 2), (2, 2), (3, 2), (4, 2)])
    puzzle.add_renban([(7, 8), (6, 7), (5, 6)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(8, 6), (7, 6), (6, 6)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(6, 8), (5, 7)])
    puzzle.add_renban([(2, 4), (3, 3)])
    puzzle.add_renban([(0, 1), (1, 1)])
    puzzle.add_renban([(2, 0), (3, 0)])

    return puzzle
