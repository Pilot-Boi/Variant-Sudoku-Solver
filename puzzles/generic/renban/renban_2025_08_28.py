"""PuzzleMadness Renban Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 8, 0, 0, 5, 3, 4, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 6, 8, 1, 0, 5, 0],
        [0, 7, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 3, 7, 0, 2, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 9, 0, 0, 0, 5, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(0, 7), (1, 7), (2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(7, 3), (6, 4), (5, 5), (4, 4), (3, 3)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_renban([(2, 2), (1, 2), (1, 1), (1, 0)])
    puzzle.add_renban([(5, 2), (5, 3), (4, 3)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
    puzzle.add_renban([(3, 4), (4, 5), (3, 6)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(4, 6), (5, 6)])
    puzzle.add_renban([(8, 4), (7, 5)])
    puzzle.add_renban([(8, 3), (7, 4)])
    puzzle.add_renban([(1, 4), (2, 5)])
    puzzle.add_renban([(2, 8), (3, 8)])

    return puzzle
