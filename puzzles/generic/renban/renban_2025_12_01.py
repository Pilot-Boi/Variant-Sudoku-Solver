"""PuzzleMadness Renban Sudoku — 2025-12-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 6, 0, 0, 0],
        [2, 0, 3, 0, 8, 0, 0, 6, 0],
        [0, 0, 0, 0, 1, 7, 0, 0, 8],
        [0, 0, 6, 0, 0, 0, 0, 0, 7],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 6, 5, 0],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 2, 6, 4, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 8, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 6), (4, 5), (3, 4), (4, 3), (5, 2)])
    puzzle.add_renban([(7, 6), (7, 7), (7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(8, 1), (8, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(0, 6), (0, 5), (1, 5), (2, 5)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(2, 3), (2, 2), (3, 2), (4, 2)])
    puzzle.add_renban([(2, 7), (3, 6), (4, 7)])
    puzzle.add_renban([(7, 4), (6, 4), (6, 3)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8)])
    puzzle.add_renban([(7, 3), (6, 2), (7, 1)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(2, 4), (3, 5)])
    puzzle.add_renban([(0, 3), (1, 4)])
    puzzle.add_renban([(1, 7), (2, 6)])
    puzzle.add_renban([(1, 2), (1, 3)])

    return puzzle
