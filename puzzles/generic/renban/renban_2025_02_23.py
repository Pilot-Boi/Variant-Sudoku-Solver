"""PuzzleMadness Renban Sudoku — 2025-02-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [8, 0, 0, 0, 5, 0, 9, 0, 0],
        [5, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 3, 4, 0, 0, 0, 9, 0],
        [0, 0, 0, 7, 0, 0, 6, 0, 2],
        [0, 0, 0, 0, 0, 3, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 4), (1, 3), (1, 2), (2, 2), (3, 2)])
    puzzle.add_renban([(4, 7), (5, 6), (6, 5), (7, 4), (8, 3)])
    puzzle.add_renban([(4, 4), (4, 5), (4, 6), (3, 6), (2, 6)])
    puzzle.add_renban([(4, 1), (5, 0), (6, 1), (7, 2)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (3, 1)])
    puzzle.add_renban([(8, 6), (7, 6), (6, 6)])
    puzzle.add_renban([(1, 7), (2, 7), (3, 7)])
    puzzle.add_renban([(2, 3), (3, 3), (3, 4)])
    puzzle.add_renban([(0, 6), (1, 5)])
    puzzle.add_renban([(7, 8), (7, 7)])
    puzzle.add_renban([(8, 4), (8, 5)])
    puzzle.add_renban([(8, 2), (7, 3)])
    puzzle.add_renban([(6, 2), (6, 3)])

    return puzzle
