"""PuzzleMadness Renban Sudoku — 2025-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 2, 7, 0, 0, 0, 0, 5],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 5, 0, 0, 2, 0, 0],
        [0, 0, 5, 0, 4, 8, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 3), (4, 3), (5, 3), (6, 3), (7, 3)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_renban([(2, 1), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(5, 6), (5, 5), (5, 4), (6, 4)])
    puzzle.add_renban([(1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(1, 6), (2, 6), (2, 7)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(5, 8), (4, 7), (3, 6)])
    puzzle.add_renban([(3, 4), (4, 4), (4, 5)])
    puzzle.add_renban([(3, 8), (3, 7)])
    puzzle.add_renban([(8, 4), (7, 5)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(7, 8), (6, 7)])
    puzzle.add_renban([(7, 6), (6, 6)])

    return puzzle
