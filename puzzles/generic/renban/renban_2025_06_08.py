"""PuzzleMadness Renban Sudoku — 2025-06-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 3, 8, 0, 0, 2],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 2, 6],
        [0, 0, 0, 0, 2, 0, 0, 5, 0],
        [6, 0, 4, 0, 0, 3, 0, 7, 0],
        [0, 0, 7, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4)])
    puzzle.add_renban([(6, 3), (6, 2), (6, 1), (7, 1), (8, 1)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7), (8, 8)])
    puzzle.add_renban([(0, 1), (1, 1), (2, 1), (2, 2)])
    puzzle.add_renban([(3, 4), (3, 3), (4, 3)])
    puzzle.add_renban([(7, 7), (6, 7), (6, 6)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 5)])
    puzzle.add_renban([(4, 4), (5, 3), (6, 4)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(7, 4), (6, 5)])
    puzzle.add_renban([(2, 5), (3, 5)])
    puzzle.add_renban([(3, 8), (4, 8)])
    puzzle.add_renban([(0, 8), (1, 7)])

    return puzzle
