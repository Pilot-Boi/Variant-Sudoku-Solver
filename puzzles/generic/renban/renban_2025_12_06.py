"""PuzzleMadness Renban Sudoku — 2025-12-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 5, 0, 4, 0],
        [3, 0, 0, 6, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 5, 0, 0, 0, 0, 4],
        [0, 8, 0, 0, 9, 2, 0, 0, 7],
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 1, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 7), (3, 7), (4, 7), (5, 7), (6, 7)])
    puzzle.add_renban([(4, 3), (3, 4), (2, 5), (1, 4), (0, 3)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(6, 6), (6, 5), (6, 4), (7, 4)])
    puzzle.add_renban([(7, 5), (8, 6), (7, 7), (6, 8)])
    puzzle.add_renban([(1, 8), (1, 7), (1, 6), (1, 5)])
    puzzle.add_renban([(3, 6), (4, 5), (5, 6)])
    puzzle.add_renban([(7, 1), (6, 2), (5, 1)])
    puzzle.add_renban([(5, 0), (4, 1), (3, 2)])
    puzzle.add_renban([(1, 2), (0, 2), (0, 1)])
    puzzle.add_renban([(8, 1), (8, 2)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(6, 3), (5, 4)])
    puzzle.add_renban([(3, 5), (4, 4)])

    return puzzle
