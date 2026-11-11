"""PuzzleMadness Renban Sudoku — 2025-05-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 4, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [9, 7, 0, 5, 1, 0, 3, 0, 0],
        [0, 0, 6, 0, 0, 0, 8, 0, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 8],
        [0, 0, 2, 7, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 2), (4, 2), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(3, 5), (3, 4), (3, 3), (4, 3), (5, 3)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(1, 6), (1, 5), (1, 4), (2, 4)])
    puzzle.add_renban([(0, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_renban([(1, 8), (2, 7), (3, 6), (4, 7)])
    puzzle.add_renban([(5, 4), (5, 5), (4, 5)])
    puzzle.add_renban([(7, 4), (6, 4), (6, 3)])
    puzzle.add_renban([(8, 8), (7, 7)])
    puzzle.add_renban([(0, 6), (0, 5)])
    puzzle.add_renban([(2, 6), (2, 5)])
    puzzle.add_renban([(0, 8), (0, 7)])
    puzzle.add_renban([(5, 8), (5, 7)])

    return puzzle
