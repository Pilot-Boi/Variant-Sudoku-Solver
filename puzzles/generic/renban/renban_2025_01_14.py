"""PuzzleMadness Renban Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 9, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 6, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 0],
        [6, 0, 0, 7, 0, 3, 0, 9, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 5, 7, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (6, 8), (7, 8)])
    puzzle.add_renban([(6, 7), (6, 6), (6, 5), (7, 5), (8, 5)])
    puzzle.add_renban([(3, 6), (3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(0, 3), (0, 2), (0, 1), (1, 1)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (3, 0)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (2, 7)])
    puzzle.add_renban([(2, 2), (2, 3), (1, 3)])
    puzzle.add_renban([(8, 3), (7, 3), (6, 3)])
    puzzle.add_renban([(0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(0, 5), (1, 5)])
    puzzle.add_renban([(4, 5), (5, 5)])
    puzzle.add_renban([(7, 0), (7, 1)])
    puzzle.add_renban([(8, 7), (7, 6)])
    puzzle.add_renban([(8, 2), (7, 2)])

    return puzzle
