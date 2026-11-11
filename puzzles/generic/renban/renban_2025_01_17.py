"""PuzzleMadness Renban Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 9],
        [5, 0, 0, 0, 4, 8, 6, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 1, 0, 2, 5, 0, 0, 0, 0],
        [4, 0, 0, 0, 9, 3, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 4],
        [2, 0, 1, 0, 0, 0, 7, 5, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 6), (2, 6), (3, 6), (3, 7), (3, 8)])
    puzzle.add_renban([(4, 8), (5, 8), (6, 8), (7, 8), (8, 8)])
    puzzle.add_renban([(4, 1), (4, 2), (4, 3), (4, 4), (4, 5)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4), (0, 5)])
    puzzle.add_renban([(8, 4), (7, 3), (6, 2), (5, 1)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(1, 3), (2, 4), (1, 5)])
    puzzle.add_renban([(8, 7), (8, 6), (8, 5)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(0, 7), (0, 6)])
    puzzle.add_renban([(4, 7), (4, 6)])
    puzzle.add_renban([(6, 6), (5, 5)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(3, 3), (3, 4)])

    return puzzle
