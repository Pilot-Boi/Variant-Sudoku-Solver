"""PuzzleMadness Renban Sudoku — 2025-09-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [3, 0, 0, 0, 1, 0, 0, 0, 0],
        [9, 0, 3, 6, 0, 0, 0, 5, 0],
        [0, 0, 7, 2, 0, 0, 0, 0, 3],
        [0, 0, 5, 0, 9, 0, 0, 0, 0],
        [0, 2, 0, 0, 4, 0, 3, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 8), (4, 8), (3, 8), (3, 7), (3, 6)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(5, 1), (6, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(6, 4), (5, 5), (4, 4), (3, 3)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(1, 6), (2, 6), (2, 7), (2, 8)])
    puzzle.add_renban([(1, 7), (0, 7), (0, 6)])
    puzzle.add_renban([(4, 2), (5, 2), (6, 2)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(8, 3), (7, 4), (6, 5)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(4, 6), (4, 5)])
    puzzle.add_renban([(1, 4), (1, 5)])
    puzzle.add_renban([(7, 7), (7, 6)])
    puzzle.add_renban([(8, 4), (7, 5)])

    return puzzle
