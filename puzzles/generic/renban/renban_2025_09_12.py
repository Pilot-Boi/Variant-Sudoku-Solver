"""PuzzleMadness Renban Sudoku — 2025-09-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 4, 7, 0, 0, 5, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 3, 9, 0, 6],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [6, 0, 0, 8, 0, 0, 0, 1, 0],
        [0, 7, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 5), (1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_renban([(3, 1), (4, 2), (5, 3), (6, 4), (7, 5)])
    puzzle.add_renban([(5, 4), (5, 5), (4, 5), (3, 5)])
    puzzle.add_renban([(3, 8), (4, 7), (5, 6), (6, 5)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(3, 4), (3, 3), (4, 3)])
    puzzle.add_renban([(5, 0), (6, 0), (6, 1)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(0, 1), (1, 1)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(8, 3), (8, 4)])

    return puzzle
