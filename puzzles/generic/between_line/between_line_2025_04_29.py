"""PuzzleMadness Between Lines Sudoku — 2025-04-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 9, 5, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 2, 0, 0],
        [3, 0, 0, 7, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 4, 0, 0, 7, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 7), (3, 8), (2, 8), (2, 7), (1, 7), (0, 7)])
    puzzle.add_between_line([(0, 2), (1, 1), (1, 0), (2, 1), (3, 1)])
    puzzle.add_between_line([(4, 7), (5, 7), (6, 8), (6, 7), (7, 6)])
    puzzle.add_between_line([(8, 1), (8, 2), (7, 1), (6, 0), (5, 1)])
    puzzle.add_between_line([(5, 0), (4, 1), (5, 2), (4, 3), (3, 4)])
    puzzle.add_between_line([(0, 5), (1, 4), (0, 4), (1, 3)])
    puzzle.add_between_line([(8, 3), (7, 4), (8, 5), (8, 4)])
    puzzle.add_between_line([(5, 4), (5, 5), (4, 5), (5, 6)])
    puzzle.add_between_line([(5, 3), (6, 4), (6, 5)])
    puzzle.add_between_line([(3, 5), (2, 6), (3, 6)])
    puzzle.add_between_line([(7, 8), (7, 7), (8, 7)])
    puzzle.add_between_line([(2, 3), (3, 2), (4, 2)])

    return puzzle
