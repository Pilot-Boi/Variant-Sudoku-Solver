"""PuzzleMadness Renban Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 2, 4, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 2, 7, 8, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 5, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [1, 5, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 5, 9, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 8, 1, 0],
        [0, 1, 0, 0, 0, 0, 5, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 5), (4, 5), (5, 5), (6, 5), (7, 5)])
    puzzle.add_renban([(3, 2), (4, 2), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(1, 7), (2, 7), (3, 7), (4, 7), (5, 7)])
    puzzle.add_renban([(1, 2), (1, 1), (2, 1), (3, 1)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(2, 3), (1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(2, 2), (3, 3), (4, 4)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0)])
    puzzle.add_renban([(2, 4), (2, 5), (1, 5)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(8, 1), (8, 2)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(4, 3), (5, 3)])

    return puzzle
