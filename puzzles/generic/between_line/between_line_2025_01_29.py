"""PuzzleMadness Between Lines Sudoku — 2025-01-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 1, 5, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [6, 4, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 6), (4, 6), (3, 5), (3, 4), (2, 4), (1, 4)])
    puzzle.add_between_line([(3, 3), (4, 2), (5, 3), (6, 4), (6, 3)])
    puzzle.add_between_line([(2, 5), (3, 6), (2, 7), (1, 7), (0, 8)])
    puzzle.add_between_line([(0, 6), (0, 5), (0, 4), (0, 3), (0, 2)])
    puzzle.add_between_line([(8, 8), (7, 7), (7, 6), (6, 7)])
    puzzle.add_between_line([(6, 0), (7, 0), (8, 1), (8, 2)])
    puzzle.add_between_line([(1, 2), (2, 3), (3, 2), (4, 1)])
    puzzle.add_between_line([(5, 5), (4, 5), (4, 4), (4, 3)])
    puzzle.add_between_line([(5, 2), (5, 1), (4, 0)])
    puzzle.add_between_line([(3, 8), (4, 8), (4, 7)])
    puzzle.add_between_line([(6, 1), (7, 2), (7, 1)])
    puzzle.add_between_line([(5, 7), (6, 8), (7, 8)])

    return puzzle
