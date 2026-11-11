"""PuzzleMadness Renban Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 6, 0, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 1],
        [7, 0, 4, 0, 3, 0, 0, 5, 8],
        [0, 0, 0, 7, 0, 2, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 2, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 6, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 4), (6, 5), (7, 6), (6, 7), (5, 8)])
    puzzle.add_renban([(4, 5), (4, 6), (4, 7), (3, 7), (2, 7)])
    puzzle.add_renban([(3, 3), (3, 2), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(7, 2), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(0, 3), (0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(2, 2), (2, 3), (2, 4), (1, 4)])
    puzzle.add_renban([(0, 5), (1, 5), (2, 5)])
    puzzle.add_renban([(4, 8), (5, 7), (6, 6)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4)])
    puzzle.add_renban([(4, 2), (4, 3), (4, 4)])
    puzzle.add_renban([(5, 2), (5, 3)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(7, 8), (7, 7)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(0, 7), (1, 6)])

    return puzzle
