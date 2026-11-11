"""PuzzleMadness Between Lines Sudoku — 2025-06-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 9, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [2, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 9, 0, 0, 0, 8, 0, 0, 0],
        [0, 1, 7, 0, 6, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 3, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 1), (0, 0), (1, 1), (2, 2), (1, 3), (0, 2)])
    puzzle.add_between_line([(8, 2), (7, 1), (6, 2), (5, 2), (5, 1)])
    puzzle.add_between_line([(3, 6), (4, 6), (3, 5), (4, 5), (5, 4)])
    puzzle.add_between_line([(1, 6), (0, 7), (1, 8), (1, 7), (2, 7)])
    puzzle.add_between_line([(6, 3), (6, 4), (5, 3), (4, 3)])
    puzzle.add_between_line([(3, 8), (4, 8), (5, 7), (4, 7)])
    puzzle.add_between_line([(2, 5), (3, 4), (2, 4), (1, 4)])
    puzzle.add_between_line([(8, 6), (8, 7), (7, 8), (8, 8)])
    puzzle.add_between_line([(5, 0), (6, 0), (6, 1)])
    puzzle.add_between_line([(2, 3), (3, 3), (4, 2)])
    puzzle.add_between_line([(6, 7), (7, 6), (8, 5)])
    puzzle.add_between_line([(0, 3), (0, 4), (0, 5)])

    return puzzle
