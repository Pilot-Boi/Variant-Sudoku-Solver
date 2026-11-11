"""PuzzleMadness Renban Sudoku — 2025-01-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 3, 0, 0, 1, 0, 0, 2],
        [0, 0, 0, 0, 0, 9, 3, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 8, 2, 9, 6, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 1, 0, 0, 5, 0, 9],
        [3, 1, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(2, 4), (1, 4), (0, 4), (0, 3), (0, 2)])
    puzzle.add_renban([(2, 2), (2, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7), (8, 8)])
    puzzle.add_renban([(1, 7), (2, 6), (3, 7), (4, 8)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(7, 2), (6, 2), (5, 2)])
    puzzle.add_renban([(8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(7, 8), (6, 7)])
    puzzle.add_renban([(2, 8), (3, 8)])
    puzzle.add_renban([(3, 3), (4, 3)])
    puzzle.add_renban([(2, 3), (3, 4)])
    puzzle.add_renban([(4, 4), (5, 4)])

    return puzzle
