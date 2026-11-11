"""PuzzleMadness Renban Sudoku — 2025-09-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 8, 0, 0, 0, 0, 0, 0, 1],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 9, 0, 3, 0, 0, 0, 5],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 4, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 7],
        [0, 9, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 5), (6, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_renban([(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)])
    puzzle.add_renban([(5, 8), (4, 8), (3, 8), (3, 7), (3, 6)])
    puzzle.add_renban([(5, 5), (4, 4), (3, 3), (4, 2)])
    puzzle.add_renban([(1, 1), (1, 2), (1, 3), (1, 4)])
    puzzle.add_renban([(5, 1), (6, 0), (7, 1), (8, 2)])
    puzzle.add_renban([(6, 1), (6, 2), (5, 2)])
    puzzle.add_renban([(4, 6), (5, 6), (5, 7)])
    puzzle.add_renban([(0, 7), (1, 6)])
    puzzle.add_renban([(2, 2), (2, 3)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(0, 3), (0, 4)])
    puzzle.add_renban([(8, 7), (7, 6)])

    return puzzle
