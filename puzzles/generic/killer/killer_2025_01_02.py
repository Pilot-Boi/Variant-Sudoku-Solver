"""PuzzleMadness Killer Sudoku — 2025-01-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-01-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/1/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_killer_cage([(0, 0), (1, 0), (2, 0)], 17)
    puzzle.add_killer_cage([(0, 1), (0, 2), (1, 1), (1, 2)], 14)
    puzzle.add_killer_cage([(1, 3), (2, 1), (2, 2), (2, 3)], 26)
    puzzle.add_killer_cage([(0, 3), (0, 4), (0, 5)], 11)
    puzzle.add_killer_cage([(1, 4), (1, 5), (1, 6), (1, 7)], 18)
    puzzle.add_killer_cage([(0, 6), (0, 7), (0, 8)], 17)
    puzzle.add_killer_cage([(1, 8), (2, 7), (2, 8)], 18)
    puzzle.add_killer_cage([(2, 4), (2, 5), (2, 6)], 14)
    puzzle.add_killer_cage([(3, 4), (3, 5), (3, 6)], 8)
    puzzle.add_killer_cage([(3, 7), (4, 7), (5, 7)], 12)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 15)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 16)
    puzzle.add_killer_cage([(3, 1), (4, 1), (5, 1)], 18)
    puzzle.add_killer_cage([(3, 2), (3, 3)], 16)
    puzzle.add_killer_cage([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], 26)
    puzzle.add_killer_cage([(5, 5), (5, 6)], 14)
    puzzle.add_killer_cage([(5, 2), (5, 3), (5, 4)], 10)
    puzzle.add_killer_cage([(6, 0), (6, 1), (7, 0)], 10)
    puzzle.add_killer_cage([(8, 0), (8, 1), (8, 2)], 20)
    puzzle.add_killer_cage([(7, 1), (7, 2), (7, 3), (7, 4)], 30)
    puzzle.add_killer_cage([(8, 3), (8, 4), (8, 5)], 11)
    puzzle.add_killer_cage([(7, 6), (7, 7), (8, 6), (8, 7)], 19)
    puzzle.add_killer_cage([(6, 8), (7, 8), (8, 8)], 9)
    puzzle.add_killer_cage([(6, 5), (6, 6), (6, 7), (7, 5)], 25)
    puzzle.add_killer_cage([(6, 2), (6, 3), (6, 4)], 11)

    return puzzle
