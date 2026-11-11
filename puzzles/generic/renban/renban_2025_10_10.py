"""PuzzleMadness Renban Sudoku — 2025-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 9, 8, 5, 2, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 3],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [3, 4, 0, 0, 0, 8, 6, 9, 0],
        [0, 0, 3, 0, 0, 9, 0, 6, 0],
        [0, 0, 0, 0, 0, 2, 7, 0, 0],
        [0, 0, 7, 3, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 6), (6, 7), (5, 8), (4, 7), (3, 6)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)])
    puzzle.add_renban([(5, 3), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(4, 1), (4, 2), (4, 3), (4, 4)])
    puzzle.add_renban([(1, 2), (1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(5, 1), (5, 0), (6, 0)])
    puzzle.add_renban([(5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(1, 7), (0, 7), (0, 6)])
    puzzle.add_renban([(3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(7, 0), (7, 1)])
    puzzle.add_renban([(2, 3), (2, 4)])
    puzzle.add_renban([(7, 3), (6, 3)])

    return puzzle
