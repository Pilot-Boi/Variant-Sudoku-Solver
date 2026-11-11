"""PuzzleMadness Renban Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 4, 0, 0, 0, 0, 0, 0, 7],
        [9, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 3, 2, 0, 0, 0, 6, 5, 0],
        [0, 8, 1, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 1, 0, 5],
        [0, 0, 5, 0, 9, 0, 0, 0, 8],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 8, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 2), (3, 2), (4, 2), (5, 2), (6, 2)])
    puzzle.add_renban([(2, 7), (1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(3, 3), (4, 3), (5, 3), (6, 3), (7, 3)])
    puzzle.add_renban([(1, 6), (2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(6, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(1, 2), (2, 3), (3, 4)])
    puzzle.add_renban([(4, 1), (4, 0), (5, 0)])
    puzzle.add_renban([(4, 8), (3, 8), (3, 7)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(8, 4), (7, 4)])
    puzzle.add_renban([(6, 4), (5, 4)])
    puzzle.add_renban([(0, 4), (1, 3)])
    puzzle.add_renban([(1, 4), (1, 5)])

    return puzzle
