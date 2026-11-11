"""PuzzleMadness Renban Sudoku — 2025-05-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 6, 7, 0, 5],
        [0, 0, 0, 9, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [4, 8, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 3, 0, 4, 0, 5, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 8, 3, 0],
        [9, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 2), (5, 3), (5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(6, 4), (6, 5), (6, 6), (6, 7), (6, 8)])
    puzzle.add_renban([(2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_renban([(2, 1), (3, 1), (4, 1), (4, 2)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(4, 7), (4, 6), (4, 5)])
    puzzle.add_renban([(1, 6), (2, 6), (2, 7)])
    puzzle.add_renban([(3, 3), (4, 3), (4, 4)])
    puzzle.add_renban([(7, 8), (7, 7)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(5, 8), (5, 7)])
    puzzle.add_renban([(7, 4), (6, 3)])
    puzzle.add_renban([(0, 4), (1, 3)])

    return puzzle
