"""PuzzleMadness Renban Sudoku — 2025-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 6, 0, 3, 0],
        [8, 4, 0, 1, 0, 3, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 1, 0],
        [2, 6, 0, 4, 0, 0, 0, 0, 1],
        [1, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(8, 2), (8, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])
    puzzle.add_renban([(3, 2), (2, 2), (1, 2), (1, 1), (1, 0)])
    puzzle.add_renban([(3, 0), (4, 1), (5, 2), (6, 3)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(5, 5), (4, 4), (3, 3), (4, 2)])
    puzzle.add_renban([(6, 6), (5, 7), (4, 6)])
    puzzle.add_renban([(5, 1), (6, 1), (6, 2)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8)])
    puzzle.add_renban([(4, 7), (3, 7), (3, 6)])
    puzzle.add_renban([(2, 3), (3, 4)])
    puzzle.add_renban([(1, 4), (2, 4)])
    puzzle.add_renban([(1, 7), (1, 6)])
    puzzle.add_renban([(2, 0), (3, 1)])
    puzzle.add_renban([(0, 1), (0, 2)])

    return puzzle
