"""PuzzleMadness Renban Sudoku — 2025-09-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 8, 0],
        [0, 7, 0, 2, 8, 0, 9, 0, 0],
        [0, 0, 0, 4, 0, 0, 5, 0, 0],
        [0, 9, 0, 0, 0, 2, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 1, 4, 0],
        [0, 0, 4, 0, 0, 8, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 3, 0, 2, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(2, 6), (2, 7), (2, 8), (1, 8), (0, 8)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (7, 6), (6, 6)])
    puzzle.add_renban([(6, 1), (7, 2), (8, 3), (7, 4)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(4, 4), (5, 3), (6, 4), (7, 5)])
    puzzle.add_renban([(1, 7), (0, 6), (1, 5)])
    puzzle.add_renban([(4, 5), (5, 5), (5, 6)])
    puzzle.add_renban([(3, 5), (4, 6), (3, 7)])
    puzzle.add_renban([(3, 2), (2, 2), (2, 1)])
    puzzle.add_renban([(3, 1), (4, 2)])
    puzzle.add_renban([(7, 8), (6, 7)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(6, 8), (5, 7)])
    puzzle.add_renban([(8, 1), (8, 2)])

    return puzzle
