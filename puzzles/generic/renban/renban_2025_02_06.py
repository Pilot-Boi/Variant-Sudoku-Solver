"""PuzzleMadness Renban Sudoku — 2025-02-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 2, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [1, 7, 9, 4, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 3, 0, 0, 0, 0, 8],
        [0, 2, 8, 0, 0, 0, 3, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 1), (5, 2), (5, 3), (4, 3), (3, 3)])
    puzzle.add_renban([(2, 8), (2, 7), (2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(5, 4), (5, 5), (5, 6), (5, 7)])
    puzzle.add_renban([(1, 2), (2, 3), (3, 4), (2, 5)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(7, 4), (8, 4), (8, 5)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
    puzzle.add_renban([(7, 7), (6, 7)])
    puzzle.add_renban([(3, 0), (4, 1)])
    puzzle.add_renban([(6, 4), (6, 5)])
    puzzle.add_renban([(4, 8), (3, 7)])
    puzzle.add_renban([(1, 1), (2, 2)])

    return puzzle
