"""PuzzleMadness Renban Sudoku — 2025-05-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 1, 9, 5, 8, 0, 0, 0],
        [0, 0, 0, 0, 3, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 6, 2, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 5, 0, 0, 7, 0, 8, 0, 0],
        [1, 0, 0, 8, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 5), (3, 4), (3, 3), (4, 3), (5, 3)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (8, 7), (8, 8)])
    puzzle.add_renban([(0, 3), (1, 4), (2, 5), (1, 6), (0, 7)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (7, 2)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0), (5, 1)])
    puzzle.add_renban([(6, 4), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(4, 5), (4, 4), (5, 4)])
    puzzle.add_renban([(3, 2), (4, 1), (5, 2)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(4, 7), (5, 6)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(2, 1), (3, 1)])
    puzzle.add_renban([(7, 4), (7, 5)])
    puzzle.add_renban([(1, 8), (2, 7)])

    return puzzle
