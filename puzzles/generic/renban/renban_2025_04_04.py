"""PuzzleMadness Renban Sudoku — 2025-04-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 7, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 9, 6, 0, 0],
        [0, 0, 8, 4, 0, 0, 0, 0, 5],
        [0, 0, 3, 0, 0, 0, 0, 0, 8],
        [0, 7, 0, 1, 5, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 1, 5, 0, 0],
        [4, 0, 0, 0, 6, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 6), (1, 5), (0, 4), (1, 3), (2, 2)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6), (6, 7), (7, 8)])
    puzzle.add_renban([(7, 2), (7, 3), (7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(2, 1), (3, 1), (4, 1), (4, 2)])
    puzzle.add_renban([(5, 0), (6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(3, 5), (4, 4), (5, 3)])
    puzzle.add_renban([(3, 2), (4, 3), (3, 4)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6)])
    puzzle.add_renban([(6, 8), (5, 8), (5, 7)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(2, 4), (2, 5)])
    puzzle.add_renban([(0, 2), (0, 3)])
    puzzle.add_renban([(6, 6), (5, 5)])
    puzzle.add_renban([(5, 1), (5, 2)])

    return puzzle
