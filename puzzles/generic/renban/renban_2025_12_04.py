"""PuzzleMadness Renban Sudoku — 2025-12-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 1, 0, 2, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 3, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 5, 0, 9, 0],
        [0, 0, 0, 0, 4, 8, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (4, 4), (4, 5), (3, 5), (2, 5)])
    puzzle.add_renban([(1, 6), (1, 5), (1, 4), (2, 4), (3, 4)])
    puzzle.add_renban([(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 5), (6, 6)])
    puzzle.add_renban([(3, 2), (3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(7, 6), (6, 5), (7, 4)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(6, 3), (6, 2), (7, 2)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(2, 0), (2, 1)])
    puzzle.add_renban([(1, 0), (1, 1)])
    puzzle.add_renban([(0, 8), (0, 7)])
    puzzle.add_renban([(0, 6), (0, 5)])
    puzzle.add_renban([(8, 5), (7, 5)])

    return puzzle
