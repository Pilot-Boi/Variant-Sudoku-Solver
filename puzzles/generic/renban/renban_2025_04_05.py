"""PuzzleMadness Renban Sudoku — 2025-04-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 9],
        [0, 5, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 5, 1, 0],
        [0, 0, 7, 9, 0, 2, 0, 8, 0],
        [0, 0, 3, 6, 5, 0, 0, 4, 0],
        [0, 0, 9, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 8, 0, 0, 0, 0, 0, 7, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 3), (6, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_renban([(3, 2), (3, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(0, 8), (1, 7), (2, 6), (3, 7), (4, 8)])
    puzzle.add_renban([(6, 8), (5, 8), (5, 7), (5, 6)])
    puzzle.add_renban([(3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5)])
    puzzle.add_renban([(4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(1, 2), (2, 3), (1, 4)])
    puzzle.add_renban([(2, 4), (3, 3)])
    puzzle.add_renban([(8, 1), (7, 1)])
    puzzle.add_renban([(1, 6), (2, 5)])
    puzzle.add_renban([(7, 7), (6, 6)])
    puzzle.add_renban([(6, 5), (5, 5)])

    return puzzle
