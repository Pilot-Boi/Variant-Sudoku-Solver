"""PuzzleMadness Renban Sudoku — 2025-11-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 4, 0, 0, 0, 9, 3, 0, 0],
        [0, 1, 7, 3, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 3, 1, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 8],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [4, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(2, 7), (2, 6), (2, 5), (3, 5), (4, 5)])
    puzzle.add_renban([(2, 4), (3, 4), (4, 4), (5, 4), (6, 4)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(6, 1), (6, 2), (6, 3), (5, 3)])
    puzzle.add_renban([(2, 2), (3, 1), (4, 2)])
    puzzle.add_renban([(1, 2), (2, 3), (1, 4)])
    puzzle.add_renban([(7, 7), (6, 8), (5, 7)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6)])
    puzzle.add_renban([(4, 1), (5, 1)])
    puzzle.add_renban([(4, 6), (5, 5)])
    puzzle.add_renban([(8, 3), (8, 4)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(1, 7), (1, 6)])

    return puzzle
