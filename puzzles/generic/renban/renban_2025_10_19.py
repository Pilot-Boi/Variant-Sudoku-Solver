"""PuzzleMadness Renban Sudoku — 2025-10-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 4, 0, 0, 0, 0, 0, 3],
        [0, 6, 2, 0, 0, 3, 0, 1, 0],
        [0, 0, 0, 8, 0, 4, 6, 0, 0],
        [5, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 2, 8, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(5, 5), (4, 6), (3, 7), (2, 6), (1, 5)])
    puzzle.add_renban([(2, 5), (2, 4), (3, 4), (4, 4)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0), (5, 0)])
    puzzle.add_renban([(2, 8), (1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(1, 6), (0, 6), (0, 5)])
    puzzle.add_renban([(4, 2), (5, 3), (6, 4)])
    puzzle.add_renban([(4, 7), (3, 8), (2, 7)])
    puzzle.add_renban([(7, 2), (6, 2)])
    puzzle.add_renban([(0, 1), (1, 2)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(6, 1), (5, 1)])
    puzzle.add_renban([(6, 6), (6, 5)])

    return puzzle
