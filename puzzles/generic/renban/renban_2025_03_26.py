"""PuzzleMadness Renban Sudoku — 2025-03-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 9, 0, 0, 0],
        [5, 0, 0, 0, 6, 2, 0, 0, 0],
        [6, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 8],
        [0, 0, 0, 0, 3, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 2, 0, 0],
        [8, 1, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 4), (5, 5), (5, 6), (5, 7), (5, 8)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)])
    puzzle.add_renban([(4, 3), (4, 4), (4, 5), (3, 5)])
    puzzle.add_renban([(7, 3), (6, 3), (6, 2), (6, 1)])
    puzzle.add_renban([(3, 6), (3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(7, 7), (6, 6), (7, 5)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(1, 4), (2, 4), (2, 5)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(7, 4), (6, 4)])
    puzzle.add_renban([(5, 0), (4, 1)])
    puzzle.add_renban([(0, 8), (0, 7)])
    puzzle.add_renban([(7, 1), (7, 2)])
    puzzle.add_renban([(5, 1), (5, 2)])

    return puzzle
