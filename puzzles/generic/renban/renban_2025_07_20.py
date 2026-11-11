"""PuzzleMadness Renban Sudoku — 2025-07-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [2, 0, 8, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 7],
        [0, 0, 1, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 8, 4, 0, 0, 5, 0, 0, 0],
        [0, 3, 5, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 1],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 3), (6, 2), (6, 1), (7, 1), (8, 1)])
    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(3, 8), (3, 7), (3, 6), (4, 6), (5, 6)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6), (2, 6)])
    puzzle.add_renban([(0, 4), (1, 3), (2, 2), (3, 3)])
    puzzle.add_renban([(5, 4), (6, 4), (6, 5), (6, 6)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(4, 3), (3, 4), (2, 3)])
    puzzle.add_renban([(0, 7), (0, 6)])
    puzzle.add_renban([(5, 8), (5, 7)])
    puzzle.add_renban([(1, 4), (2, 4)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(4, 8), (4, 7)])

    return puzzle
