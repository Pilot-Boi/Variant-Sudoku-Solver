"""PuzzleMadness Inequality Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Inequality Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/greaterthansudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_inequality((0, 0), (0, 1), '<')
    puzzle.add_inequality((0, 3), (0, 4), '>')
    puzzle.add_inequality((0, 6), (0, 7), '<')
    puzzle.add_inequality((0, 7), (0, 8), '<')
    puzzle.add_inequality((1, 4), (1, 5), '<')
    puzzle.add_inequality((2, 0), (2, 1), '<')
    puzzle.add_inequality((2, 6), (2, 7), '>')
    puzzle.add_inequality((3, 0), (3, 1), '>')
    puzzle.add_inequality((3, 1), (3, 2), '>')
    puzzle.add_inequality((3, 4), (3, 5), '>')
    puzzle.add_inequality((3, 6), (3, 7), '>')
    puzzle.add_inequality((4, 0), (4, 1), '>')
    puzzle.add_inequality((4, 3), (4, 4), '<')
    puzzle.add_inequality((4, 6), (4, 7), '>')
    puzzle.add_inequality((5, 1), (5, 2), '<')
    puzzle.add_inequality((5, 4), (5, 5), '>')
    puzzle.add_inequality((5, 6), (5, 7), '<')
    puzzle.add_inequality((6, 1), (6, 2), '>')
    puzzle.add_inequality((6, 3), (6, 4), '>')
    puzzle.add_inequality((7, 1), (7, 2), '<')
    puzzle.add_inequality((7, 3), (7, 4), '<')
    puzzle.add_inequality((7, 4), (7, 5), '>')
    puzzle.add_inequality((8, 3), (8, 4), '<')
    puzzle.add_inequality((8, 4), (8, 5), '>')
    puzzle.add_inequality((0, 0), (1, 0), '>')
    puzzle.add_inequality((0, 1), (1, 1), '<')
    puzzle.add_inequality((0, 2), (1, 2), '>')
    puzzle.add_inequality((0, 3), (1, 3), '<')
    puzzle.add_inequality((0, 4), (1, 4), '<')
    puzzle.add_inequality((0, 5), (1, 5), '>')
    puzzle.add_inequality((0, 8), (1, 8), '<')
    puzzle.add_inequality((1, 3), (2, 3), '<')
    puzzle.add_inequality((1, 7), (2, 7), '<')
    puzzle.add_inequality((1, 8), (2, 8), '<')
    puzzle.add_inequality((3, 0), (4, 0), '>')
    puzzle.add_inequality((3, 2), (4, 2), '<')
    puzzle.add_inequality((3, 5), (4, 5), '>')
    puzzle.add_inequality((4, 2), (5, 2), '<')
    puzzle.add_inequality((4, 3), (5, 3), '>')
    puzzle.add_inequality((4, 4), (5, 4), '<')
    puzzle.add_inequality((4, 5), (5, 5), '<')
    puzzle.add_inequality((4, 7), (5, 7), '>')
    puzzle.add_inequality((6, 0), (7, 0), '<')
    puzzle.add_inequality((6, 2), (7, 2), '>')
    puzzle.add_inequality((6, 3), (7, 3), '<')
    puzzle.add_inequality((6, 5), (7, 5), '<')
    puzzle.add_inequality((6, 7), (7, 7), '<')
    puzzle.add_inequality((7, 7), (8, 7), '>')

    return puzzle
