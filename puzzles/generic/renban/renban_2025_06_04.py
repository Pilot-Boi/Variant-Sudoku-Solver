"""PuzzleMadness Renban Sudoku — 2025-06-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 5, 0],
        [2, 0, 0, 0, 0, 3, 0, 0, 9],
        [3, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 2, 6, 0, 0, 0],
        [0, 2, 0, 5, 0, 0, 0, 1, 0],
        [4, 0, 0, 0, 0, 0, 8, 0, 0],
        [5, 0, 0, 8, 0, 0, 0, 0, 3],
        [0, 8, 0, 1, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 1), (3, 2), (3, 3), (2, 3), (1, 3)])
    puzzle.add_renban([(6, 6), (6, 5), (6, 4), (7, 4), (8, 4)])
    puzzle.add_renban([(7, 0), (6, 1), (5, 2), (4, 1), (3, 0)])
    puzzle.add_renban([(2, 6), (2, 7), (1, 7), (0, 7)])
    puzzle.add_renban([(2, 4), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(6, 3), (6, 2), (7, 2)])
    puzzle.add_renban([(4, 7), (4, 6), (5, 6)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8)])
    puzzle.add_renban([(4, 0), (5, 1)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(8, 8), (7, 7)])
    puzzle.add_renban([(1, 1), (1, 2)])
    puzzle.add_renban([(0, 4), (1, 4)])

    return puzzle
