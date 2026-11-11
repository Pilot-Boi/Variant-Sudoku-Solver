"""PuzzleMadness Renban Sudoku — 2025-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 8, 0, 0, 0, 0, 0, 6],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 5, 6, 0, 0, 0, 4, 0, 9],
        [0, 9, 0, 5, 0, 6, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 8, 0, 1, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 8, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 6), (5, 6), (6, 6), (7, 6), (8, 6)])
    puzzle.add_renban([(2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_renban([(5, 1), (6, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(4, 0), (4, 1), (4, 2), (3, 2)])
    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (1, 2)])
    puzzle.add_renban([(2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(3, 4), (4, 3), (5, 4)])
    puzzle.add_renban([(6, 2), (6, 3), (5, 3)])
    puzzle.add_renban([(0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(3, 0), (3, 1)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(7, 8), (6, 7)])
    puzzle.add_renban([(8, 4), (7, 4)])
    puzzle.add_renban([(8, 2), (8, 3)])

    return puzzle
