"""PuzzleMadness Renban Sudoku — 2025-05-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 5, 0, 0, 6, 0, 2, 0],
        [0, 0, 7, 0, 5, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 4, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 3, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 6, 9, 0, 0, 0],
        [0, 9, 2, 0, 7, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(4, 4), (3, 3), (2, 2), (3, 1), (4, 0)])
    puzzle.add_renban([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(1, 7), (1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(6, 8), (5, 7), (4, 6)])
    puzzle.add_renban([(7, 3), (6, 2), (7, 1)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(8, 6), (8, 5)])
    puzzle.add_renban([(8, 7), (7, 6)])
    puzzle.add_renban([(4, 1), (5, 2)])
    puzzle.add_renban([(8, 4), (7, 4)])

    return puzzle
