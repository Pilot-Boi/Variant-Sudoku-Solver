"""PuzzleMadness Renban Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 4],
        [0, 0, 3, 0, 0, 0, 0, 2, 0],
        [0, 0, 1, 9, 4, 0, 3, 0, 6],
        [0, 0, 0, 0, 2, 0, 8, 0, 9],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 4, 0, 1, 0, 3, 0, 0, 0],
        [0, 0, 6, 0, 7, 0, 0, 9, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 3), (2, 4), (3, 5), (2, 6), (1, 7)])
    puzzle.add_renban([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_renban([(6, 8), (6, 7), (6, 6), (6, 5)])
    puzzle.add_renban([(6, 3), (6, 2), (7, 2), (8, 2)])
    puzzle.add_renban([(3, 0), (4, 1), (5, 2), (4, 3)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(3, 8), (3, 7), (3, 6)])
    puzzle.add_renban([(1, 6), (1, 5), (2, 5)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(2, 8), (2, 7)])
    puzzle.add_renban([(7, 8), (7, 7)])
    puzzle.add_renban([(8, 6), (7, 5)])

    return puzzle
