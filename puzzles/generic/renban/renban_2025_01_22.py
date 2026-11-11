"""PuzzleMadness Renban Sudoku — 2025-01-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 1, 0, 4, 0],
        [8, 0, 0, 5, 0, 0, 3, 0, 2],
        [5, 4, 1, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 7],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [4, 6, 0, 0, 2, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 6, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(4, 6), (5, 5), (6, 4), (7, 5), (8, 6)])
    puzzle.add_renban([(0, 6), (0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(5, 8), (4, 8), (3, 8), (3, 7)])
    puzzle.add_renban([(4, 2), (5, 2), (5, 3), (5, 4)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8), (6, 7)])
    puzzle.add_renban([(8, 1), (7, 1), (6, 1)])
    puzzle.add_renban([(4, 3), (3, 4), (2, 3)])
    puzzle.add_renban([(2, 5), (3, 5), (3, 6)])
    puzzle.add_renban([(6, 3), (6, 2), (7, 2)])
    puzzle.add_renban([(7, 3), (7, 4)])
    puzzle.add_renban([(4, 0), (5, 1)])
    puzzle.add_renban([(1, 7), (2, 6)])
    puzzle.add_renban([(0, 3), (1, 3)])
    puzzle.add_renban([(1, 0), (2, 1)])

    return puzzle
