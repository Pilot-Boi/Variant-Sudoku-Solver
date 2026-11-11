"""PuzzleMadness Renban Sudoku — 2025-10-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 4, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 3, 5, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 9, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 2, 7],
        [4, 0, 2, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 5), (4, 5), (3, 5), (3, 4), (3, 3)])
    puzzle.add_renban([(4, 0), (4, 1), (4, 2), (3, 2), (2, 2)])
    puzzle.add_renban([(2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_renban([(6, 2), (6, 1), (7, 1), (8, 1)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7), (8, 8)])
    puzzle.add_renban([(5, 6), (5, 7), (5, 8), (4, 8)])
    puzzle.add_renban([(4, 4), (4, 3), (5, 3)])
    puzzle.add_renban([(7, 5), (6, 4), (7, 3)])
    puzzle.add_renban([(4, 6), (3, 7), (2, 6)])
    puzzle.add_renban([(7, 0), (6, 0), (5, 0)])
    puzzle.add_renban([(3, 8), (4, 7)])
    puzzle.add_renban([(0, 4), (1, 3)])
    puzzle.add_renban([(1, 8), (2, 8)])
    puzzle.add_renban([(8, 2), (7, 2)])
    puzzle.add_renban([(7, 7), (6, 6)])

    return puzzle
