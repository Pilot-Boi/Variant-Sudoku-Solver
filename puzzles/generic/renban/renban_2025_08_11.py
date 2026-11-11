"""PuzzleMadness Renban Sudoku — 2025-08-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 7, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 5, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 3, 9, 0, 1],
        [0, 0, 9, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 0, 4, 0],
        [7, 0, 0, 0, 0, 0, 3, 6, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [6, 0, 0, 0, 0, 4, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (3, 4), (2, 4), (2, 3), (2, 2)])
    puzzle.add_renban([(6, 7), (6, 6), (6, 5), (7, 5), (8, 5)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(0, 8), (1, 7), (2, 6), (3, 5)])
    puzzle.add_renban([(5, 2), (6, 2), (7, 2), (7, 3)])
    puzzle.add_renban([(1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(5, 7), (4, 7), (4, 6)])
    puzzle.add_renban([(1, 6), (2, 5)])
    puzzle.add_renban([(4, 3), (5, 4)])
    puzzle.add_renban([(3, 0), (4, 1)])
    puzzle.add_renban([(2, 0), (2, 1)])
    puzzle.add_renban([(7, 4), (6, 3)])

    return puzzle
