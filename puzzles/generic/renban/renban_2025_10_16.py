"""PuzzleMadness Renban Sudoku — 2025-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 7, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 3, 1, 0, 0, 0, 0, 5],
        [0, 0, 9, 0, 2, 8, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 1, 9, 6, 0, 2],
        [7, 0, 0, 0, 0, 0, 0, 4, 1],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    puzzle.add_renban([(5, 4), (4, 3), (3, 2), (4, 1), (5, 0)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(0, 3), (1, 4), (2, 5), (1, 6)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(8, 1), (7, 1), (6, 1)])
    puzzle.add_renban([(5, 8), (4, 7), (3, 6)])
    puzzle.add_renban([(7, 2), (8, 3), (7, 4)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(2, 7), (3, 7)])
    puzzle.add_renban([(7, 3), (6, 3)])
    puzzle.add_renban([(2, 4), (3, 4)])
    puzzle.add_renban([(8, 4), (7, 5)])

    return puzzle
