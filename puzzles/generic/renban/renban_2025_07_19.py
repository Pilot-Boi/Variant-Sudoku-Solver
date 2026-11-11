"""PuzzleMadness Renban Sudoku — 2025-07-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 9, 0, 8],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [1, 0, 7, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 2],
        [0, 0, 0, 0, 6, 0, 0, 8, 5],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 7, 2, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(1, 6), (2, 5), (3, 4), (4, 5), (5, 6)])
    puzzle.add_renban([(5, 7), (4, 7), (3, 7), (3, 6), (3, 5)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(4, 2), (5, 2), (5, 3), (5, 4)])
    puzzle.add_renban([(2, 7), (1, 7), (0, 7), (0, 6)])
    puzzle.add_renban([(0, 1), (0, 2), (0, 3)])
    puzzle.add_renban([(6, 5), (7, 6), (6, 7)])
    puzzle.add_renban([(0, 8), (1, 8), (2, 8)])
    puzzle.add_renban([(7, 4), (6, 3), (7, 2)])
    puzzle.add_renban([(1, 2), (1, 3)])
    puzzle.add_renban([(2, 3), (3, 3)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(1, 4), (1, 5)])

    return puzzle
