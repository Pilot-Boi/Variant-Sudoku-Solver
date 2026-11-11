"""PuzzleMadness Renban Sudoku — 2025-09-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 1, 0, 0, 7, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 8],
        [7, 0, 0, 6, 0, 5, 0, 0, 2],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 2, 8, 0],
        [0, 0, 2, 0, 0, 0, 5, 0, 0],
        [2, 0, 9, 3, 0, 0, 7, 0, 0],
        [0, 5, 0, 7, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(6, 8), (6, 7), (6, 6), (7, 6)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6), (2, 6)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(6, 3), (5, 3), (5, 2)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(4, 4), (3, 4), (3, 3)])
    puzzle.add_renban([(0, 4), (0, 5)])
    puzzle.add_renban([(4, 8), (3, 7)])
    puzzle.add_renban([(4, 7), (5, 7)])
    puzzle.add_renban([(7, 5), (6, 5)])
    puzzle.add_renban([(1, 2), (2, 3)])

    return puzzle
