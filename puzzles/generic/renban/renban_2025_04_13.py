"""PuzzleMadness Renban Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 3, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 7, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 4],
        [0, 7, 0, 2, 0, 0, 0, 0, 8],
        [0, 0, 3, 0, 7, 0, 0, 9, 0],
        [0, 5, 0, 0, 0, 3, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 5, 9, 0, 0],
        [0, 0, 0, 9, 0, 2, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 3), (1, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_renban([(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])
    puzzle.add_renban([(4, 8), (5, 7), (6, 6), (7, 7), (8, 8)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (6, 5)])
    puzzle.add_renban([(4, 2), (4, 1), (4, 0), (5, 0)])
    puzzle.add_renban([(5, 5), (4, 6), (3, 7), (2, 6)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(4, 3), (4, 4), (4, 5)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6)])
    puzzle.add_renban([(6, 3), (6, 4)])
    puzzle.add_renban([(1, 4), (1, 5)])
    puzzle.add_renban([(7, 1), (7, 2)])
    puzzle.add_renban([(6, 1), (5, 1)])
    puzzle.add_renban([(1, 0), (2, 0)])

    return puzzle
