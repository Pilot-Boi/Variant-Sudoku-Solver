"""PuzzleMadness Renban Sudoku — 2025-11-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 6],
        [0, 5, 0, 0, 2, 0, 0, 0, 0],
        [9, 0, 0, 6, 0, 8, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 1, 0, 2, 8, 0, 0, 0, 0],
        [4, 0, 2, 0, 1, 0, 0, 6, 0],
        [0, 0, 0, 0, 7, 4, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5), (7, 5), (8, 5)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(2, 4), (3, 5), (2, 6), (1, 7)])
    puzzle.add_renban([(2, 2), (2, 1), (3, 1), (4, 1)])
    puzzle.add_renban([(0, 5), (1, 5), (2, 5)])
    puzzle.add_renban([(2, 7), (2, 8), (1, 8)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6)])
    puzzle.add_renban([(3, 7), (3, 6)])
    puzzle.add_renban([(5, 7), (4, 6)])
    puzzle.add_renban([(6, 8), (6, 7)])
    puzzle.add_renban([(6, 4), (5, 3)])
    puzzle.add_renban([(4, 8), (5, 8)])

    return puzzle
