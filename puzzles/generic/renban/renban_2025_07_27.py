"""PuzzleMadness Renban Sudoku — 2025-07-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [7, 6, 0, 0, 5, 0, 0, 3, 9],
        [4, 0, 0, 0, 0, 0, 1, 6, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 0, 8, 6, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [6, 0, 0, 0, 0, 9, 8, 0, 0],
        [0, 0, 4, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 6), (5, 5), (5, 4), (6, 4), (7, 4)])
    puzzle.add_renban([(3, 6), (2, 6), (1, 6), (1, 5), (1, 4)])
    puzzle.add_renban([(3, 2), (2, 2), (2, 1), (2, 0)])
    puzzle.add_renban([(3, 4), (4, 4), (4, 5), (4, 6)])
    puzzle.add_renban([(6, 8), (5, 8), (4, 8), (4, 7)])
    puzzle.add_renban([(4, 0), (5, 0), (5, 1)])
    puzzle.add_renban([(5, 3), (4, 3), (4, 2)])
    puzzle.add_renban([(3, 0), (4, 1), (5, 2)])
    puzzle.add_renban([(8, 0), (7, 1)])
    puzzle.add_renban([(1, 3), (2, 3)])
    puzzle.add_renban([(8, 1), (7, 2)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(8, 8), (7, 8)])

    return puzzle
