"""PuzzleMadness Renban Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 0, 7],
        [0, 6, 0, 0, 0, 0, 0, 2, 0],
        [7, 0, 0, 6, 0, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 9, 0],
        [4, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 9, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 6), (7, 7), (7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(1, 1), (2, 2), (3, 3), (2, 4), (1, 5)])
    puzzle.add_renban([(6, 6), (5, 5), (4, 4), (5, 3), (6, 2)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(3, 2), (4, 2), (5, 2)])
    puzzle.add_renban([(7, 5), (8, 5), (8, 6)])
    puzzle.add_renban([(7, 3), (7, 4), (6, 4)])
    puzzle.add_renban([(0, 7), (1, 6), (2, 5)])
    puzzle.add_renban([(1, 3), (1, 4)])
    puzzle.add_renban([(1, 2), (2, 3)])
    puzzle.add_renban([(6, 7), (5, 7)])
    puzzle.add_renban([(3, 8), (4, 7)])
    puzzle.add_renban([(7, 0), (6, 1)])

    return puzzle
