"""PuzzleMadness Killer Sudoku — 2025-05-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-05-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/5/25'
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

    puzzle.add_killer_cage([(0, 0), (1, 0), (2, 0)], 15)
    puzzle.add_killer_cage([(0, 1), (0, 2), (0, 3)], 13)
    puzzle.add_killer_cage([(1, 1), (1, 2), (1, 3)], 12)
    puzzle.add_killer_cage([(2, 1), (3, 1), (4, 1)], 17)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 18)
    puzzle.add_killer_cage([(5, 1), (6, 0), (6, 1)], 18)
    puzzle.add_killer_cage([(7, 0), (7, 1), (7, 2)], 16)
    puzzle.add_killer_cage([(8, 0), (8, 1), (8, 2)], 9)
    puzzle.add_killer_cage([(0, 4), (1, 4), (2, 4), (3, 4)], 28)
    puzzle.add_killer_cage([(0, 5), (0, 6), (0, 7)], 12)
    puzzle.add_killer_cage([(0, 8), (1, 8), (2, 8)], 11)
    puzzle.add_killer_cage([(1, 5), (1, 6), (1, 7)], 18)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 5)], 16)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7)], 16)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 19)
    puzzle.add_killer_cage([(5, 7), (6, 7), (6, 8)], 13)
    puzzle.add_killer_cage([(7, 6), (7, 7), (7, 8)], 16)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 21)
    puzzle.add_killer_cage([(7, 5), (8, 5)], 9)
    puzzle.add_killer_cage([(4, 5), (5, 5), (6, 5), (6, 6)], 17)
    puzzle.add_killer_cage([(3, 6), (4, 6), (5, 6)], 12)
    puzzle.add_killer_cage([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)], 17)
    puzzle.add_killer_cage([(4, 3), (5, 3), (6, 2), (6, 3)], 22)
    puzzle.add_killer_cage([(7, 3), (8, 3)], 9)
    puzzle.add_killer_cage([(2, 2), (2, 3), (3, 3)], 20)
    puzzle.add_killer_cage([(3, 2), (4, 2), (5, 2)], 11)

    return puzzle
