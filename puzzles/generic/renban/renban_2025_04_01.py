"""PuzzleMadness Renban Sudoku — 2025-04-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 9, 7, 0],
        [0, 0, 0, 0, 0, 2, 0, 8, 0],
        [4, 2, 0, 1, 0, 0, 0, 0, 5],
        [0, 5, 3, 7, 0, 0, 1, 0, 0],
        [0, 0, 0, 3, 2, 0, 6, 0, 1],
        [1, 0, 0, 0, 9, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(2, 2), (3, 1), (4, 0), (5, 1), (6, 2)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 5), (6, 6), (7, 7)])
    puzzle.add_renban([(2, 5), (1, 5), (1, 4), (1, 3)])
    puzzle.add_renban([(5, 3), (5, 4), (4, 4), (3, 4)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (6, 5)])
    puzzle.add_renban([(4, 1), (5, 2), (4, 3)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
    puzzle.add_renban([(2, 7), (2, 8), (1, 8)])
    puzzle.add_renban([(3, 6), (3, 5), (4, 5)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(2, 0), (2, 1)])
    puzzle.add_renban([(6, 3), (6, 4)])
    puzzle.add_renban([(4, 8), (4, 7)])
    puzzle.add_renban([(6, 8), (5, 7)])

    return puzzle
