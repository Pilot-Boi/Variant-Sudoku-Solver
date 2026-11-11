"""PuzzleMadness Renban Sudoku — 2025-09-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 0, 4],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 1, 5, 0, 0, 8],
        [0, 7, 6, 0, 0, 0, 0, 0, 0],
        [9, 0, 8, 0, 7, 4, 0, 0, 0],
        [3, 5, 0, 0, 0, 0, 1, 0, 0],
        [5, 0, 7, 0, 9, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 3, 2, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])
    puzzle.add_renban([(6, 4), (7, 4), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(0, 2), (1, 1), (2, 0), (3, 1)])
    puzzle.add_renban([(8, 0), (7, 1), (6, 2), (5, 1)])
    puzzle.add_renban([(2, 5), (1, 4), (2, 3), (3, 2)])
    puzzle.add_renban([(0, 4), (0, 3), (1, 3)])
    puzzle.add_renban([(8, 2), (8, 3), (7, 3)])
    puzzle.add_renban([(4, 1), (5, 0), (6, 1)])
    puzzle.add_renban([(3, 8), (2, 8), (2, 7)])
    puzzle.add_renban([(6, 8), (5, 8)])
    puzzle.add_renban([(6, 3), (5, 3)])
    puzzle.add_renban([(4, 7), (5, 6)])
    puzzle.add_renban([(6, 7), (6, 6)])
    puzzle.add_renban([(6, 5), (5, 4)])

    return puzzle
