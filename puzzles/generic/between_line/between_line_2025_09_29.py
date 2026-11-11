"""PuzzleMadness Between Lines Sudoku — 2025-09-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 6],
        [0, 1, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 3, 0, 8, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [8, 0, 1, 0, 0, 7, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 1), (0, 0), (1, 0), (2, 0), (3, 1), (3, 0)])
    puzzle.add_between_line([(7, 2), (7, 1), (6, 2), (6, 1), (6, 0)])
    puzzle.add_between_line([(8, 6), (7, 5), (8, 5), (8, 4), (7, 3)])
    puzzle.add_between_line([(0, 1), (0, 2), (0, 3), (1, 4), (1, 3)])
    puzzle.add_between_line([(3, 8), (2, 7), (2, 6), (2, 5), (1, 6)])
    puzzle.add_between_line([(5, 0), (4, 1), (5, 2), (5, 3)])
    puzzle.add_between_line([(5, 7), (6, 6), (6, 5), (5, 5)])
    puzzle.add_between_line([(2, 4), (3, 5), (3, 6), (4, 7)])
    puzzle.add_between_line([(2, 8), (1, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(2, 3), (2, 2), (2, 1)])
    puzzle.add_between_line([(7, 6), (6, 7), (7, 8)])
    puzzle.add_between_line([(8, 7), (7, 7), (8, 8)])

    return puzzle
