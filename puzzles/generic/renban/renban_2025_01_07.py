"""PuzzleMadness Renban Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 4, 5, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 7, 0, 0, 0, 0, 9, 0],
        [4, 0, 0, 0, 9, 0, 1, 0, 0],
        [0, 6, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 1), (6, 2), (6, 3), (5, 3), (4, 3)])
    puzzle.add_renban([(0, 2), (1, 2), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(4, 7), (5, 6), (6, 5), (7, 4), (8, 3)])
    puzzle.add_renban([(4, 6), (3, 6), (3, 5), (3, 4)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(1, 5), (2, 5), (2, 6), (2, 7)])
    puzzle.add_renban([(5, 5), (4, 5), (4, 4)])
    puzzle.add_renban([(6, 7), (6, 8), (5, 8)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(4, 2), (4, 1), (5, 1)])
    puzzle.add_renban([(4, 0), (3, 1)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(7, 2), (7, 3)])
    puzzle.add_renban([(0, 3), (1, 4)])
    puzzle.add_renban([(1, 0), (2, 1)])

    return puzzle
