"""PuzzleMadness Renban Sudoku — 2025-01-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 7, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 0],
        [3, 0, 0, 0, 0, 4, 1, 2, 0],
        [4, 0, 5, 0, 0, 7, 0, 0, 0],
        [0, 0, 7, 3, 0, 0, 0, 5, 0],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 4, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)])
    puzzle.add_renban([(6, 3), (6, 2), (6, 1), (7, 1), (8, 1)])
    puzzle.add_renban([(5, 5), (4, 5), (3, 5), (3, 4), (3, 3)])
    puzzle.add_renban([(5, 1), (5, 2), (4, 2), (3, 2)])
    puzzle.add_renban([(3, 7), (4, 7), (5, 7), (6, 7)])
    puzzle.add_renban([(7, 6), (6, 5), (5, 4)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(8, 8), (7, 8)])
    puzzle.add_renban([(1, 0), (1, 1)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(0, 0), (0, 1)])

    return puzzle
