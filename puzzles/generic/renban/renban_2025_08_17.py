"""PuzzleMadness Renban Sudoku — 2025-08-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 3, 0, 0, 9, 0],
        [4, 6, 0, 0, 5, 0, 0, 8, 2],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 3, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 2, 4],
        [0, 0, 0, 6, 0, 4, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [8, 7, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 5), (2, 6), (2, 7), (1, 7), (0, 7)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(7, 0), (6, 1), (5, 2), (4, 3)])
    puzzle.add_renban([(3, 4), (4, 4), (5, 4), (6, 4)])
    puzzle.add_renban([(8, 3), (8, 4), (7, 4)])
    puzzle.add_renban([(5, 5), (6, 5), (6, 6)])
    puzzle.add_renban([(4, 6), (5, 6)])
    puzzle.add_renban([(4, 2), (3, 3)])
    puzzle.add_renban([(3, 6), (3, 5)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(4, 1), (5, 1)])

    return puzzle
