"""PuzzleMadness Renban Sudoku — 2025-06-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 2, 3, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 7, 0, 0, 8, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 2, 1],
        [0, 8, 0, 4, 0, 0, 9, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 8, 4, 0, 0],
        [0, 6, 3, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 2), (5, 2), (6, 2), (6, 3), (6, 4)])
    puzzle.add_renban([(4, 4), (3, 4), (2, 4), (2, 3), (2, 2)])
    puzzle.add_renban([(3, 6), (4, 6), (5, 6), (5, 7), (5, 8)])
    puzzle.add_renban([(5, 0), (4, 1), (3, 2), (2, 1)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2), (1, 3)])
    puzzle.add_renban([(1, 4), (1, 5), (1, 6), (1, 7)])
    puzzle.add_renban([(4, 7), (4, 8), (3, 8)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(2, 7), (2, 8), (1, 8)])
    puzzle.add_renban([(5, 5), (6, 5), (6, 6)])
    puzzle.add_renban([(3, 3), (4, 3)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(7, 4), (7, 5)])
    puzzle.add_renban([(7, 8), (6, 7)])
    puzzle.add_renban([(8, 8), (7, 7)])

    return puzzle
