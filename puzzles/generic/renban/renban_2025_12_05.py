"""PuzzleMadness Renban Sudoku — 2025-12-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 4],
        [0, 0, 0, 4, 1, 9, 0, 0, 8],
        [0, 0, 9, 3, 0, 0, 7, 0, 1],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 5, 0, 7, 2, 0, 6, 0],
        [7, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(5, 2), (4, 2), (3, 2), (3, 1), (3, 0)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (7, 7), (7, 8)])
    puzzle.add_renban([(2, 4), (2, 5), (2, 6), (1, 6)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_renban([(3, 7), (4, 7), (5, 7)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2)])
    puzzle.add_renban([(6, 0), (6, 1), (6, 2)])
    puzzle.add_renban([(1, 0), (1, 1)])
    puzzle.add_renban([(4, 0), (5, 1)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(1, 3), (2, 3)])

    return puzzle
