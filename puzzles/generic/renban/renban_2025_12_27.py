"""PuzzleMadness Renban Sudoku — 2025-12-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 5, 0, 2, 0],
        [0, 0, 0, 0, 6, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 0, 8, 0, 0],
        [8, 0, 0, 0, 7, 2, 0, 0, 5],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [7, 9, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 8, 0, 0, 0, 0],
        [0, 2, 0, 9, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(4, 5), (5, 4), (6, 3), (7, 4), (8, 5)])
    puzzle.add_renban([(5, 6), (4, 7), (3, 8), (2, 7), (1, 6)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(6, 0), (6, 1), (6, 2), (5, 2)])
    puzzle.add_renban([(1, 2), (1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(4, 3), (4, 4), (3, 4)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(6, 8), (6, 7), (6, 6)])
    puzzle.add_renban([(3, 2), (3, 3)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(8, 0), (8, 1)])

    return puzzle
