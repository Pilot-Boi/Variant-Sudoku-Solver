from sudoku.constraints import (
    KillerCageConstraint,
    ThermometerConstraint,
    NotEqualConstraint,
    NonConsecutiveConstraint,
    GermanWhispersConstraint,
)

def validate_solution(puzzle, solution):
    """
    Validate a solved Sudoku grid independently of the CSP solver.

    solution: dictionary mapping (row, column) -> digit
    Returns a list of error messages.
    An empty list means the solution passed all checks.
    """
    errors = []
    expected = set(range(1, 10))

    # Check that every cell has a valid digit.
    for r in range(9):
        for c in range(9):
            value = solution.get((r, c))

            if value not in expected:
                errors.append(
                    f"Invalid value at R{r + 1}C{c + 1}: {value}"
                )

    # Check rows.
    for r in range(9):
        values = [solution.get((r, c)) for c in range(9)]

        if set(values) != expected:
            errors.append(f"Row {r + 1} is invalid")

    # Check columns.
    for c in range(9):
        values = [solution.get((r, c)) for r in range(9)]

        if set(values) != expected:
            errors.append(f"Column {c + 1} is invalid")

    # Check 3x3 boxes.
    for box_r in range(3):
        for box_c in range(3):
            cells = [
                (r, c)
                for r in range(box_r * 3, box_r * 3 + 3)
                for c in range(box_c * 3, box_c * 3 + 3)
            ]

            values = [solution.get(cell) for cell in cells]

            if set(values) != expected:
                errors.append(
                    f"Box {box_r * 3 + box_c + 1} is invalid"
                )

    # Check given digits.
    for r in range(9):
        for c in range(9):
            given = puzzle.grid[r][c]

            if given and solution.get((r, c)) != given:
                errors.append(
                    f"Given digit mismatch at R{r + 1}C{c + 1}"
                )

    # Check variant constraints.
    for constraint in puzzle.constraints:

        if isinstance(constraint, ThermometerConstraint):
            values = [
                solution.get(cell)
                for cell in constraint.variables
            ]

            if any(
                a is None or b is None or a >= b
                for a, b in zip(values, values[1:])
            ):
                errors.append(
                    f"Invalid thermometer: {constraint.variables}"
                )

        elif isinstance(constraint, KillerCageConstraint):
            values = [
                solution.get(cell)
                for cell in constraint.variables
            ]

            if (
                any(v is None for v in values)
                or sum(v for v in values if v is not None)
                    != constraint.target_sum
                or len(values) != len(set(values))
            ):
                errors.append(
                    f"Invalid Killer cage "
                    f"(target {constraint.target_sum}): "
                    f"{constraint.variables}"
                )
        
        elif isinstance(constraint, NotEqualConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            if (
                value_a is None
                or value_b is None
                or value_a == value_b
            ):
                errors.append(
                    f"Not-equal constraint violation: ..."
                    f"R{a[0] + 1}C{a[1] + 1} and "
                    f"R{b[0] + 1}C{b[1] + 1}"
                )
        elif isinstance(constraint, NonConsecutiveConstraint):
            a, b = constraint.variables

            if a in solution and b in solution:
                if abs(solution[a] - solution[b]) == 1:
                    errors.append(
                        f"Nonconsecutive violation: "
                        f"R{a[0] + 1}C{a[1] + 1} and "
                        f"R{b[0] + 1}C{b[1] + 1}"
                    )
        
    return errors