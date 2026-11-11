"""PuzzleMadness Renban Sudoku — 2025-07-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 7, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 7, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 6, 1, 0, 0, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 3, 7, 0],
        [4, 0, 0, 0, 0, 8, 0, 0, 5],
        [6, 1, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 2, 0, 0, 0],
        [7, 0, 0, 0, 0, 5, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (4, 5), (4, 6), (4, 7), (4, 8)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(5, 2), (6, 2), (7, 2), (7, 3)])
    puzzle.add_renban([(3, 5), (2, 6), (1, 5), (0, 4)])
    puzzle.add_renban([(7, 5), (6, 5), (6, 4)])
    puzzle.add_renban([(3, 4), (2, 5), (1, 4)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(2, 8), (3, 8)])
    puzzle.add_renban([(1, 7), (1, 6)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(6, 3), (5, 4)])

    return puzzle
