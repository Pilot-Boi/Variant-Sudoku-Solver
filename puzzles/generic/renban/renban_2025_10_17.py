"""PuzzleMadness Renban Sudoku — 2025-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 5, 0, 6, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 5, 9],
        [5, 0, 0, 0, 0, 0, 0, 3, 1],
        [3, 0, 0, 0, 0, 0, 0, 4, 0],
        [4, 0, 6, 2, 0, 9, 0, 0, 5],
        [2, 0, 0, 0, 0, 8, 0, 0, 6],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 7), (3, 7), (4, 7), (5, 7), (6, 7)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])
    puzzle.add_renban([(5, 4), (5, 5), (5, 6), (4, 6), (3, 6)])
    puzzle.add_renban([(5, 2), (6, 2), (7, 2), (7, 3)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_renban([(1, 3), (1, 2), (2, 2), (3, 2)])
    puzzle.add_renban([(7, 4), (6, 4), (6, 3)])
    puzzle.add_renban([(7, 1), (6, 1), (5, 1)])
    puzzle.add_renban([(2, 3), (3, 3), (4, 3)])
    puzzle.add_renban([(3, 5), (2, 6), (1, 5)])
    puzzle.add_renban([(3, 1), (4, 1)])
    puzzle.add_renban([(0, 7), (1, 7)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(8, 3), (8, 4)])

    return puzzle
