"""PuzzleMadness Renban Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 7, 6, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 9],
        [7, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 5, 4],
        [9, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 6, 0, 0, 8, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (6, 2), (5, 2)])
    puzzle.add_renban([(2, 2), (3, 2), (4, 2), (4, 3), (4, 4)])
    puzzle.add_renban([(3, 7), (3, 6), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(1, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_renban([(5, 6), (4, 7), (3, 8), (2, 7)])
    puzzle.add_renban([(0, 4), (1, 4), (2, 4), (2, 5)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(8, 3), (7, 3), (6, 3)])
    puzzle.add_renban([(6, 6), (6, 5), (7, 5)])
    puzzle.add_renban([(4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(0, 1), (0, 2)])
    puzzle.add_renban([(3, 0), (3, 1)])
    puzzle.add_renban([(4, 8), (5, 7)])
    puzzle.add_renban([(1, 3), (2, 3)])
    puzzle.add_renban([(3, 3), (3, 4)])

    return puzzle
