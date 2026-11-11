"""PuzzleMadness Renban Sudoku — 2025-03-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 6, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 4, 0, 8, 3, 0, 0, 7, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 3, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(7, 5), (6, 4), (5, 3), (6, 2), (7, 1)])
    puzzle.add_renban([(2, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_renban([(0, 0), (1, 1), (2, 2), (1, 3)])
    puzzle.add_renban([(8, 2), (8, 3), (7, 3), (6, 3)])
    puzzle.add_renban([(4, 6), (4, 7), (3, 7)])
    puzzle.add_renban([(6, 8), (6, 7), (6, 6)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(5, 2), (4, 2), (4, 1)])
    puzzle.add_renban([(8, 8), (7, 7)])
    puzzle.add_renban([(5, 0), (5, 1)])
    puzzle.add_renban([(2, 3), (3, 4)])
    puzzle.add_renban([(5, 7), (5, 6)])
    puzzle.add_renban([(8, 4), (8, 5)])

    return puzzle
