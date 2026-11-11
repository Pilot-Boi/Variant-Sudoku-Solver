"""PuzzleMadness Renban Sudoku — 2025-08-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [6, 9, 0, 0, 1, 0, 8, 3, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 2, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 6],
        [0, 2, 0, 4, 0, 0, 0, 0, 0],
        [8, 3, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(5, 0), (5, 1), (5, 2), (4, 2), (3, 2)])
    puzzle.add_renban([(0, 2), (1, 3), (2, 4), (1, 5), (0, 6)])
    puzzle.add_renban([(6, 4), (5, 4), (4, 4), (4, 3)])
    puzzle.add_renban([(6, 6), (6, 7), (6, 8), (5, 8)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (4, 1)])
    puzzle.add_renban([(0, 1), (1, 2), (2, 3)])
    puzzle.add_renban([(8, 1), (7, 1), (6, 1)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 7)])
    puzzle.add_renban([(4, 7), (4, 8), (3, 8)])
    puzzle.add_renban([(7, 8), (7, 7)])
    puzzle.add_renban([(6, 3), (5, 3)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(8, 7), (8, 6)])
    puzzle.add_renban([(8, 2), (8, 3)])

    return puzzle
