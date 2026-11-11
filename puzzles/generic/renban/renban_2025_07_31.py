"""PuzzleMadness Renban Sudoku — 2025-07-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 7, 0, 4, 0],
        [8, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 3, 0, 0, 0],
        [0, 0, 9, 0, 0, 5, 0, 0, 8],
        [0, 0, 0, 0, 0, 4, 9, 7, 0],
        [0, 7, 0, 0, 0, 0, 0, 2, 1],
        [0, 1, 3, 0, 8, 0, 0, 0, 0],
        [0, 8, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(8, 5), (7, 6), (6, 7), (5, 6), (4, 5)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(3, 4), (3, 5), (3, 6), (3, 7), (3, 8)])
    puzzle.add_renban([(1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_renban([(4, 3), (5, 2), (6, 1), (7, 2)])
    puzzle.add_renban([(0, 2), (1, 1), (2, 0), (3, 1)])
    puzzle.add_renban([(2, 3), (2, 4), (2, 5)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(7, 7), (6, 8), (5, 7)])
    puzzle.add_renban([(4, 2), (4, 1), (5, 1)])
    puzzle.add_renban([(6, 4), (6, 5)])
    puzzle.add_renban([(1, 7), (2, 7)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(3, 0), (4, 0)])
    puzzle.add_renban([(1, 3), (1, 4)])

    return puzzle
