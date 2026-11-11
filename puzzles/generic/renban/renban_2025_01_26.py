"""PuzzleMadness Renban Sudoku — 2025-01-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 5, 0, 0, 0, 0, 0, 0],
        [1, 0, 2, 0, 0, 8, 0, 5, 0],
        [0, 6, 0, 0, 9, 0, 0, 0, 0],
        [0, 8, 3, 0, 0, 0, 1, 0, 6],
        [4, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [7, 3, 0, 0, 0, 1, 0, 0, 5],
        [8, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(4, 6), (5, 6), (6, 6), (7, 6), (8, 6)])
    puzzle.add_renban([(0, 1), (1, 1), (2, 1), (2, 2), (2, 3)])
    puzzle.add_renban([(2, 8), (1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(6, 1), (7, 1), (8, 1), (8, 2)])
    puzzle.add_renban([(6, 7), (6, 8), (5, 8)])
    puzzle.add_renban([(2, 4), (3, 4), (4, 4)])
    puzzle.add_renban([(7, 4), (6, 4), (5, 4)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(8, 4), (8, 5)])
    puzzle.add_renban([(3, 1), (4, 1)])
    puzzle.add_renban([(7, 2), (7, 3)])
    puzzle.add_renban([(3, 5), (4, 5)])
    puzzle.add_renban([(3, 3), (4, 3)])

    return puzzle
