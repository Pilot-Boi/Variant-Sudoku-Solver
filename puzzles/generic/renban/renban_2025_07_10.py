"""PuzzleMadness Renban Sudoku — 2025-07-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 6, 0, 0, 0, 5, 9, 3, 0],
        [0, 3, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [2, 0, 3, 0, 0, 0, 0, 6, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 4, 0, 0, 7, 2, 0, 1, 0],
        [0, 0, 0, 0, 2, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 5, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 8), (1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(5, 1), (5, 2), (5, 3), (5, 4)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8), (6, 7)])
    puzzle.add_renban([(0, 2), (1, 3), (2, 4), (1, 5)])
    puzzle.add_renban([(3, 6), (3, 7), (2, 7)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(2, 1), (2, 2), (2, 3)])
    puzzle.add_renban([(5, 7), (5, 6), (5, 5)])
    puzzle.add_renban([(8, 1), (7, 2)])
    puzzle.add_renban([(7, 3), (6, 4)])
    puzzle.add_renban([(0, 6), (1, 6)])
    puzzle.add_renban([(4, 0), (3, 1)])
    puzzle.add_renban([(3, 3), (3, 4)])

    return puzzle
