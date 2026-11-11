"""PuzzleMadness Renban Sudoku — 2025-03-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 7, 0, 6, 3, 1, 0],
        [0, 8, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 4, 2, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 5, 0, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
        [2, 5, 0, 0, 8, 0, 6, 0, 0],
        [4, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(6, 1), (5, 2), (4, 3), (3, 2), (2, 1)])
    puzzle.add_renban([(2, 6), (2, 7), (2, 8), (1, 8), (0, 8)])
    puzzle.add_renban([(2, 4), (3, 4), (4, 4), (4, 5)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7), (6, 6)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (7, 0)])
    puzzle.add_renban([(5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2)])
    puzzle.add_renban([(7, 6), (6, 5), (7, 4)])
    puzzle.add_renban([(4, 6), (4, 7), (3, 7)])
    puzzle.add_renban([(1, 3), (2, 3)])
    puzzle.add_renban([(6, 3), (5, 3)])
    puzzle.add_renban([(8, 3), (7, 3)])
    puzzle.add_renban([(3, 8), (4, 8)])
    puzzle.add_renban([(8, 0), (7, 1)])

    return puzzle
