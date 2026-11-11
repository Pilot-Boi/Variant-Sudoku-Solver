"""PuzzleMadness Renban Sudoku — 2025-09-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 1, 8, 5, 0, 0, 0],
        [0, 8, 7, 0, 9, 3, 6, 2, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 1, 0, 0, 0, 6],
        [7, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 2, 0, 6, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 2), (6, 3), (6, 4), (6, 5), (6, 6)])
    puzzle.add_renban([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])
    puzzle.add_renban([(2, 7), (1, 6), (0, 5), (1, 4), (2, 3)])
    puzzle.add_renban([(2, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(3, 2), (3, 3), (3, 4), (2, 4)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (7, 6)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(2, 2), (1, 2), (1, 1)])
    puzzle.add_renban([(5, 7), (4, 8), (3, 7)])
    puzzle.add_renban([(2, 6), (3, 6)])
    puzzle.add_renban([(5, 4), (5, 5)])
    puzzle.add_renban([(8, 3), (7, 3)])
    puzzle.add_renban([(6, 8), (6, 7)])
    puzzle.add_renban([(0, 7), (1, 7)])

    return puzzle
