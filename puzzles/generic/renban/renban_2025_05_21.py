"""PuzzleMadness Renban Sudoku — 2025-05-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 0, 7],
        [0, 8, 3, 9, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 6, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 7, 5, 0, 1, 3],
        [3, 0, 5, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 3, 0, 5, 0],
        [0, 0, 0, 0, 9, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 8), (1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(8, 6), (7, 7), (6, 8), (5, 7), (4, 6)])
    puzzle.add_renban([(3, 1), (3, 2), (3, 3), (3, 4)])
    puzzle.add_renban([(5, 3), (4, 3), (4, 2), (4, 1)])
    puzzle.add_renban([(4, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_renban([(7, 4), (7, 5), (6, 5)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(1, 1), (2, 2), (1, 3)])
    puzzle.add_renban([(7, 2), (7, 3), (6, 3)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(0, 5), (1, 4)])
    puzzle.add_renban([(6, 7), (6, 6)])
    puzzle.add_renban([(0, 3), (0, 4)])
    puzzle.add_renban([(1, 7), (1, 6)])

    return puzzle
