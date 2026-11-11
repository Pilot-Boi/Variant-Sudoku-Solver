"""PuzzleMadness Renban Sudoku — 2025-12-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 4],
        [0, 5, 0, 4, 1, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 8, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 7, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 0, 5, 7, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    puzzle.add_renban([(5, 1), (5, 2), (4, 2), (3, 2)])
    puzzle.add_renban([(2, 5), (3, 4), (4, 5), (5, 6)])
    puzzle.add_renban([(1, 5), (1, 4), (1, 3), (2, 3)])
    puzzle.add_renban([(2, 1), (3, 1), (4, 1)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(6, 3), (5, 3)])
    puzzle.add_renban([(4, 7), (5, 7)])
    puzzle.add_renban([(8, 5), (7, 5)])
    puzzle.add_renban([(8, 1), (7, 1)])

    return puzzle
