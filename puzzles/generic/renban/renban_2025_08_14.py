"""PuzzleMadness Renban Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 0, 4, 9, 1, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [2, 0, 3, 9, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 9],
        [0, 0, 0, 0, 0, 0, 2, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [8, 0, 5, 0, 0, 1, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)])
    puzzle.add_renban([(3, 5), (2, 5), (1, 5), (1, 4), (1, 3)])
    puzzle.add_renban([(4, 6), (4, 7), (4, 8), (3, 8), (2, 8)])
    puzzle.add_renban([(1, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_renban([(6, 2), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(7, 5), (6, 5), (6, 4), (6, 3)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(6, 1), (5, 2), (4, 1)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(2, 1), (2, 2)])
    puzzle.add_renban([(0, 7), (0, 6)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(4, 0), (3, 1)])
    puzzle.add_renban([(1, 7), (2, 7)])

    return puzzle
