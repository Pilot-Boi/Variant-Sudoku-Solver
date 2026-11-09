from sudoku.constraints import (
    KillerCageConstraint,
    ThermometerConstraint,
    NotEqualConstraint,
    NonConsecutiveConstraint,
    GermanWhispersConstraint,
    RenbanConstraint,
    PalindromeConstraint,
    ArrowConstraint,
    KropkiConstraint,
    NegativeKropkiConstraint,
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

        elif isinstance(constraint, GermanWhispersConstraint):
            cells = constraint.variables
            minimum = constraint.MINIMUM_DIFFERENCE

            for a, b in zip(cells, cells[1:]):
                value_a = solution.get(a)
                value_b = solution.get(b)

                if (
                    value_a is None
                    or value_b is None
                    or abs(value_a - value_b) < minimum
                ):
                    errors.append(
                        f"German Whispers violation: "
                        f"R{a[0] + 1}C{a[1] + 1} and "
                        f"R{b[0] + 1}C{b[1] + 1}"
                    )

        elif isinstance(constraint, RenbanConstraint):
            cells = constraint.variables
            values = [solution.get(cell) for cell in cells]

            if any(value is None for value in values):
                errors.append(
                    f"Renban line is incomplete: {cells}"
                )

            elif len(values) != len(set(values)):
                errors.append(
                    f"Renban line repeats a digit: {cells}"
                )

            elif max(values) - min(values) != len(cells) - 1:
                errors.append(
                    f"Renban line digits are not consecutive: "
                    f"{cells}"
                )

        elif isinstance(constraint, PalindromeConstraint):
            cells = constraint.variables

            if any(
                solution.get(cell) is None
                for cell in cells
            ):
                errors.append(
                    f"Palindrome line is incomplete: {cells}"
                )

            else:
                for a, b in constraint.mirrored_pairs:
                    if solution[a] != solution[b]:
                        errors.append(
                            f"Palindrome mismatch: "
                            f"R{a[0] + 1}C{a[1] + 1} and "
                            f"R{b[0] + 1}C{b[1] + 1}"
                        )

        elif isinstance(constraint, ArrowConstraint):
            circle = constraint.circle_cells
            arrow = constraint.arrow_cells

            values = [
                solution.get(cell)
                for cell in circle + arrow
            ]

            if any(value is None for value in values):
                errors.append(
                    f"Arrow is incomplete: circle {circle}, "
                    f"shaft {arrow}"
                )

            else:
                number = 0

                for cell in circle:
                    number = number * 10 + solution[cell]

                total = sum(
                    solution[cell] for cell in arrow
                )

                if number != total:
                    circle_text = ", ".join(
                        f"R{r + 1}C{c + 1}" for r, c in circle
                    )

                    errors.append(
                        f"Arrow violation: circle "
                        f"[{circle_text}] expects {number}, "
                        f"but the shaft sums to {total}"
                    )

        elif isinstance(constraint, KropkiConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            label_a = f"R{a[0] + 1}C{a[1] + 1}"
            label_b = f"R{b[0] + 1}C{b[1] + 1}"

            if value_a is None or value_b is None:
                errors.append(
                    f"Kropki dot is incomplete: "
                    f"{label_a} and {label_b}"
                )

            elif constraint.dot_type == "white":
                if abs(value_a - value_b) != 1:
                    errors.append(
                        f"White Kropki violation: {label_a} "
                        f"and {label_b} must differ by "
                        f"exactly 1"
                    )

            else:
                if (
                    value_a != 2 * value_b
                    and value_b != 2 * value_a
                ):
                    errors.append(
                        f"Black Kropki violation: {label_a} "
                        f"and {label_b} must be in a 1:2 "
                        f"ratio"
                    )

        elif isinstance(constraint, NegativeKropkiConstraint):
            a, b = constraint.variables

            value_a = solution.get(a)
            value_b = solution.get(b)

            label_a = f"R{a[0] + 1}C{a[1] + 1}"
            label_b = f"R{b[0] + 1}C{b[1] + 1}"

            if value_a is None or value_b is None:
                errors.append(
                    f"Negative Kropki pair is incomplete: "
                    f"{label_a} and {label_b}"
                )

            elif (
                abs(value_a - value_b) == 1
                or value_a == 2 * value_b
                or value_b == 2 * value_a
            ):
                errors.append(
                    f"Negative Kropki violation: the "
                    f"undotted pair {label_a} and {label_b} "
                    f"must not be consecutive or in a 1:2 "
                    f"ratio"
                )
        
    return errors