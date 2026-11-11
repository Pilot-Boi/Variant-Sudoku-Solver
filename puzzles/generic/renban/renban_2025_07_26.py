"""PuzzleMadness Renban Sudoku — 2025-07-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 4, 0],
        [0, 7, 0, 0, 0, 5, 0, 0, 0],
        [0, 4, 5, 0, 0, 8, 0, 0, 0],
        [3, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 1, 0, 6],
        [0, 0, 0, 0, 2, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (5, 3), (6, 2), (7, 1), (8, 0)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_renban([(6, 5), (7, 5), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(4, 6), (5, 5), (6, 4), (7, 3)])
    puzzle.add_renban([(1, 2), (2, 3), (1, 4), (0, 5)])
    puzzle.add_renban([(2, 6), (2, 5), (2, 4), (3, 4)])
    puzzle.add_renban([(5, 6), (5, 7), (4, 7)])
    puzzle.add_renban([(0, 1), (0, 2), (0, 3)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6)])
    puzzle.add_renban([(5, 2), (4, 3)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(0, 6), (1, 6)])
    puzzle.add_renban([(0, 8), (0, 7)])
    puzzle.add_renban([(8, 1), (7, 2)])

    return puzzle
