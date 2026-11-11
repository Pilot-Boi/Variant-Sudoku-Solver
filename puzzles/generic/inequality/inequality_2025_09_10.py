"""PuzzleMadness Inequality Sudoku — 2025-09-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Inequality Sudoku — 2025-09-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/greaterthansudoku/hard/2025/9/10'
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
    puzzle.add_inequality((0, 1), (0, 2), '<')
    puzzle.add_inequality((0, 3), (0, 4), '<')
    puzzle.add_inequality((1, 3), (1, 4), '<')
    puzzle.add_inequality((1, 6), (1, 7), '>')
    puzzle.add_inequality((2, 0), (2, 1), '<')
    puzzle.add_inequality((2, 3), (2, 4), '<')
    puzzle.add_inequality((2, 4), (2, 5), '>')
    puzzle.add_inequality((2, 6), (2, 7), '<')
    puzzle.add_inequality((3, 0), (3, 1), '>')
    puzzle.add_inequality((3, 7), (3, 8), '<')
    puzzle.add_inequality((4, 0), (4, 1), '<')
    puzzle.add_inequality((5, 0), (5, 1), '>')
    puzzle.add_inequality((5, 3), (5, 4), '<')
    puzzle.add_inequality((5, 4), (5, 5), '>')
    puzzle.add_inequality((5, 7), (5, 8), '>')
    puzzle.add_inequality((6, 4), (6, 5), '>')
    puzzle.add_inequality((7, 0), (7, 1), '<')
    puzzle.add_inequality((7, 4), (7, 5), '>')
    puzzle.add_inequality((8, 0), (8, 1), '>')
    puzzle.add_inequality((8, 1), (8, 2), '<')
    puzzle.add_inequality((8, 3), (8, 4), '<')
    puzzle.add_inequality((8, 4), (8, 5), '<')
    puzzle.add_inequality((8, 6), (8, 7), '<')
    puzzle.add_inequality((8, 7), (8, 8), '<')
    puzzle.add_inequality((0, 1), (1, 1), '>')
    puzzle.add_inequality((0, 4), (1, 4), '>')
    puzzle.add_inequality((0, 5), (1, 5), '<')
    puzzle.add_inequality((0, 6), (1, 6), '<')
    puzzle.add_inequality((0, 8), (1, 8), '<')
    puzzle.add_inequality((1, 1), (2, 1), '>')
    puzzle.add_inequality((1, 8), (2, 8), '>')
    puzzle.add_inequality((3, 0), (4, 0), '<')
    puzzle.add_inequality((3, 2), (4, 2), '>')
    puzzle.add_inequality((3, 3), (4, 3), '<')
    puzzle.add_inequality((3, 8), (4, 8), '<')
    puzzle.add_inequality((4, 0), (5, 0), '>')
    puzzle.add_inequality((4, 2), (5, 2), '<')
    puzzle.add_inequality((4, 8), (5, 8), '<')
    puzzle.add_inequality((6, 1), (7, 1), '>')
    puzzle.add_inequality((6, 2), (7, 2), '>')
    puzzle.add_inequality((6, 3), (7, 3), '>')
    puzzle.add_inequality((6, 7), (7, 7), '<')
    puzzle.add_inequality((7, 0), (8, 0), '>')
    puzzle.add_inequality((7, 2), (8, 2), '>')
    puzzle.add_inequality((7, 4), (8, 4), '<')
    puzzle.add_inequality((7, 8), (8, 8), '>')

    return puzzle
