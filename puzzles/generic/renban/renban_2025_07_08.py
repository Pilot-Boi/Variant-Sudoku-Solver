"""PuzzleMadness Renban Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 4, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 5, 4, 0, 0, 0, 7],
        [5, 0, 0, 8, 0, 0, 3, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 3, 0, 0, 0, 0, 6, 0, 2],
        [0, 7, 0, 9, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 3), (6, 4), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(3, 4), (3, 3), (3, 2), (4, 2), (5, 2)])
    puzzle.add_renban([(1, 4), (1, 5), (1, 6), (1, 7), (1, 8)])
    puzzle.add_renban([(4, 5), (3, 5), (2, 5), (2, 4)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4), (0, 5)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(5, 8), (4, 8), (4, 7)])
    puzzle.add_renban([(5, 7), (4, 6), (5, 5)])
    puzzle.add_renban([(8, 4), (8, 5), (7, 5)])
    puzzle.add_renban([(2, 8), (2, 7)])
    puzzle.add_renban([(4, 3), (5, 4)])
    puzzle.add_renban([(7, 0), (6, 1)])
    puzzle.add_renban([(2, 0), (2, 1)])
    puzzle.add_renban([(0, 1), (1, 1)])

    return puzzle
