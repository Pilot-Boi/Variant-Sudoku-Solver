"""PuzzleMadness Renban Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 6],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 2, 6, 0, 4, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 2, 3, 0],
        [0, 0, 0, 0, 1, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 8, 4, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 4],
        [0, 0, 0, 5, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (4, 2), (4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(7, 5), (7, 6), (7, 7), (6, 7), (5, 7)])
    puzzle.add_renban([(6, 3), (6, 2), (7, 2), (8, 2)])
    puzzle.add_renban([(0, 7), (0, 6), (0, 5), (1, 5)])
    puzzle.add_renban([(2, 3), (1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(4, 5), (5, 4), (6, 5)])
    puzzle.add_renban([(7, 0), (6, 0), (5, 0)])
    puzzle.add_renban([(2, 6), (3, 5), (4, 6)])
    puzzle.add_renban([(5, 8), (4, 8), (4, 7)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(3, 7), (3, 6)])
    puzzle.add_renban([(4, 4), (5, 3)])
    puzzle.add_renban([(7, 4), (6, 4)])
    puzzle.add_renban([(8, 4), (7, 3)])

    return puzzle
