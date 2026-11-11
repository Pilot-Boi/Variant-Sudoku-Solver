"""PuzzleMadness Renban Sudoku — 2025-01-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 7, 0, 2, 0, 0, 0],
        [0, 3, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 4, 0, 0, 8],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 4, 0, 1],
        [0, 0, 5, 0, 0, 9, 6, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 7), (1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(6, 3), (5, 4), (4, 5), (3, 4), (2, 3)])
    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(5, 1), (6, 2), (7, 3), (6, 4)])
    puzzle.add_renban([(1, 6), (1, 5), (2, 5), (3, 5)])
    puzzle.add_renban([(7, 2), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(4, 7), (3, 7), (3, 6)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(1, 1), (2, 2)])
    puzzle.add_renban([(0, 2), (1, 2)])
    puzzle.add_renban([(7, 1), (6, 1)])

    return puzzle
