"""PuzzleMadness Renban Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 2, 1, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 5],
        [0, 0, 0, 0, 4, 5, 0, 0, 0],
        [5, 7, 0, 0, 9, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 6, 0, 3, 0, 0, 7, 0, 0],
        [0, 1, 0, 6, 0, 0, 0, 4, 0],
        [0, 0, 9, 0, 7, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 4), (5, 5), (5, 6), (5, 7), (5, 8)])
    puzzle.add_renban([(0, 2), (1, 2), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(7, 2), (7, 3), (7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4)])
    puzzle.add_renban([(1, 4), (2, 5), (3, 6)])
    puzzle.add_renban([(1, 7), (1, 6), (1, 5)])
    puzzle.add_renban([(0, 4), (1, 3)])
    puzzle.add_renban([(4, 6), (4, 5)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(6, 0), (5, 1)])
    puzzle.add_renban([(3, 4), (3, 5)])

    return puzzle
