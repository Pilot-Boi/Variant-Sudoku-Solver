"""PuzzleMadness Renban Sudoku — 2025-08-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 4],
        [0, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 4, 0, 0, 0, 7],
        [2, 9, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 9, 8, 0],
        [0, 6, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 5), (5, 6), (5, 7), (4, 7), (3, 7)])
    puzzle.add_renban([(2, 3), (1, 3), (0, 3), (0, 2), (0, 1)])
    puzzle.add_renban([(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4), (5, 4)])
    puzzle.add_renban([(7, 7), (6, 7), (6, 6), (6, 5)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(4, 8), (5, 8), (6, 8)])
    puzzle.add_renban([(7, 4), (8, 4), (8, 5)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(3, 3), (3, 4), (2, 4)])
    puzzle.add_renban([(7, 2), (7, 3)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(2, 7), (3, 6)])
    puzzle.add_renban([(7, 0), (6, 1)])
    puzzle.add_renban([(6, 0), (5, 0)])

    return puzzle
