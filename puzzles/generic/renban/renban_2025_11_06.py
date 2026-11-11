"""PuzzleMadness Renban Sudoku — 2025-11-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 8, 0],
        [1, 5, 8, 0, 9, 0, 7, 0, 0],
        [0, 0, 0, 2, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [5, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 0, 2, 0, 4, 0],
        [0, 4, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 6), (7, 7), (7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(0, 4), (1, 3), (2, 2), (3, 3), (4, 4)])
    puzzle.add_renban([(1, 2), (1, 1), (2, 1), (3, 1)])
    puzzle.add_renban([(8, 5), (7, 4), (6, 3), (5, 2)])
    puzzle.add_renban([(4, 5), (5, 5), (5, 6), (5, 7)])
    puzzle.add_renban([(3, 2), (4, 3), (5, 4)])
    puzzle.add_renban([(0, 8), (1, 7), (2, 6)])
    puzzle.add_renban([(4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(7, 5), (6, 5), (6, 4)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(0, 5), (1, 5)])

    return puzzle
