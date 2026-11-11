"""PuzzleMadness Renban Sudoku — 2025-01-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 4, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 5, 0, 0, 7, 0],
        [0, 0, 8, 0, 0, 0, 3, 6, 0],
        [5, 0, 0, 0, 1, 3, 2, 0, 0],
        [0, 5, 0, 8, 0, 0, 0, 0, 0],
        [9, 0, 0, 1, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 3), (2, 3), (3, 3), (3, 4), (3, 5)])
    puzzle.add_renban([(4, 4), (4, 5), (4, 6), (4, 7), (4, 8)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (7, 7), (7, 8)])
    puzzle.add_renban([(0, 8), (1, 8), (2, 8), (3, 8)])
    puzzle.add_renban([(1, 6), (0, 6), (0, 5), (0, 4)])
    puzzle.add_renban([(6, 3), (5, 3), (5, 2), (5, 1)])
    puzzle.add_renban([(5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2)])
    puzzle.add_renban([(7, 1), (7, 2), (6, 2)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2)])
    puzzle.add_renban([(1, 4), (2, 5)])
    puzzle.add_renban([(6, 7), (6, 6)])
    puzzle.add_renban([(4, 0), (3, 1)])
    puzzle.add_renban([(2, 7), (2, 6)])
    puzzle.add_renban([(4, 1), (4, 2)])

    return puzzle
