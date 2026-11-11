"""PuzzleMadness Renban Sudoku — 2025-07-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 3, 0, 5, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 8, 4],
        [0, 0, 0, 2, 0, 0, 6, 0, 0],
        [0, 6, 8, 4, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 5, 0, 3, 0, 0, 7],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 1), (4, 2), (3, 3), (2, 2), (1, 1)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(3, 8), (2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(3, 5), (4, 4), (5, 3), (6, 4)])
    puzzle.add_renban([(4, 6), (5, 6), (6, 6), (6, 7)])
    puzzle.add_renban([(8, 3), (7, 3), (6, 3), (6, 2)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(8, 7), (7, 6), (6, 5)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(2, 5), (2, 4), (3, 4)])
    puzzle.add_renban([(8, 5), (7, 5)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(4, 7), (5, 7)])
    puzzle.add_renban([(0, 7), (0, 6)])
    puzzle.add_renban([(0, 1), (0, 2)])

    return puzzle
