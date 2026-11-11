"""PuzzleMadness Renban Sudoku — 2025-09-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 2, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 2, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 6, 0, 8],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 9, 3, 0, 0, 0, 0, 5, 0],
        [1, 0, 0, 8, 7, 0, 0, 0, 5],
        [0, 5, 0, 0, 6, 4, 0, 3, 0],
        [0, 0, 6, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(7, 7), (6, 7), (5, 7), (5, 6), (5, 5)])
    puzzle.add_renban([(1, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_renban([(3, 8), (3, 7), (3, 6), (4, 6)])
    puzzle.add_renban([(5, 2), (5, 3), (4, 3), (3, 3)])
    puzzle.add_renban([(6, 2), (6, 1), (7, 1)])
    puzzle.add_renban([(1, 2), (2, 1), (3, 2)])
    puzzle.add_renban([(5, 8), (4, 8), (4, 7)])
    puzzle.add_renban([(1, 4), (0, 4), (0, 3)])
    puzzle.add_renban([(3, 1), (4, 2)])
    puzzle.add_renban([(4, 1), (5, 1)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(7, 3), (6, 3)])

    return puzzle
