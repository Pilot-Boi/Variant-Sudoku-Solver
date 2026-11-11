"""PuzzleMadness Renban Sudoku — 2025-12-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [6, 0, 8, 0, 4, 0, 1, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 8],
        [8, 0, 0, 0, 5, 0, 2, 0, 0],
        [5, 0, 0, 0, 9, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 8, 0],
        [3, 0, 0, 0, 7, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(7, 6), (6, 7), (5, 8), (4, 7), (3, 6)])
    puzzle.add_renban([(5, 4), (5, 3), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(5, 5), (4, 5), (4, 4), (4, 3)])
    puzzle.add_renban([(0, 5), (1, 4), (2, 3), (3, 4)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(7, 5), (6, 5), (6, 4)])
    puzzle.add_renban([(1, 2), (1, 1), (2, 1)])
    puzzle.add_renban([(1, 7), (2, 6), (3, 5)])
    puzzle.add_renban([(5, 1), (4, 2), (3, 1)])
    puzzle.add_renban([(7, 3), (6, 3)])
    puzzle.add_renban([(4, 6), (5, 6)])
    puzzle.add_renban([(7, 0), (7, 1)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(7, 8), (7, 7)])

    return puzzle
