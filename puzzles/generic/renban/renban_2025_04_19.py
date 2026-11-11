"""PuzzleMadness Renban Sudoku — 2025-04-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 5, 0, 7, 6, 0],
        [0, 2, 0, 0, 1, 0, 0, 0, 9],
        [6, 8, 0, 5, 9, 0, 2, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 6, 1, 4, 5, 0],
        [3, 0, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 6), (5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_renban([(4, 6), (3, 6), (2, 6), (2, 5), (2, 4)])
    puzzle.add_renban([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(2, 2), (3, 3), (4, 4), (3, 5)])
    puzzle.add_renban([(6, 0), (6, 1), (6, 2), (6, 3)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(7, 8), (6, 8), (6, 7)])
    puzzle.add_renban([(5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(2, 1), (3, 2), (4, 3)])
    puzzle.add_renban([(4, 1), (5, 1)])
    puzzle.add_renban([(2, 0), (3, 0)])
    puzzle.add_renban([(7, 7), (7, 6)])
    puzzle.add_renban([(6, 6), (6, 5)])
    puzzle.add_renban([(1, 8), (2, 8)])

    return puzzle
