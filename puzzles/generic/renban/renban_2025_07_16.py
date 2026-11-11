"""PuzzleMadness Renban Sudoku — 2025-07-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 9, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 4],
        [2, 4, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 9, 0, 0, 3, 0, 0, 0, 0],
        [1, 5, 0, 0, 9, 0, 0, 7, 0],
        [0, 0, 0, 7, 0, 2, 5, 0, 0],
        [0, 0, 9, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 0), (5, 1), (6, 2), (5, 3), (4, 4)])
    puzzle.add_renban([(4, 7), (5, 7), (6, 7), (7, 7), (8, 7)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(3, 5), (3, 4), (3, 3), (4, 3)])
    puzzle.add_renban([(8, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(2, 6), (1, 6), (1, 5)])
    puzzle.add_renban([(7, 4), (6, 3), (7, 2)])
    puzzle.add_renban([(1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(4, 8), (3, 7)])
    puzzle.add_renban([(3, 1), (4, 2)])
    puzzle.add_renban([(1, 7), (2, 7)])
    puzzle.add_renban([(6, 6), (5, 6)])

    return puzzle
