"""PuzzleMadness Renban Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 4, 5, 0, 0],
        [3, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 4, 0, 3, 0, 0],
        [0, 9, 0, 0, 8, 6, 4, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 5, 0, 0, 0, 0, 0, 3],
        [1, 0, 0, 4, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)])
    puzzle.add_renban([(4, 8), (5, 8), (6, 8), (7, 8), (8, 8)])
    puzzle.add_renban([(6, 3), (6, 2), (6, 1), (7, 1), (8, 1)])
    puzzle.add_renban([(2, 7), (1, 6), (2, 5), (3, 4)])
    puzzle.add_renban([(4, 6), (3, 5), (4, 4), (5, 3)])
    puzzle.add_renban([(7, 2), (7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(1, 0), (2, 0), (2, 1)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(4, 5), (5, 4)])
    puzzle.add_renban([(2, 8), (3, 8)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(0, 4), (1, 3)])
    puzzle.add_renban([(7, 7), (7, 6)])

    return puzzle
