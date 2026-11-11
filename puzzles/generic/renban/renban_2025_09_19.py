"""PuzzleMadness Renban Sudoku — 2025-09-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 7, 0, 0, 0, 0],
        [7, 0, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [1, 0, 4, 0, 5, 0, 0, 0, 2],
        [6, 0, 0, 9, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 5, 2, 3, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 7), (1, 7), (2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(3, 1), (3, 2), (3, 3), (3, 4), (3, 5)])
    puzzle.add_renban([(8, 8), (7, 7), (6, 6), (7, 5), (8, 4)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3)])
    puzzle.add_renban([(2, 6), (1, 6), (1, 5), (1, 4)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3), (6, 3)])
    puzzle.add_renban([(3, 6), (4, 6), (5, 6)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(5, 5), (4, 5), (4, 4)])
    puzzle.add_renban([(4, 2), (5, 3), (6, 4)])
    puzzle.add_renban([(3, 8), (4, 8)])
    puzzle.add_renban([(4, 1), (5, 2)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(8, 6), (7, 6)])
    puzzle.add_renban([(2, 4), (2, 5)])

    return puzzle
