"""PuzzleMadness Renban Sudoku — 2025-06-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 7, 6, 4, 0, 1, 2, 0],
        [0, 8, 6, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 0, 0, 9, 6, 0, 0],
        [0, 0, 2, 0, 0, 6, 0, 0, 0],
        [0, 2, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 6, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 6), (5, 6), (6, 6), (7, 6), (8, 6)])
    puzzle.add_renban([(6, 2), (5, 2), (4, 2), (4, 1), (4, 0)])
    puzzle.add_renban([(2, 2), (2, 3), (2, 4), (1, 4), (0, 4)])
    puzzle.add_renban([(8, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(2, 8), (1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(4, 7), (5, 7), (6, 7)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(5, 1), (5, 0), (6, 0)])
    puzzle.add_renban([(3, 6), (2, 5), (3, 4)])
    puzzle.add_renban([(0, 6), (0, 5)])
    puzzle.add_renban([(0, 1), (1, 1)])
    puzzle.add_renban([(3, 3), (4, 3)])
    puzzle.add_renban([(2, 7), (2, 6)])
    puzzle.add_renban([(2, 0), (3, 1)])

    return puzzle
