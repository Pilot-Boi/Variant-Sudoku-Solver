"""PuzzleMadness Renban Sudoku — 2025-07-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 5, 2, 7, 0],
        [0, 5, 0, 9, 1, 0, 0, 6, 8],
        [5, 0, 0, 6, 0, 0, 3, 0, 0],
        [6, 0, 0, 0, 8, 2, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 6, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 2), (5, 2), (4, 2), (4, 1), (4, 0)])
    puzzle.add_renban([(4, 8), (4, 7), (4, 6), (5, 6), (6, 6)])
    puzzle.add_renban([(2, 5), (1, 4), (0, 3), (1, 2), (2, 1)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (6, 5)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(3, 5), (3, 4), (4, 4)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(6, 8), (5, 7)])
    puzzle.add_renban([(8, 1), (8, 2)])
    puzzle.add_renban([(8, 0), (7, 1)])
    puzzle.add_renban([(6, 0), (5, 0)])
    puzzle.add_renban([(8, 8), (8, 7)])

    return puzzle
