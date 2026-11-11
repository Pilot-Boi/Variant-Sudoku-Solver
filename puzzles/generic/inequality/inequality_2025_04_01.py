"""PuzzleMadness Inequality Sudoku — 2025-04-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Inequality Sudoku — 2025-04-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/greaterthansudoku/hard/2025/4/1'
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

    puzzle.add_inequality((0, 1), (0, 2), '<')
    puzzle.add_inequality((0, 4), (0, 5), '>')
    puzzle.add_inequality((0, 6), (0, 7), '>')
    puzzle.add_inequality((1, 6), (1, 7), '<')
    puzzle.add_inequality((2, 0), (2, 1), '>')
    puzzle.add_inequality((2, 1), (2, 2), '>')
    puzzle.add_inequality((2, 3), (2, 4), '<')
    puzzle.add_inequality((3, 1), (3, 2), '>')
    puzzle.add_inequality((3, 3), (3, 4), '<')
    puzzle.add_inequality((3, 7), (3, 8), '<')
    puzzle.add_inequality((4, 3), (4, 4), '<')
    puzzle.add_inequality((4, 4), (4, 5), '>')
    puzzle.add_inequality((5, 3), (5, 4), '<')
    puzzle.add_inequality((5, 4), (5, 5), '>')
    puzzle.add_inequality((5, 6), (5, 7), '>')
    puzzle.add_inequality((6, 4), (6, 5), '>')
    puzzle.add_inequality((6, 7), (6, 8), '<')
    puzzle.add_inequality((7, 0), (7, 1), '>')
    puzzle.add_inequality((7, 7), (7, 8), '<')
    puzzle.add_inequality((8, 0), (8, 1), '>')
    puzzle.add_inequality((8, 3), (8, 4), '<')
    puzzle.add_inequality((8, 4), (8, 5), '<')
    puzzle.add_inequality((0, 1), (1, 1), '>')
    puzzle.add_inequality((0, 3), (1, 3), '<')
    puzzle.add_inequality((0, 5), (1, 5), '>')
    puzzle.add_inequality((0, 6), (1, 6), '<')
    puzzle.add_inequality((0, 8), (1, 8), '>')
    puzzle.add_inequality((1, 3), (2, 3), '<')
    puzzle.add_inequality((1, 7), (2, 7), '<')
    puzzle.add_inequality((3, 1), (4, 1), '<')
    puzzle.add_inequality((3, 5), (4, 5), '<')
    puzzle.add_inequality((3, 6), (4, 6), '<')
    puzzle.add_inequality((4, 3), (5, 3), '<')
    puzzle.add_inequality((4, 8), (5, 8), '>')
    puzzle.add_inequality((6, 1), (7, 1), '<')
    puzzle.add_inequality((6, 3), (7, 3), '<')
    puzzle.add_inequality((6, 6), (7, 6), '<')
    puzzle.add_inequality((7, 2), (8, 2), '<')
    puzzle.add_inequality((7, 5), (8, 5), '>')
    puzzle.add_inequality((7, 7), (8, 7), '>')

    return puzzle
