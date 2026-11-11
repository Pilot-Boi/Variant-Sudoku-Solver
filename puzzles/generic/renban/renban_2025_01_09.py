"""PuzzleMadness Renban Sudoku — 2025-01-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 7, 0],
        [9, 0, 0, 0, 2, 7, 4, 0, 6],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 5, 0, 0, 0, 1],
        [0, 5, 0, 0, 0, 8, 0, 0, 4],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 8, 0, 0, 5, 0, 0, 3],
        [0, 7, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 2, 8, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 6), (5, 6), (6, 6), (7, 6), (8, 6)])
    puzzle.add_renban([(8, 3), (7, 4), (6, 5), (5, 4), (4, 3)])
    puzzle.add_renban([(5, 0), (6, 0), (7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(4, 4), (3, 4), (3, 3), (3, 2)])
    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5)])
    puzzle.add_renban([(2, 7), (1, 6), (0, 5), (1, 4)])
    puzzle.add_renban([(6, 3), (5, 2), (6, 1)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(0, 1), (0, 2), (0, 3)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(2, 1), (3, 1)])
    puzzle.add_renban([(4, 7), (3, 6)])
    puzzle.add_renban([(4, 1), (4, 2)])
    puzzle.add_renban([(1, 1), (2, 2)])
    puzzle.add_renban([(5, 8), (5, 7)])

    return puzzle
