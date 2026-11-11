"""PuzzleMadness Renban Sudoku — 2025-08-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 0, 0, 0, 0, 1, 8, 0],
        [0, 0, 2, 0, 0, 3, 0, 0, 0],
        [0, 0, 7, 1, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 4, 7, 0, 0],
        [3, 0, 0, 0, 8, 0, 0, 9, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 3, 7, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 6), (3, 6), (4, 6), (5, 6), (6, 6)])
    puzzle.add_renban([(5, 3), (4, 4), (3, 5), (2, 4), (1, 3)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(1, 4), (2, 5), (1, 6), (0, 7)])
    puzzle.add_renban([(6, 2), (6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (7, 2)])
    puzzle.add_renban([(1, 2), (0, 2), (0, 1)])
    puzzle.add_renban([(6, 5), (6, 4), (7, 4)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(6, 7), (6, 8), (5, 8)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(3, 8), (3, 7)])
    puzzle.add_renban([(3, 1), (4, 2)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(2, 1), (2, 2)])

    return puzzle
