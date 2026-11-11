"""PuzzleMadness Renban Sudoku — 2025-05-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 8, 0, 0, 3, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 7, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 5, 0, 0, 0, 0, 8],
        [0, 2, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 3, 5, 2, 0, 0, 6, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 6), (3, 6), (4, 6), (5, 6), (6, 6)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)])
    puzzle.add_renban([(4, 0), (3, 1), (2, 2), (1, 1), (0, 0)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(6, 1), (6, 2), (5, 2), (4, 2)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(5, 5), (4, 5), (4, 4)])
    puzzle.add_renban([(1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(3, 4), (3, 5), (2, 5)])
    puzzle.add_renban([(4, 8), (5, 7)])
    puzzle.add_renban([(2, 8), (3, 7)])
    puzzle.add_renban([(6, 0), (5, 0)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(6, 4), (5, 4)])

    return puzzle
