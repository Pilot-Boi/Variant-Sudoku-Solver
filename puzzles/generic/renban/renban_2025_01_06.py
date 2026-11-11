"""PuzzleMadness Renban Sudoku — 2025-01-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 5, 0, 4, 0, 0],
        [1, 0, 0, 0, 3, 0, 0, 0, 7],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0, 7, 2, 5, 0],
        [0, 0, 6, 0, 7, 1, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 2), (4, 1), (5, 0), (6, 1), (7, 2)])
    puzzle.add_renban([(3, 5), (3, 4), (3, 3), (4, 3), (5, 3)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(4, 4), (5, 4), (6, 4), (7, 4)])
    puzzle.add_renban([(4, 5), (3, 6), (2, 5), (1, 4)])
    puzzle.add_renban([(0, 1), (1, 1), (2, 1), (3, 1)])
    puzzle.add_renban([(2, 2), (2, 3), (1, 3)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(4, 7), (5, 6), (6, 7)])
    puzzle.add_renban([(4, 6), (5, 5), (6, 6)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(0, 4), (1, 5)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(7, 3), (6, 3)])
    puzzle.add_renban([(0, 6), (1, 6)])

    return puzzle
