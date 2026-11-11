"""PuzzleMadness Renban Sudoku — 2025-06-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 6, 0, 1, 0, 0, 4, 0, 0],
        [0, 4, 1, 0, 8, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 6, 1, 3, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 6, 9, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 0, 0, 0, 0, 7],
        [0, 0, 5, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 6), (6, 6), (5, 6), (5, 5), (5, 4)])
    puzzle.add_renban([(4, 3), (3, 3), (2, 3), (2, 2), (2, 1)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (2, 7), (2, 8)])
    puzzle.add_renban([(4, 8), (4, 7), (4, 6), (4, 5)])
    puzzle.add_renban([(1, 4), (2, 4), (3, 4), (3, 5)])
    puzzle.add_renban([(7, 3), (6, 3), (5, 3), (5, 2)])
    puzzle.add_renban([(7, 1), (6, 1), (5, 1)])
    puzzle.add_renban([(4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(0, 2), (0, 3)])
    puzzle.add_renban([(6, 8), (5, 8)])
    puzzle.add_renban([(7, 4), (7, 5)])
    puzzle.add_renban([(8, 7), (8, 6)])
    puzzle.add_renban([(0, 8), (1, 8)])

    return puzzle
