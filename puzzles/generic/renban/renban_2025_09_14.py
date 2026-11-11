"""PuzzleMadness Renban Sudoku — 2025-09-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 8, 0, 0, 0, 0, 4, 1, 0],
        [1, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 9],
        [0, 0, 1, 0, 0, 0, 0, 0, 7],
        [0, 3, 0, 0, 7, 0, 8, 6, 0],
        [0, 0, 0, 0, 4, 0, 7, 0, 3],
        [0, 7, 0, 8, 9, 0, 0, 4, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 4), (5, 5), (5, 6), (5, 7), (5, 8)])
    puzzle.add_renban([(3, 3), (3, 4), (3, 5), (3, 6), (3, 7)])
    puzzle.add_renban([(0, 1), (1, 2), (2, 3), (1, 4), (0, 5)])
    puzzle.add_renban([(7, 6), (7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(3, 0), (3, 1), (3, 2), (2, 2)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(7, 0), (6, 1), (5, 2)])
    puzzle.add_renban([(8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(4, 3), (4, 4)])
    puzzle.add_renban([(7, 5), (6, 5)])
    puzzle.add_renban([(0, 2), (0, 3)])
    puzzle.add_renban([(2, 7), (2, 6)])
    puzzle.add_renban([(1, 0), (1, 1)])

    return puzzle
