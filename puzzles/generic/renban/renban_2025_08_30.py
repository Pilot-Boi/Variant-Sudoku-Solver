"""PuzzleMadness Renban Sudoku — 2025-08-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 0, 0, 0, 7],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 9, 0, 0, 4, 0],
        [0, 3, 0, 0, 5, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 8, 0],
        [4, 0, 3, 9, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 5, 0, 2, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6), (6, 7)])
    puzzle.add_renban([(2, 5), (1, 5), (1, 4), (1, 3)])
    puzzle.add_renban([(4, 2), (4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(7, 6), (6, 5), (5, 4)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(8, 3), (8, 4), (7, 4)])
    puzzle.add_renban([(8, 0), (7, 1), (6, 2)])
    puzzle.add_renban([(8, 6), (7, 5)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(4, 0), (3, 1)])
    puzzle.add_renban([(3, 7), (4, 6)])

    return puzzle
