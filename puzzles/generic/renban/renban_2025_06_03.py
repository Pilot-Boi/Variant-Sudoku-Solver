"""PuzzleMadness Renban Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 8, 0, 1, 0, 0, 0, 7],
        [0, 7, 3, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [0, 6, 0, 0, 0, 5, 0, 9, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 1, 8, 0, 0, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(5, 4), (6, 4), (7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(3, 3), (2, 4), (1, 3), (0, 2)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(1, 2), (1, 1), (2, 1)])
    puzzle.add_renban([(5, 8), (5, 7), (5, 6)])
    puzzle.add_renban([(3, 8), (2, 8), (2, 7)])
    puzzle.add_renban([(6, 3), (5, 2), (6, 1)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(4, 8), (3, 7)])
    puzzle.add_renban([(0, 4), (0, 5)])

    return puzzle
