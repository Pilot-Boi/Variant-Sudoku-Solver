"""PuzzleMadness Renban Sudoku — 2025-03-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9],
        [0, 8, 0, 0, 0, 0, 6, 0, 0],
        [0, 9, 3, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 5, 0, 0, 0, 0, 6],
        [0, 2, 0, 3, 0, 5, 0, 0, 0],
        [0, 0, 0, 9, 2, 0, 5, 0, 0],
        [0, 0, 0, 0, 6, 0, 4, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 6), (5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_renban([(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)])
    puzzle.add_renban([(0, 3), (0, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_renban([(2, 6), (1, 5), (2, 4), (3, 3)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(7, 6), (7, 7), (6, 7)])
    puzzle.add_renban([(2, 2), (2, 3), (1, 3)])
    puzzle.add_renban([(3, 6), (4, 6), (4, 7)])
    puzzle.add_renban([(6, 2), (6, 1), (7, 1)])
    puzzle.add_renban([(3, 4), (4, 5)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(3, 2), (4, 3)])
    puzzle.add_renban([(2, 7), (3, 7)])
    puzzle.add_renban([(8, 3), (7, 4)])

    return puzzle
