"""PuzzleMadness Renban Sudoku — 2025-04-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 1, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 9, 2, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 5, 0, 7, 0, 0],
        [3, 2, 0, 0, 0, 0, 0, 6, 0],
        [0, 4, 0, 1, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 4), (1, 3), (2, 2), (3, 3), (4, 4)])
    puzzle.add_renban([(6, 4), (6, 5), (6, 6), (5, 6), (4, 6)])
    puzzle.add_renban([(3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(3, 4), (4, 5), (3, 6), (2, 7)])
    puzzle.add_renban([(0, 2), (1, 1), (2, 0), (3, 1)])
    puzzle.add_renban([(5, 2), (6, 2), (7, 2), (7, 3)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(0, 5), (1, 4), (2, 3)])
    puzzle.add_renban([(2, 4), (2, 5)])
    puzzle.add_renban([(0, 7), (1, 7)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(8, 4), (7, 4)])
    puzzle.add_renban([(5, 4), (5, 5)])

    return puzzle
