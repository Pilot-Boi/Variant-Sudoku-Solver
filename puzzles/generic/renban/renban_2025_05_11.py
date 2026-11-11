"""PuzzleMadness Renban Sudoku — 2025-05-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
        [4, 6, 0, 9, 0, 0, 2, 0, 0],
        [0, 1, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 2, 0, 0, 1, 0, 0, 0, 6],
        [0, 0, 8, 0, 0, 2, 9, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 9],
        [0, 0, 6, 5, 0, 0, 7, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 3), (5, 4), (5, 5), (4, 5), (3, 5)])
    puzzle.add_renban([(2, 8), (3, 8), (4, 8), (5, 8), (6, 8)])
    puzzle.add_renban([(6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    puzzle.add_renban([(7, 5), (7, 6), (7, 7), (6, 7)])
    puzzle.add_renban([(2, 1), (3, 1), (4, 1), (4, 2)])
    puzzle.add_renban([(8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(1, 2), (2, 2), (3, 2)])
    puzzle.add_renban([(3, 4), (3, 3), (4, 3)])
    puzzle.add_renban([(0, 7), (0, 6), (1, 6)])
    puzzle.add_renban([(7, 1), (7, 2)])
    puzzle.add_renban([(7, 3), (7, 4)])
    puzzle.add_renban([(1, 7), (2, 6)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(1, 4), (2, 4)])

    return puzzle
