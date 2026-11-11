"""PuzzleMadness Between Lines Sudoku — 2025-12-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 1, 9],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 6, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 5), (6, 4), (5, 5), (4, 6), (5, 7), (5, 8)])
    puzzle.add_between_line([(6, 1), (5, 2), (6, 2), (5, 3), (4, 2)])
    puzzle.add_between_line([(4, 0), (5, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_between_line([(1, 7), (1, 8), (2, 7), (1, 6), (0, 7)])
    puzzle.add_between_line([(3, 5), (3, 4), (4, 3), (4, 4), (5, 4)])
    puzzle.add_between_line([(7, 6), (7, 7), (7, 8), (6, 8)])
    puzzle.add_between_line([(3, 1), (3, 0), (2, 1), (1, 1)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4), (2, 4)])
    puzzle.add_between_line([(8, 3), (8, 4), (8, 5), (7, 4)])
    puzzle.add_between_line([(1, 0), (0, 0), (0, 1)])
    puzzle.add_between_line([(6, 6), (7, 5), (8, 6)])
    puzzle.add_between_line([(7, 3), (7, 2), (8, 1)])

    return puzzle
