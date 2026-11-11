"""PuzzleMadness Renban Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 8, 0, 0, 0],
        [3, 0, 0, 0, 7, 0, 4, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 2, 4, 0, 5, 0],
        [0, 0, 4, 9, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 6, 2, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 7, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 5), (1, 4), (1, 3), (2, 3), (3, 3)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (7, 6), (6, 6)])
    puzzle.add_renban([(2, 8), (1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(3, 8), (2, 7), (1, 6), (2, 5)])
    puzzle.add_renban([(7, 2), (6, 2), (5, 2), (5, 1)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(2, 2), (2, 1), (3, 1)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(8, 8), (7, 8)])
    puzzle.add_renban([(4, 8), (5, 7)])
    puzzle.add_renban([(4, 6), (5, 6)])
    puzzle.add_renban([(4, 7), (3, 6)])

    return puzzle
