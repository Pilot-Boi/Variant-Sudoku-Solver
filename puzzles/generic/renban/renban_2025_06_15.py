"""PuzzleMadness Renban Sudoku — 2025-06-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 3],
        [0, 1, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 8],
        [9, 0, 1, 0, 0, 0, 0, 0, 4],
        [0, 4, 0, 0, 8, 9, 5, 6, 0],
        [0, 6, 0, 1, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [2, 7, 9, 0, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 3), (2, 4), (2, 5), (2, 6), (2, 7)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(5, 7), (4, 6), (3, 5), (4, 4), (5, 3)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0), (5, 0)])
    puzzle.add_renban([(5, 1), (4, 2), (3, 3), (2, 2)])
    puzzle.add_renban([(6, 7), (6, 8), (5, 8), (4, 8)])
    puzzle.add_renban([(5, 4), (5, 5), (4, 5)])
    puzzle.add_renban([(6, 1), (6, 2), (5, 2)])
    puzzle.add_renban([(3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(7, 7), (6, 6), (7, 5)])
    puzzle.add_renban([(1, 1), (1, 2)])
    puzzle.add_renban([(7, 4), (6, 3)])
    puzzle.add_renban([(0, 3), (1, 3)])
    puzzle.add_renban([(8, 8), (7, 8)])
    puzzle.add_renban([(0, 6), (0, 5)])

    return puzzle
