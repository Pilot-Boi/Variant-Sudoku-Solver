"""PuzzleMadness Renban Sudoku — 2025-09-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 5, 0, 8],
        [4, 0, 0, 0, 0, 0, 0, 2, 1],
        [0, 3, 6, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 1, 0],
        [2, 6, 0, 0, 5, 0, 0, 9, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)])
    puzzle.add_renban([(6, 4), (7, 5), (8, 6), (7, 7), (6, 8)])
    puzzle.add_renban([(3, 7), (2, 7), (1, 7), (1, 6)])
    puzzle.add_renban([(1, 3), (1, 2), (2, 2), (3, 2)])
    puzzle.add_renban([(4, 6), (4, 7), (4, 8), (3, 8)])
    puzzle.add_renban([(8, 1), (7, 1), (6, 1)])
    puzzle.add_renban([(1, 4), (2, 4), (3, 4)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(3, 3), (4, 4), (3, 5)])
    puzzle.add_renban([(0, 4), (0, 5)])
    puzzle.add_renban([(6, 6), (6, 5)])
    puzzle.add_renban([(4, 3), (5, 4)])
    puzzle.add_renban([(0, 7), (0, 6)])
    puzzle.add_renban([(8, 0), (7, 0)])

    return puzzle
