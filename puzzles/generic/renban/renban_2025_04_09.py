"""PuzzleMadness Renban Sudoku — 2025-04-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 7, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [6, 9, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 2, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 7],
        [0, 0, 0, 9, 0, 5, 4, 0, 0],
        [0, 3, 0, 1, 4, 0, 9, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(1, 5), (2, 4), (3, 3), (4, 4), (5, 5)])
    puzzle.add_renban([(4, 3), (4, 2), (4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(2, 6), (2, 7), (2, 8), (1, 8)])
    puzzle.add_renban([(5, 2), (6, 3), (7, 4), (6, 5)])
    puzzle.add_renban([(1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(4, 6), (3, 6), (3, 5)])
    puzzle.add_renban([(2, 1), (2, 2), (2, 3)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6)])
    puzzle.add_renban([(0, 4), (1, 3)])
    puzzle.add_renban([(7, 6), (6, 6)])
    puzzle.add_renban([(6, 4), (5, 4)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(8, 7), (8, 6)])

    return puzzle
