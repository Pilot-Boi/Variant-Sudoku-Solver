"""PuzzleMadness Renban Sudoku — 2025-08-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 2, 9, 5, 1],
        [9, 7, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 1, 0],
        [2, 0, 0, 5, 0, 0, 0, 3, 0],
        [8, 0, 5, 9, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 6, 0, 8, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8), (4, 8), (5, 8)])
    puzzle.add_renban([(3, 6), (4, 5), (5, 4), (6, 5), (7, 6)])
    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(6, 2), (7, 2), (8, 2), (8, 3)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(1, 2), (1, 3), (1, 4)])
    puzzle.add_renban([(2, 6), (2, 7), (1, 7)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(0, 4), (1, 5)])
    puzzle.add_renban([(8, 4), (7, 5)])
    puzzle.add_renban([(2, 4), (2, 5)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(3, 4), (4, 3)])

    return puzzle
