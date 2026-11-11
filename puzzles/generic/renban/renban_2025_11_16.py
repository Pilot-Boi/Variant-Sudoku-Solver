"""PuzzleMadness Renban Sudoku — 2025-11-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 1],
        [0, 0, 0, 7, 2, 0, 4, 0, 0],
        [0, 6, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 1, 5],
        [0, 0, 0, 1, 0, 0, 0, 0, 8],
        [1, 0, 9, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 3, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 3), (5, 4), (5, 5), (5, 6), (5, 7)])
    puzzle.add_renban([(0, 1), (1, 1), (2, 1), (2, 2), (2, 3)])
    puzzle.add_renban([(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(1, 6), (1, 5), (2, 5), (3, 5)])
    puzzle.add_renban([(1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(0, 4), (0, 3), (1, 3)])
    puzzle.add_renban([(6, 7), (6, 6), (6, 5)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(2, 7), (2, 8), (1, 8)])
    puzzle.add_renban([(7, 6), (7, 5)])
    puzzle.add_renban([(6, 2), (6, 3)])
    puzzle.add_renban([(4, 7), (4, 6)])
    puzzle.add_renban([(6, 0), (6, 1)])
    puzzle.add_renban([(0, 2), (1, 2)])

    return puzzle
