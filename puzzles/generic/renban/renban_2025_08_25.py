"""PuzzleMadness Renban Sudoku — 2025-08-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 2, 0, 1, 0],
        [6, 1, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 1, 0, 0, 6, 0, 7],
        [0, 0, 4, 0, 2, 8, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 5, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)])
    puzzle.add_renban([(4, 4), (4, 5), (4, 6), (4, 7), (4, 8)])
    puzzle.add_renban([(6, 1), (7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(2, 2), (2, 3), (1, 3), (0, 3)])
    puzzle.add_renban([(7, 3), (6, 4), (5, 3), (4, 2)])
    puzzle.add_renban([(7, 6), (7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(1, 7), (2, 6), (3, 5)])
    puzzle.add_renban([(6, 3), (6, 2), (7, 2)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(1, 6), (1, 5), (2, 5)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(1, 4), (2, 4)])
    puzzle.add_renban([(8, 4), (7, 4)])
    puzzle.add_renban([(0, 6), (0, 5)])

    return puzzle
