"""PuzzleMadness Renban Sudoku — 2025-11-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [8, 0, 0, 0, 6, 0, 0, 3, 0],
        [0, 9, 0, 0, 0, 0, 1, 5, 0],
        [0, 4, 0, 1, 0, 0, 8, 0, 6],
        [1, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 3, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(8, 1), (8, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8), (5, 7), (5, 6)])
    puzzle.add_renban([(4, 6), (4, 7), (4, 8), (3, 8), (2, 8)])
    puzzle.add_renban([(7, 3), (7, 4), (6, 4), (5, 4)])
    puzzle.add_renban([(4, 1), (3, 2), (2, 3), (1, 2)])
    puzzle.add_renban([(1, 0), (2, 0), (2, 1), (2, 2)])
    puzzle.add_renban([(2, 4), (2, 5), (2, 6)])
    puzzle.add_renban([(1, 5), (0, 4), (1, 3)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6)])
    puzzle.add_renban([(7, 5), (6, 6), (5, 5)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(0, 7), (0, 6)])
    puzzle.add_renban([(7, 1), (6, 2)])
    puzzle.add_renban([(7, 7), (6, 7)])
    puzzle.add_renban([(6, 1), (5, 2)])

    return puzzle
