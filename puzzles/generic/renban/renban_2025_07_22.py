"""PuzzleMadness Renban Sudoku — 2025-07-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 1, 0, 2, 8, 0],
        [4, 0, 0, 2, 0, 6, 0, 5, 0],
        [0, 9, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 6, 0],
        [5, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 1), (6, 2), (6, 3), (5, 3), (4, 3)])
    puzzle.add_renban([(3, 8), (2, 7), (1, 6), (2, 5), (3, 4)])
    puzzle.add_renban([(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)])
    puzzle.add_renban([(6, 4), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(4, 4), (4, 5), (4, 6), (4, 7)])
    puzzle.add_renban([(8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(0, 4), (1, 3), (2, 2)])
    puzzle.add_renban([(5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(1, 1), (2, 1)])
    puzzle.add_renban([(7, 1), (7, 2)])
    puzzle.add_renban([(8, 5), (7, 5)])
    puzzle.add_renban([(3, 0), (4, 0)])
    puzzle.add_renban([(0, 8), (1, 7)])

    return puzzle
