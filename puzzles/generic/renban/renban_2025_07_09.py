"""PuzzleMadness Renban Sudoku — 2025-07-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 2, 3, 0, 0, 6, 0, 0, 8],
        [0, 0, 0, 3, 9, 0, 0, 4, 0],
        [6, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 5, 4, 0, 0],
        [0, 6, 2, 0, 0, 4, 9, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 9, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (2, 7), (2, 8)])
    puzzle.add_renban([(5, 2), (5, 3), (5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(1, 5), (1, 4), (1, 3), (2, 3)])
    puzzle.add_renban([(3, 4), (4, 4), (4, 5), (4, 6)])
    puzzle.add_renban([(8, 1), (7, 1), (6, 1)])
    puzzle.add_renban([(4, 7), (4, 8), (3, 8)])
    puzzle.add_renban([(5, 1), (5, 0), (6, 0)])
    puzzle.add_renban([(7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(7, 6), (6, 5)])
    puzzle.add_renban([(3, 0), (4, 0)])
    puzzle.add_renban([(7, 5), (6, 4)])
    puzzle.add_renban([(3, 6), (3, 5)])

    return puzzle
