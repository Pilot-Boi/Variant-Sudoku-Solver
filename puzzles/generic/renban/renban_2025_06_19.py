"""PuzzleMadness Renban Sudoku — 2025-06-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 3, 1, 0, 2, 0, 0, 0],
        [6, 0, 2, 8, 0, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 7, 0, 0, 9],
        [0, 0, 0, 0, 8, 3, 0, 2, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 6, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 6, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 2), (1, 1), (1, 0), (2, 0), (3, 0)])
    puzzle.add_renban([(4, 6), (3, 6), (2, 6), (2, 5), (2, 4)])
    puzzle.add_renban([(5, 3), (6, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(8, 6), (7, 6), (6, 6), (5, 6)])
    puzzle.add_renban([(3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(0, 6), (0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(2, 2), (2, 1), (3, 1)])
    puzzle.add_renban([(4, 2), (5, 2), (6, 2)])
    puzzle.add_renban([(2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(4, 0), (5, 0)])
    puzzle.add_renban([(7, 0), (6, 1)])
    puzzle.add_renban([(4, 8), (5, 7)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(6, 4), (5, 5)])

    return puzzle
