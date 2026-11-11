"""PuzzleMadness Renban Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 5, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 7],
        [4, 0, 6, 7, 3, 0, 5, 0, 8],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [8, 0, 0, 4, 5, 0, 0, 0, 3],
        [5, 0, 0, 0, 0, 9, 0, 0, 6],
        [0, 9, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 6), (4, 6), (5, 6), (5, 7), (5, 8)])
    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4), (5, 4), (4, 4)])
    puzzle.add_renban([(3, 7), (2, 7), (1, 7), (1, 6)])
    puzzle.add_renban([(2, 6), (1, 5), (2, 4), (3, 3)])
    puzzle.add_renban([(5, 0), (4, 1), (3, 2), (2, 1)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(5, 1), (5, 2), (5, 3)])
    puzzle.add_renban([(1, 1), (2, 0), (3, 1)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(4, 2), (4, 3)])
    puzzle.add_renban([(1, 3), (1, 4)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(1, 2), (2, 2)])

    return puzzle
