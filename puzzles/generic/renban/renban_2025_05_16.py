"""PuzzleMadness Renban Sudoku — 2025-05-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [6, 0, 0, 0, 3, 0, 0, 0, 4],
        [0, 6, 0, 7, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 9, 0, 0, 0, 0, 3, 5],
        [1, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(4, 8), (3, 8), (2, 8), (2, 7), (2, 6)])
    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (4, 6), (4, 7)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (6, 1)])
    puzzle.add_renban([(8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(1, 4), (2, 4), (3, 4), (4, 4)])
    puzzle.add_renban([(1, 0), (2, 0), (2, 1)])
    puzzle.add_renban([(1, 5), (0, 4), (1, 3)])
    puzzle.add_renban([(7, 4), (6, 4), (5, 4)])
    puzzle.add_renban([(3, 2), (3, 1), (4, 1)])
    puzzle.add_renban([(4, 2), (4, 3)])
    puzzle.add_renban([(7, 2), (6, 3)])
    puzzle.add_renban([(6, 5), (5, 5)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(0, 7), (1, 7)])

    return puzzle
