"""PuzzleMadness Renban Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [5, 7, 0, 1, 0, 0, 0, 3, 9],
        [0, 4, 0, 2, 0, 0, 7, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 5],
        [0, 0, 0, 5, 0, 0, 0, 0, 7],
        [3, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 2), (3, 2), (4, 2), (5, 2), (6, 2)])
    puzzle.add_renban([(5, 5), (5, 4), (5, 3), (6, 3), (7, 3)])
    puzzle.add_renban([(5, 0), (6, 0), (7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(2, 4), (2, 3), (3, 3), (4, 3)])
    puzzle.add_renban([(6, 4), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(3, 5), (2, 5), (1, 5), (1, 4)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(1, 6), (2, 6), (2, 7)])
    puzzle.add_renban([(1, 7), (0, 7), (0, 6)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(3, 0), (3, 1)])
    puzzle.add_renban([(3, 7), (4, 6)])
    puzzle.add_renban([(0, 2), (1, 2)])
    puzzle.add_renban([(8, 1), (8, 2)])

    return puzzle
