"""PuzzleMadness Between Lines Sudoku — 2025-06-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 8, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 3, 0, 0, 0, 6, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 2), (8, 3), (8, 4), (8, 5), (7, 6), (6, 7)])
    puzzle.add_between_line([(0, 4), (0, 5), (1, 5), (0, 6), (1, 7)])
    puzzle.add_between_line([(0, 0), (1, 1), (0, 2), (1, 2), (2, 2)])
    puzzle.add_between_line([(1, 4), (2, 4), (3, 3), (4, 2), (4, 1)])
    puzzle.add_between_line([(4, 3), (5, 4), (4, 4), (3, 4), (3, 5)])
    puzzle.add_between_line([(5, 1), (6, 1), (7, 0), (8, 0)])
    puzzle.add_between_line([(7, 4), (6, 5), (6, 4), (7, 3)])
    puzzle.add_between_line([(5, 7), (5, 6), (4, 7), (5, 8)])
    puzzle.add_between_line([(8, 7), (8, 6), (7, 7), (7, 8)])
    puzzle.add_between_line([(1, 6), (2, 7), (1, 8)])
    puzzle.add_between_line([(5, 3), (6, 3), (6, 2)])
    puzzle.add_between_line([(3, 6), (3, 7), (3, 8)])
    puzzle.add_between_line([(2, 1), (3, 0), (4, 0)])

    return puzzle
