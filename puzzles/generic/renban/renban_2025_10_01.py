"""PuzzleMadness Renban Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 9, 0, 0, 0, 0],
        [6, 9, 0, 4, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 5, 0, 0, 0, 4],
        [2, 6, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 3, 1],
        [0, 8, 0, 0, 0, 0, 6, 0, 0],
        [1, 0, 7, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 8, 0, 0, 1, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(4, 4), (3, 5), (2, 6), (1, 5), (0, 4)])
    puzzle.add_renban([(6, 3), (7, 3), (8, 3), (8, 4)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (5, 2)])
    puzzle.add_renban([(8, 2), (7, 2), (6, 2), (6, 1)])
    puzzle.add_renban([(5, 3), (4, 3), (4, 2)])
    puzzle.add_renban([(7, 5), (8, 5), (8, 6)])
    puzzle.add_renban([(0, 7), (1, 7), (2, 7)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3)])
    puzzle.add_renban([(7, 4), (6, 5)])
    puzzle.add_renban([(4, 6), (5, 5)])
    puzzle.add_renban([(2, 8), (3, 8)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(1, 1), (2, 2)])

    return puzzle
