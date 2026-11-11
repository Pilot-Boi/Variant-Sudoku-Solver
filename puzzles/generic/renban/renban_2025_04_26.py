"""PuzzleMadness Renban Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 7, 0, 0, 3, 0, 8],
        [6, 0, 1, 5, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 3, 0],
        [7, 0, 3, 0, 0, 0, 0, 6, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 9, 0, 0, 0, 8, 2, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 6), (4, 5), (3, 4), (4, 3), (5, 2)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(8, 8), (7, 7), (6, 6), (7, 5), (8, 4)])
    puzzle.add_renban([(2, 6), (1, 5), (2, 4), (3, 3)])
    puzzle.add_renban([(2, 7), (2, 8), (1, 8), (0, 8)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 7), (6, 8)])
    puzzle.add_renban([(2, 3), (1, 2), (2, 1)])
    puzzle.add_renban([(4, 7), (4, 8), (3, 8)])
    puzzle.add_renban([(0, 7), (0, 6), (1, 6)])
    puzzle.add_renban([(7, 4), (6, 4), (5, 4)])
    puzzle.add_renban([(1, 3), (1, 4)])
    puzzle.add_renban([(4, 1), (3, 2)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(3, 0), (4, 0)])

    return puzzle
