"""PuzzleMadness Renban Sudoku — 2025-07-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 4],
        [0, 0, 0, 7, 0, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 9, 6, 1, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 6],
        [0, 0, 2, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 6, 5, 7, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 4), (3, 5), (3, 6), (3, 7), (3, 8)])
    puzzle.add_renban([(5, 1), (5, 2), (5, 3), (4, 3), (3, 3)])
    puzzle.add_renban([(3, 2), (2, 2), (1, 2), (1, 1), (1, 0)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (6, 2)])
    puzzle.add_renban([(4, 4), (5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(7, 7), (6, 8), (5, 7)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(0, 4), (0, 3), (1, 3)])
    puzzle.add_renban([(1, 6), (0, 5), (1, 4)])
    puzzle.add_renban([(4, 8), (4, 7)])
    puzzle.add_renban([(5, 0), (4, 1)])
    puzzle.add_renban([(4, 6), (4, 5)])
    puzzle.add_renban([(3, 0), (3, 1)])
    puzzle.add_renban([(8, 0), (8, 1)])

    return puzzle
