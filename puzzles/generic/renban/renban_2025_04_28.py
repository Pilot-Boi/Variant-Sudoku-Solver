"""PuzzleMadness Renban Sudoku — 2025-04-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 6, 0, 1, 5],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 8, 0, 3, 0, 0, 0, 0],
        [0, 3, 0, 9, 0, 0, 4, 5, 2],
        [0, 0, 0, 0, 0, 0, 3, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 2, 1, 0, 0, 0, 4, 0],
        [3, 7, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 6), (3, 6), (2, 6), (2, 5), (2, 4)])
    puzzle.add_renban([(6, 2), (5, 2), (4, 2), (4, 1), (4, 0)])
    puzzle.add_renban([(1, 5), (1, 4), (1, 3), (2, 3), (3, 3)])
    puzzle.add_renban([(6, 4), (6, 5), (5, 5), (4, 5)])
    puzzle.add_renban([(3, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_renban([(3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(6, 1), (7, 2), (6, 3)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(2, 2), (1, 2), (1, 1)])
    puzzle.add_renban([(7, 1), (8, 1), (8, 2)])
    puzzle.add_renban([(6, 0), (5, 1)])
    puzzle.add_renban([(6, 8), (5, 7)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(8, 4), (7, 5)])

    return puzzle
