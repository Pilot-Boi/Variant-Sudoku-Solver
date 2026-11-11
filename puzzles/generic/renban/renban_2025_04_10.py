"""PuzzleMadness Renban Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 3, 0, 0],
        [0, 0, 6, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 2, 0, 0, 0, 0, 3],
        [0, 0, 0, 7, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 4, 8, 9, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [2, 0, 3, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (2, 7), (2, 8)])
    puzzle.add_renban([(8, 5), (7, 5), (6, 5), (6, 4), (6, 3)])
    puzzle.add_renban([(5, 6), (5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_renban([(7, 2), (6, 2), (6, 1), (6, 0)])
    puzzle.add_renban([(1, 5), (1, 4), (1, 3), (2, 3)])
    puzzle.add_renban([(3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(6, 7), (6, 6), (7, 6)])
    puzzle.add_renban([(3, 1), (4, 1), (4, 2)])
    puzzle.add_renban([(4, 7), (3, 6), (2, 5)])
    puzzle.add_renban([(1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(1, 0), (2, 0)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(3, 0), (4, 0)])
    puzzle.add_renban([(5, 0), (5, 1)])

    return puzzle
