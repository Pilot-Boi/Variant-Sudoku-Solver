"""PuzzleMadness Renban Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 4, 0, 6, 2, 7, 0, 0],
        [0, 2, 6, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 7, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 6],
        [0, 4, 0, 0, 9, 0, 2, 3, 0],
        [0, 0, 2, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(0, 4), (1, 5), (2, 6), (1, 7), (0, 8)])
    puzzle.add_renban([(7, 1), (6, 2), (5, 3), (4, 2), (3, 1)])
    puzzle.add_renban([(3, 5), (4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_renban([(4, 7), (5, 6), (6, 7)])
    puzzle.add_renban([(3, 2), (3, 3), (3, 4)])
    puzzle.add_renban([(5, 2), (5, 1), (6, 1)])
    puzzle.add_renban([(8, 3), (7, 3), (6, 3)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(8, 6), (7, 5)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(3, 8), (3, 7)])
    puzzle.add_renban([(2, 4), (2, 5)])

    return puzzle
