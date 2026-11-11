"""PuzzleMadness Renban Sudoku — 2025-05-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [2, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 6, 0, 9, 0, 0, 4, 0],
        [5, 0, 0, 4, 3, 8, 0, 0, 0],
        [0, 0, 0, 0, 4, 6, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 2],
        [0, 0, 0, 0, 5, 0, 4, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7)])
    puzzle.add_renban([(1, 2), (2, 1), (3, 2), (4, 3)])
    puzzle.add_renban([(7, 6), (7, 7), (6, 7)])
    puzzle.add_renban([(5, 4), (4, 5), (3, 4)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1)])
    puzzle.add_renban([(1, 7), (1, 6), (1, 5)])
    puzzle.add_renban([(8, 1), (8, 2)])
    puzzle.add_renban([(4, 6), (3, 5)])
    puzzle.add_renban([(1, 0), (1, 1)])
    puzzle.add_renban([(2, 8), (3, 7)])
    puzzle.add_renban([(0, 0), (0, 1)])

    return puzzle
