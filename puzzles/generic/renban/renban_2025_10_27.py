"""PuzzleMadness Renban Sudoku — 2025-10-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 5, 4, 0, 0, 3],
        [0, 0, 5, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 9, 0, 0, 0, 2, 0, 0],
        [0, 1, 0, 0, 0, 5, 3, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 9, 6],
        [0, 8, 6, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 6), (6, 7), (6, 8), (5, 8), (4, 8)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (7, 6), (7, 7)])
    puzzle.add_renban([(7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(3, 4), (2, 4), (1, 4), (1, 3)])
    puzzle.add_renban([(3, 7), (3, 6), (4, 6), (5, 6)])
    puzzle.add_renban([(2, 6), (2, 5), (3, 5)])
    puzzle.add_renban([(0, 1), (0, 2), (0, 3)])
    puzzle.add_renban([(1, 1), (2, 1), (2, 2)])
    puzzle.add_renban([(2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(8, 8), (7, 8)])
    puzzle.add_renban([(1, 2), (2, 3)])
    puzzle.add_renban([(6, 3), (5, 4)])
    puzzle.add_renban([(6, 0), (6, 1)])

    return puzzle
