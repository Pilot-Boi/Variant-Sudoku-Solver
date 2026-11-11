"""PuzzleMadness Renban Sudoku — 2025-06-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 9, 3, 0, 0, 0, 7],
        [0, 2, 6, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 4],
        [1, 0, 4, 3, 0, 9, 0, 7, 0],
        [0, 7, 0, 0, 5, 0, 2, 0, 3],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 1), (5, 2), (5, 3), (4, 3), (3, 3)])
    puzzle.add_renban([(5, 5), (5, 6), (5, 7), (4, 7), (3, 7)])
    puzzle.add_renban([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)])
    puzzle.add_renban([(0, 6), (0, 5), (1, 5), (2, 5)])
    puzzle.add_renban([(6, 7), (6, 8), (5, 8), (4, 8)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(8, 7), (7, 6), (6, 5)])
    puzzle.add_renban([(1, 1), (2, 1), (3, 1)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(0, 0), (1, 0)])
    puzzle.add_renban([(3, 6), (3, 5)])
    puzzle.add_renban([(8, 6), (8, 5)])
    puzzle.add_renban([(4, 0), (5, 0)])
    puzzle.add_renban([(0, 7), (1, 7)])

    return puzzle
