"""PuzzleMadness Renban Sudoku — 2025-09-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 4, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 5, 7, 0, 0, 2],
        [1, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 2, 9, 0, 0, 0, 1, 0, 0],
        [0, 0, 3, 8, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 7, 0, 0, 9, 0],
        [0, 0, 0, 0, 1, 0, 5, 8, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4)])
    puzzle.add_renban([(1, 3), (1, 2), (1, 1), (2, 1), (3, 1)])
    puzzle.add_renban([(3, 3), (4, 2), (5, 1), (6, 2), (7, 3)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (7, 5)])
    puzzle.add_renban([(5, 0), (6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(6, 3), (7, 4), (6, 5)])
    puzzle.add_renban([(3, 7), (4, 7), (5, 7)])
    puzzle.add_renban([(7, 6), (6, 6), (5, 6)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(0, 6), (1, 6)])
    puzzle.add_renban([(5, 3), (5, 4)])
    puzzle.add_renban([(0, 5), (1, 4)])
    puzzle.add_renban([(2, 2), (2, 3)])

    return puzzle
