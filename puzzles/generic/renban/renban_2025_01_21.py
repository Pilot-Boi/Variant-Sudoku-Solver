"""PuzzleMadness Renban Sudoku — 2025-01-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 7, 0, 0, 6, 0, 0, 0, 3],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [1, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 6, 0, 4, 0, 3, 0, 8, 2],
        [0, 3, 0, 0, 9, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 2, 8, 9, 0],
        [8, 0, 4, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)])
    puzzle.add_renban([(3, 4), (3, 5), (3, 6), (3, 7), (3, 8)])
    puzzle.add_renban([(6, 5), (6, 6), (6, 7), (5, 7), (4, 7)])
    puzzle.add_renban([(7, 2), (7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(4, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(4, 2), (5, 3), (6, 4)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6)])
    puzzle.add_renban([(8, 4), (8, 5)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(1, 2), (2, 3)])
    puzzle.add_renban([(2, 2), (3, 3)])
    puzzle.add_renban([(7, 7), (7, 6)])

    return puzzle
