"""PuzzleMadness Renban Sudoku — 2025-02-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 7, 4, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 9, 0, 0, 2],
        [0, 0, 0, 0, 7, 0, 9, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 8],
        [0, 0, 0, 2, 6, 1, 0, 0, 0],
        [8, 1, 0, 0, 0, 5, 6, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 2), (6, 2), (5, 2), (5, 1), (5, 0)])
    puzzle.add_renban([(0, 7), (1, 7), (2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(5, 4), (5, 5), (5, 6), (4, 6), (3, 6)])
    puzzle.add_renban([(2, 4), (2, 3), (3, 3), (4, 3)])
    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(8, 6), (7, 5), (6, 4)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(5, 7), (5, 8), (4, 8)])
    puzzle.add_renban([(1, 1), (2, 1), (2, 2)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(0, 2), (1, 2)])
    puzzle.add_renban([(0, 4), (1, 5)])
    puzzle.add_renban([(0, 3), (1, 4)])
    puzzle.add_renban([(8, 4), (7, 4)])

    return puzzle
