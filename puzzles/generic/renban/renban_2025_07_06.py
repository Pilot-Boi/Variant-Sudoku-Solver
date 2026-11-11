"""PuzzleMadness Renban Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 9, 5, 0, 4],
        [0, 0, 0, 2, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 9, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 0, 3, 7],
        [0, 0, 8, 0, 0, 2, 6, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 3), (3, 3), (4, 3), (5, 3), (6, 3)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(0, 8), (1, 7), (2, 6), (3, 7), (4, 8)])
    puzzle.add_renban([(7, 5), (6, 6), (5, 7), (4, 6)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(5, 2), (4, 2), (3, 2), (3, 1)])
    puzzle.add_renban([(4, 4), (3, 5), (2, 4)])
    puzzle.add_renban([(2, 5), (1, 5), (1, 4)])
    puzzle.add_renban([(2, 8), (2, 7)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(4, 0), (5, 1)])
    puzzle.add_renban([(0, 3), (1, 3)])
    puzzle.add_renban([(0, 4), (0, 5)])

    return puzzle
