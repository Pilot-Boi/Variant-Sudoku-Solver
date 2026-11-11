"""PuzzleMadness Renban Sudoku — 2025-03-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 4, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 8, 7, 0, 0, 0, 5, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 1, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 6, 0, 0, 4, 0, 0, 0, 0],
        [0, 3, 4, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (3, 3), (2, 2), (3, 1), (4, 0)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(0, 8), (1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(4, 6), (5, 6), (6, 6), (7, 6)])
    puzzle.add_renban([(3, 7), (2, 7), (1, 7), (1, 6)])
    puzzle.add_renban([(0, 6), (0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(7, 5), (6, 4), (5, 3)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(2, 6), (3, 5)])
    puzzle.add_renban([(1, 5), (2, 4)])
    puzzle.add_renban([(5, 0), (4, 1)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(6, 2), (6, 3)])

    return puzzle
