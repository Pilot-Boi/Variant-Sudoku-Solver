"""PuzzleMadness Renban Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 7, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 3, 0, 0, 4, 0, 0, 0],
        [0, 0, 4, 5, 0, 3, 8, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 5],
        [0, 0, 6, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 8],
        [3, 0, 0, 0, 6, 8, 0, 7, 0],
        [5, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_renban([(4, 2), (4, 1), (4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    puzzle.add_renban([(4, 5), (4, 6), (4, 7), (3, 7)])
    puzzle.add_renban([(8, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(7, 8), (6, 8), (6, 7), (6, 6)])
    puzzle.add_renban([(2, 7), (2, 6), (3, 6)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(6, 2), (5, 2), (5, 1)])
    puzzle.add_renban([(1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(3, 3), (3, 4)])
    puzzle.add_renban([(4, 3), (5, 4)])
    puzzle.add_renban([(3, 1), (3, 2)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(7, 0), (7, 1)])

    return puzzle
