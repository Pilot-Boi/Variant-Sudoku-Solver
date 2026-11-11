"""PuzzleMadness Renban Sudoku — 2025-06-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 9, 0, 5, 0, 0, 0, 0],
        [5, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 1, 0, 8, 0, 0],
        [0, 0, 0, 0, 6, 8, 4, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 7, 0, 6, 8],
        [0, 0, 0, 0, 0, 0, 0, 9, 3],
        [0, 3, 4, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 1, 3, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_renban([(4, 3), (5, 3), (6, 3), (6, 4), (6, 5)])
    puzzle.add_renban([(8, 5), (8, 6), (8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(5, 6), (4, 7), (3, 6), (2, 5)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2), (0, 3)])
    puzzle.add_renban([(4, 2), (3, 2), (2, 2), (2, 1)])
    puzzle.add_renban([(6, 1), (7, 1), (7, 2)])
    puzzle.add_renban([(8, 3), (8, 4), (7, 4)])
    puzzle.add_renban([(1, 7), (2, 7), (3, 7)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(4, 6), (3, 5)])
    puzzle.add_renban([(3, 0), (4, 1)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(1, 4), (2, 3)])
    puzzle.add_renban([(7, 6), (6, 6)])

    return puzzle
