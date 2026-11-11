"""PuzzleMadness Renban Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 4, 0, 8, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 2, 3, 0],
        [9, 0, 0, 0, 0, 3, 5, 0, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 4, 6, 5, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 7, 0, 0, 0, 1, 6, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (4, 1)])
    puzzle.add_renban([(5, 0), (6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(1, 4), (2, 4), (3, 4), (4, 4)])
    puzzle.add_renban([(8, 3), (8, 4), (7, 4)])
    puzzle.add_renban([(4, 8), (4, 7), (4, 6)])
    puzzle.add_renban([(3, 2), (2, 3), (1, 2)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(6, 5), (5, 4)])
    puzzle.add_renban([(7, 8), (6, 7)])
    puzzle.add_renban([(6, 1), (5, 2)])
    puzzle.add_renban([(6, 6), (5, 6)])
    puzzle.add_renban([(2, 7), (3, 6)])

    return puzzle
