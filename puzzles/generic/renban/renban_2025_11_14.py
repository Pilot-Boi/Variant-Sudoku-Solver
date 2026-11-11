"""PuzzleMadness Renban Sudoku — 2025-11-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 3, 7, 0, 6, 0, 0, 0],
        [2, 4, 0, 3, 1, 0, 0, 8, 5],
        [0, 0, 0, 0, 5, 0, 3, 6, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 9, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (5, 2), (5, 3)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4), (6, 5), (6, 6)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5), (1, 5), (2, 5)])
    puzzle.add_renban([(3, 3), (4, 3), (4, 4), (4, 5)])
    puzzle.add_renban([(7, 3), (8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(4, 6), (5, 6), (5, 7)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(2, 6), (3, 6), (3, 7)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(1, 3), (2, 4)])
    puzzle.add_renban([(1, 1), (2, 1)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(3, 0), (4, 0)])

    return puzzle
