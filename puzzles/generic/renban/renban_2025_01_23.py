"""PuzzleMadness Renban Sudoku — 2025-01-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 5, 3, 0, 0],
        [4, 0, 0, 1, 0, 0, 8, 0, 5],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 4],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 3, 0, 0, 0, 0, 7],
        [0, 8, 0, 0, 0, 0, 4, 5, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 7), (2, 7), (1, 7), (1, 6), (1, 5)])
    puzzle.add_renban([(6, 0), (6, 1), (6, 2), (5, 2), (4, 2)])
    puzzle.add_renban([(5, 6), (4, 6), (3, 6), (3, 5), (3, 4)])
    puzzle.add_renban([(7, 4), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(0, 0), (1, 1), (2, 2), (3, 3)])
    puzzle.add_renban([(4, 3), (5, 3), (6, 3), (7, 3)])
    puzzle.add_renban([(2, 1), (3, 1), (4, 1)])
    puzzle.add_renban([(2, 4), (2, 5), (2, 6)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(5, 0), (5, 1)])
    puzzle.add_renban([(4, 4), (5, 4)])
    puzzle.add_renban([(8, 8), (7, 7)])
    puzzle.add_renban([(6, 5), (5, 5)])
    puzzle.add_renban([(8, 1), (7, 2)])

    return puzzle
