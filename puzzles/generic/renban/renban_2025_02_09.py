"""PuzzleMadness Renban Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 7, 0, 0, 0, 0, 0],
        [2, 0, 6, 0, 0, 3, 0, 0, 9],
        [3, 0, 0, 0, 0, 6, 5, 0, 0],
        [0, 2, 1, 0, 8, 0, 0, 0, 0],
        [7, 0, 0, 6, 0, 9, 0, 0, 1],
        [6, 0, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 0, 9, 0, 2, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)])
    puzzle.add_renban([(4, 4), (4, 3), (4, 2), (5, 2), (6, 2)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7), (6, 6), (6, 5)])
    puzzle.add_renban([(2, 3), (1, 2), (2, 1), (3, 0)])
    puzzle.add_renban([(3, 3), (3, 2), (3, 1), (4, 1)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(4, 7), (4, 8), (3, 8)])
    puzzle.add_renban([(4, 5), (3, 5), (3, 4)])
    puzzle.add_renban([(5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(0, 6), (0, 5), (1, 5)])
    puzzle.add_renban([(8, 6), (7, 5)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(0, 0), (1, 0)])

    return puzzle
