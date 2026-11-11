"""PuzzleMadness Renban Sudoku — 2025-01-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 3, 8, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0],
        [9, 0, 0, 0, 0, 2, 0, 1, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 7, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [6, 0, 0, 3, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 1), (1, 2), (2, 3), (1, 4), (0, 5)])
    puzzle.add_renban([(6, 6), (7, 6), (8, 6), (8, 7), (8, 8)])
    puzzle.add_renban([(3, 2), (4, 1), (5, 0), (6, 1), (7, 2)])
    puzzle.add_renban([(3, 5), (2, 4), (3, 3), (4, 2)])
    puzzle.add_renban([(4, 6), (3, 6), (2, 6), (2, 5)])
    puzzle.add_renban([(8, 3), (7, 3), (6, 3)])
    puzzle.add_renban([(7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(5, 7), (5, 8), (4, 8)])
    puzzle.add_renban([(1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(7, 4), (6, 5)])
    puzzle.add_renban([(8, 1), (8, 2)])
    puzzle.add_renban([(5, 1), (5, 2)])
    puzzle.add_renban([(3, 4), (4, 4)])
    puzzle.add_renban([(6, 4), (5, 5)])

    return puzzle
