"""PuzzleMadness Renban Sudoku — 2025-03-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 8, 2, 0, 0, 0],
        [7, 5, 0, 4, 0, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [1, 8, 0, 0, 0, 0, 0, 4, 0],
        [4, 0, 0, 9, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 5, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 9, 8, 0, 0, 3, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)])
    puzzle.add_renban([(6, 3), (7, 4), (8, 5), (7, 6)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(4, 7), (4, 6), (5, 6), (6, 6)])
    puzzle.add_renban([(2, 1), (2, 0), (3, 0)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6)])
    puzzle.add_renban([(0, 8), (1, 8), (2, 8)])
    puzzle.add_renban([(0, 7), (1, 7), (2, 7)])
    puzzle.add_renban([(6, 1), (5, 1)])
    puzzle.add_renban([(1, 5), (2, 5)])
    puzzle.add_renban([(1, 4), (2, 4)])
    puzzle.add_renban([(4, 1), (3, 2)])
    puzzle.add_renban([(7, 5), (6, 5)])

    return puzzle
