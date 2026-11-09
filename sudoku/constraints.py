from csp.constraint import Constraint
from itertools import combinations, product
from functools import lru_cache

class AllDifferentConstraint(Constraint):
    
    def __init__(
        self,
        variables,
        required_values=None,
        max_subset_size=4
    ):
        super().__init__(variables)

        if required_values is not None:
            required_values = set(required_values)

            if len(required_values) != len(self.variables):
                raise ValueError(
                    "Required values must match variable count."
                )

        if not isinstance(max_subset_size, int) or max_subset_size < 1:
            raise ValueError(
                "max_subset_size must be a positive integer"
            )

        self.required_values = required_values
        self.max_subset_size = max_subset_size

    def is_satisfied(self, assignment):
        values = [
            assignment[var]
            for var in self.variables
            if var in assignment
        ]

        if len(values) != len(set(values)):
            return False

        if self.required_values is not None:
            return all(
                value in self.required_values
                for value in values
            )

        return True
    
    def _propagate_naked_subsets(self, domains):
        """
        Detect naked subsets up to max_subset_size.

        Optimizations:
        - Filter candidates by domain size.
        - Stop building unions that exceed subset size.
        - Apply all eliminations from a discovered subset.
        - Restart after changes to avoid stale combinations.
        """
        max_size = min(
            self.max_subset_size,
            len(self.variables) - 1
        )

        changed = False

        while True:
            found_change = False

            for size in range(2, max_size + 1):

                candidates = [
                    var
                    for var in self.variables
                    if 1 < len(domains[var]) <= size
                ]

                if len(candidates) < size:
                    continue

                for group in combinations(candidates, size):
                    union = set()

                    for var in group:
                        union.update(domains[var])

                        if len(union) > size:
                            break

                    if len(union) != size:
                        continue

                    group_set = set(group)

                    # Calculate reductions before applying them.
                    reductions = {}

                    for var in self.variables:
                        if var in group_set:
                            continue

                        reduced = domains[var] - union

                        if not reduced:
                            raise ValueError(
                                "Naked subset caused contradiction"
                            )

                        if reduced != domains[var]:
                            reductions[var] = reduced

                    if reductions:
                        domains.update(reductions)

                        changed = True
                        found_change = True

                        # Restart using the updated domains.
                        break

                if found_change:
                    break

            if not found_change:
                return changed

    def propagate(self, domains):
        changed = False

        # Step 1: Enforce required values, if provided.
        if self.required_values is not None:
            for var in self.variables:
                allowed = domains[var] & self.required_values

                if not allowed:
                    raise ValueError("No valid candidates")

                if allowed != domains[var]:
                    domains[var] = allowed
                    changed = True

        # Step 2: Naked singles.
        singletons = [
            next(iter(domains[var]))
            for var in self.variables
            if len(domains[var]) == 1
        ]

        if len(singletons) != len(set(singletons)):
            raise ValueError("AllDifferent contradiction")

        forced_values = set(singletons)

        for var in self.variables:
            if len(domains[var]) == 1:
                continue

            allowed = domains[var] - forced_values

            if not allowed:
                raise ValueError("Empty domain")

            if allowed != domains[var]:
                domains[var] = allowed
                changed = True

        # Step 3: Hidden singles.
        if self.required_values is not None:
            for value in self.required_values:
                possible_cells = [
                    var for var in self.variables
                    if value in domains[var]
                ]

                if not possible_cells:
                    raise ValueError(
                        f"Required value {value} has no location"
                    )

                if len(possible_cells) == 1:
                    var = possible_cells[0]

                    if domains[var] != {value}:
                        domains[var] = {value}
                        changed = True


        # Step 4: Naked subsets.
        if self._propagate_naked_subsets(domains):
            changed = True

        return changed
        
class ThermometerConstraint(Constraint):
    def is_satisfied(self, assignment):
        n = len(self.variables)

        if n > 9:
            return False

        for i, cell in enumerate(self.variables):
            if cell not in assignment:
                continue

            value = assignment[cell]

            min_value = i + 1
            max_value = 9 - (n - 1 - i)

            if not min_value <= value <= max_value:
                return False

            for j in range(i):
                previous = self.variables[j]

                if previous in assignment:
                    if value - assignment[previous] < i - j:
                        return False

        return True

    def propagate(self, domains):
        changed = False
        cells = self.variables
        n = len(cells)

        if n > 9:
            raise ValueError("Thermometer too long")

        # First enforce positional bounds.
        for i, cell in enumerate(cells):
            minimum = i + 1
            maximum = 9 - (n - 1 - i)

            allowed = {
                value for value in domains[cell]
                if minimum <= value <= maximum
            }

            if not allowed:
                raise ValueError("Thermometer contradiction")

            if allowed != domains[cell]:
                domains[cell] = allowed
                changed = True

        # Forward pass: each value must have a
        # smaller supporting value in the prior cell.
        for i in range(1, n):
            previous = cells[i - 1]
            current = cells[i]

            smallest_previous = min(domains[previous])

            allowed = {
                value for value in domains[current]
                if value > smallest_previous
            }

            if not allowed:
                raise ValueError("Thermometer contradiction")

            if allowed != domains[current]:
                domains[current] = allowed
                changed = True

        # Backward pass: each value must have a
        # larger supporting value in the next cell.
        for i in range(n - 2, -1, -1):
            current = cells[i]
            following = cells[i + 1]

            largest_following = max(domains[following])

            allowed = {
                value for value in domains[current]
                if value < largest_following
            }

            if not allowed:
                raise ValueError("Thermometer contradiction")

            if allowed != domains[current]:
                domains[current] = allowed
                changed = True

        return changed

class KillerCageConstraint(Constraint):
    """
    Killer Sudoku cage with cached sum combinations
    and domain-aware propagation.
    """

    @staticmethod
    @lru_cache(maxsize=None)
    def _valid_combinations(size, target_sum):
        """
        Generate all unordered sets of distinct digits
        that satisfy the cage sum.

        Cached across all cages of the same size and sum.
        """
        return tuple(
            combo
            for combo in combinations(range(1, 10), size)
            if sum(combo) == target_sum
        )

    def __init__(self, variables, target_sum):
        super().__init__(variables)

        if not variables:
            raise ValueError("A cage cannot be empty")

        if len(set(variables)) != len(variables):
            raise ValueError("Duplicate cells in cage")

        if not isinstance(target_sum, int):
            raise ValueError("Target sum must be an integer")

        if len(variables) > 9:
            raise ValueError(
                "Killer cages cannot contain more than 9 cells"
            )

        n = len(variables)

        minimum = sum(range(1, n + 1))
        maximum = sum(range(10 - n, 10))

        if not minimum <= target_sum <= maximum:
            raise ValueError(
                "Target sum is impossible for cage size"
            )

        self.target_sum = target_sum
        
        self.full_digit_cage = (
            len(self.variables) == 9
            and target_sum == 45
        )

        self.full_digit_constraint = (
            AllDifferentConstraint(
                self.variables,
                required_values=set(range(1, 10))
            )
            if self.full_digit_cage
            else None
        )

        # Precomputed combinations for this cage.
        self.combinations = self._valid_combinations(
            n, target_sum
        )

        # Cache domain-specific propagation results.
        self._support_cache = {}

    def is_satisfied(self, assignment):
        assigned = [
            assignment[var]
            for var in self.variables
            if var in assignment
        ]

        if len(assigned) != len(set(assigned)):
            return False

        if any(value not in range(1, 10) for value in assigned):
            return False

        if sum(assigned) > self.target_sum:
            return False

        if len(assigned) == len(self.variables):
            return sum(assigned) == self.target_sum

        return True

    def _find_supports(self, domains):
        """
        Find every value that participates in at least
        one valid assignment of this cage.
        """
        supports = {
            var: set()
            for var in self.variables
        }
        
        targets = {
            var: set(domains[var])
            for var in self.variables
        }

        def fully_supported():
            return all(
                supports[var] == targets[var]
                for var in self.variables
            )

        # Examine only combinations compatible with
        # the current domains.
        for combo in self.combinations:
            digits = set(combo)

            # Every cell must be able to use at least
            # one digit from this combination.
            if any(
                not (domains[var] & digits)
                for var in self.variables
            ):
                continue

            # Every digit in the combination must
            # have at least one possible location.
            if any(
                not any(
                    digit in domains[var]
                    for var in self.variables
                )
                for digit in combo
            ):
                continue

            def assign(index, remaining, chosen):
                if fully_supported():
                    return

                if index == len(self.variables):
                    for var, value in chosen.items():
                        supports[var].add(value)
                    return

                var = self.variables[index]

                for value in domains[var] & remaining:
                    chosen[var] = value

                    assign(
                        index + 1,
                        remaining - {value},
                        chosen
                    )

                    del chosen[var]

                    if fully_supported():
                        return

            assign(0, digits, {})
            
            if fully_supported():
                break

        return supports

    def propagate(self, domains):
        """
        Eliminate values that cannot participate in
        any valid cage assignment.
        """
        if self.full_digit_cage:
            return self.full_digit_constraint.propagate(domains)
       
        key = tuple(
            frozenset(domains[var])
            for var in self.variables
        )

        if key in self._support_cache:
            cached = self._support_cache[key]

            if cached is None:
                raise ValueError(
                    "Killer cage has no valid assignments"
                )

            supports = {
                var: set(values)
                for var, values in zip(self.variables, cached)
            }

        else:
            supports = self._find_supports(domains)

            if any(
                not supports[var]
                for var in self.variables
            ):
                self._support_cache[key] = None
                raise ValueError(
                    "Killer cage has no valid assignments"
                )

            self._support_cache[key] = tuple(
                frozenset(supports[var])
                for var in self.variables
            )

        changed = False

        for var in self.variables:
            allowed = domains[var] & supports[var]

            if not allowed:
                raise ValueError(
                    "Killer cage has no valid assignments"
                )

            if allowed != domains[var]:
                domains[var] = allowed
                changed = True

        return changed
    
class NotEqualConstraint(Constraint):
    """
    Binary inequality constraint: A != B.

    Used by Anti-Knight and potentially Anti-King Sudoku.
    """

    def __init__(self, cell_a, cell_b):
        super().__init__((cell_a, cell_b))

        if cell_a == cell_b:
            raise ValueError(
                "NotEqualConstraint requires two distinct cells"
            )

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return assignment[a] != assignment[b]

    def propagate(self, domains):
        a, b = self.variables

        domain_a = domains[a]
        domain_b = domains[b]

        if not domain_a or not domain_b:
            raise ValueError("Empty domain")

        # If both cells have the same forced value,
        # the constraint cannot be satisfied.
        if (
            len(domain_a) == 1
            and len(domain_b) == 1
            and domain_a == domain_b
        ):
            raise ValueError(
                "NotEqualConstraint contradiction"
            )

        changed = False

        # If A is fixed, remove its value from B.
        if len(domain_a) == 1:
            value = next(iter(domain_a))

            if value in domain_b:
                domains[b] = domain_b - {value}
                changed = True

        # If B is fixed, remove its value from A.
        if len(domain_b) == 1:
            value = next(iter(domain_b))

            if value in domains[a]:
                domains[a] = domains[a] - {value}
                changed = True

        if not domains[a] or not domains[b]:
            raise ValueError(
                "NotEqualConstraint emptied a domain"
            )

        return changed


class NonConsecutiveConstraint(Constraint):
    """
    Two cells cannot contain consecutive digits.

    Valid examples:
        (1, 3), (4, 7), (5, 5)

    Invalid examples:
        (3, 4), (7, 6)
    """

    def __init__(self, cell_a, cell_b):
        super().__init__((cell_a, cell_b))

        if cell_a == cell_b:
            raise ValueError(
                "NonConsecutiveConstraint requires two distinct cells"
            )

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return abs(assignment[a] - assignment[b]) != 1

    def propagate(self, domains):
        a, b = self.variables

        domain_a = domains[a]
        domain_b = domains[b]

        if not domain_a or not domain_b:
            raise ValueError("Empty domain")

        # Keep only values that have at least one
        # compatible value in the other domain.
        supported_a = {
            x for x in domain_a
            if any(abs(x - y) != 1 for y in domain_b)
        }

        supported_b = {
            y for y in domain_b
            if any(abs(x - y) != 1 for x in domain_a)
        }

        if not supported_a or not supported_b:
            raise ValueError(
                "NonConsecutiveConstraint contradiction"
            )

        changed = (
            supported_a != domain_a
            or supported_b != domain_b
        )

        if changed:
            domains[a] = supported_a
            domains[b] = supported_b

        return changed


class GermanWhispersConstraint(Constraint):
    """
    German Whispers line.

    Adjacent cells along the line must contain
    digits that differ by at least 5.

    Valid examples:
        (1, 6), (9, 4), (2, 7)

    Invalid examples:
        (3, 4), (6, 9), (5, 5)
    """

    MINIMUM_DIFFERENCE = 5

    def __init__(self, cells):
        cells = tuple(cells)

        if len(cells) < 2:
            raise ValueError(
                "A German Whispers line needs at least two cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A German Whispers line cannot repeat a cell."
            )

        super().__init__(cells)

    def is_satisfied(self, assignment):
        minimum = self.MINIMUM_DIFFERENCE

        for a, b in zip(self.variables, self.variables[1:]):
            if a not in assignment or b not in assignment:
                continue

            if abs(assignment[a] - assignment[b]) < minimum:
                return False

        return True

    def _restrict_pair(self, domains, a, b):
        """
        Enforce arc consistency between one adjacent
        pair of cells on the line.
        """
        minimum = self.MINIMUM_DIFFERENCE

        domain_a = domains[a]
        domain_b = domains[b]

        if not domain_a or not domain_b:
            raise ValueError("Empty domain")

        supported_a = {
            x for x in domain_a
            if any(abs(x - y) >= minimum for y in domain_b)
        }

        supported_b = {
            y for y in domain_b
            if any(abs(x - y) >= minimum for x in domain_a)
        }

        if not supported_a or not supported_b:
            raise ValueError(
                "GermanWhispersConstraint contradiction"
            )

        changed = (
            supported_a != domain_a
            or supported_b != domain_b
        )

        if changed:
            domains[a] = supported_a
            domains[b] = supported_b

        return changed

    def propagate(self, domains):
        """
        Repeatedly enforce arc consistency along every
        adjacent pair until the domains are stable.
        """
        changed = False

        while True:
            pass_changed = False

            for a, b in zip(self.variables, self.variables[1:]):
                if self._restrict_pair(domains, a, b):
                    pass_changed = True

            if not pass_changed:
                return changed

            changed = True


class RenbanConstraint(Constraint):
    """
    Renban line.

    A line of N cells must contain N distinct consecutive
    digits in any order, e.g. 4-6-5-7 on a 4-cell line.

    Completed lines must satisfy both:
    - All values are distinct.
    - max(values) - min(values) == N - 1.
    """

    def __init__(self, cells):
        cells = tuple(cells)

        if not 2 <= len(cells) <= 9:
            raise ValueError(
                "A Renban line needs between two and nine cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A Renban line cannot repeat a cell."
            )

        super().__init__(cells)

        # Cache domain-specific propagation results.
        self._support_cache = {}

    def is_satisfied(self, assignment):
        values = [
            assignment[cell]
            for cell in self.variables
            if cell in assignment
        ]

        if not values:
            return True

        if len(values) != len(set(values)):
            return False

        # Every assigned value must fit inside one
        # consecutive interval of the line's length.
        return max(values) - min(values) <= len(self.variables) - 1

    def _window_supports(self, domains, window):
        """
        Collect supported (cell, value) pairs for one
        consecutive digit interval.

        A value is supported when it appears in at least
        one complete, distinct assignment of the window's
        digits to the line's cells.

        Returns None if the window admits no assignment.
        """
        allowed = {
            cell: domains[cell] & window
            for cell in self.variables
        }

        # Every cell needs a candidate in the window.
        if any(not values for values in allowed.values()):
            return None

        # Every digit in the window needs a possible cell.
        if any(
            not any(digit in allowed[cell] for cell in self.variables)
            for digit in window
        ):
            return None

        # Search cells with the fewest candidates first.
        order = sorted(
            self.variables,
            key=lambda cell: len(allowed[cell])
        )

        def extend(index, remaining, chosen):
            """Complete one assignment, honoring seeds in chosen."""
            if index == len(order):
                return True

            cell = order[index]

            if cell in chosen:
                return extend(index + 1, remaining, chosen)

            for value in allowed[cell] & remaining:
                chosen[cell] = value

                if extend(index + 1, remaining - {value}, chosen):
                    return True

                del chosen[cell]

            return False

        supports = {cell: set() for cell in self.variables}

        # Seed one search per unsupported pair. Each found
        # assignment supports every pair it contains, so few
        # searches are needed in practice.
        for cell in order:
            for value in allowed[cell]:
                if value in supports[cell]:
                    continue

                chosen = {cell: value}

                if extend(0, window - {value}, chosen):
                    for var, chosen_value in chosen.items():
                        supports[var].add(chosen_value)

        if any(not supports[cell] for cell in self.variables):
            return None

        return supports

    def propagate(self, domains):
        """
        Keep only values that participate in at least one
        complete assignment of some consecutive interval.
        """
        n = len(self.variables)

        key = tuple(
            frozenset(domains[var])
            for var in self.variables
        )

        if key in self._support_cache:
            cached = self._support_cache[key]

            if cached is None:
                raise ValueError(
                    "Renban line has no valid assignments"
                )

            supports = {
                var: set(values)
                for var, values in zip(self.variables, cached)
            }

        else:
            supports = {var: set() for var in self.variables}

            for low in range(1, 11 - n):
                window = frozenset(range(low, low + n))

                window_supports = self._window_supports(
                    domains, window
                )

                if window_supports is None:
                    continue

                for var in self.variables:
                    supports[var].update(window_supports[var])

                # Stop early once nothing can be pruned.
                if all(
                    supports[var] == domains[var]
                    for var in self.variables
                ):
                    break

            # Detect contradictions before mutating domains.
            if any(not supports[var] for var in self.variables):
                self._support_cache[key] = None
                raise ValueError(
                    "Renban line has no valid assignments"
                )

            self._support_cache[key] = tuple(
                frozenset(supports[var])
                for var in self.variables
            )

        changed = False

        for var in self.variables:
            retained = domains[var] & supports[var]

            if not retained:
                raise ValueError(
                    "Renban line has no valid assignments"
                )

            if retained != domains[var]:
                domains[var] = retained
                changed = True

        return changed


class PalindromeConstraint(Constraint):
    """
    Palindrome line.

    The sequence of digits must read the same in both
    directions: values[i] == values[N - 1 - i] for every
    mirrored pair. The center cell of an odd-length line
    is unrestricted.
    """

    def __init__(self, cells):
        cells = tuple(cells)

        if len(cells) < 2:
            raise ValueError(
                "A Palindrome line needs at least two cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A Palindrome line cannot repeat a cell."
            )

        super().__init__(cells)

        n = len(cells)

        self.mirrored_pairs = tuple(
            (cells[i], cells[n - 1 - i])
            for i in range(n // 2)
        )

    def is_satisfied(self, assignment):
        for a, b in self.mirrored_pairs:
            if a not in assignment or b not in assignment:
                continue

            if assignment[a] != assignment[b]:
                return False

        return True

    def propagate(self, domains):
        """
        Intersect the domains of every mirrored pair.

        Equality propagation is exact for this constraint,
        so no support enumeration is needed.
        """
        # Detect contradictions before mutating domains.
        intersections = []

        for a, b in self.mirrored_pairs:
            common = domains[a] & domains[b]

            if not common:
                raise ValueError(
                    "PalindromeConstraint contradiction"
                )

            intersections.append((a, b, common))

        changed = False

        for a, b, common in intersections:
            if domains[a] != common:
                domains[a] = set(common)
                changed = True

            if domains[b] != common:
                domains[b] = set(common)
                changed = True

        return changed


class ArrowConstraint(Constraint):
    """
    Arrow Sudoku constraint.

    The digits on the arrow shaft must sum to the number
    shown in the circle. Multi-cell circles are read as a
    base-10 number in the supplied cell order.

    Shaft digits may repeat unless other constraints
    forbid it.
    """

    def __init__(self, circle_cells, arrow_cells):
        circle_cells = tuple(circle_cells)
        arrow_cells = tuple(arrow_cells)

        if not circle_cells:
            raise ValueError(
                "An arrow needs at least one circle cell."
            )

        if not arrow_cells:
            raise ValueError(
                "An arrow needs at least one shaft cell."
            )

        all_cells = circle_cells + arrow_cells

        if len(set(all_cells)) != len(all_cells):
            raise ValueError(
                "Arrow circle and shaft cells must be distinct."
            )

        super().__init__(all_cells)

        self.circle_cells = circle_cells
        self.arrow_cells = arrow_cells

        # Cache domain-state-dependent propagation results.
        self._support_cache = {}

    def _circle_bounds(self, assignment):
        """Smallest and largest possible circle numbers."""
        low = 0
        high = 0

        for cell in self.circle_cells:
            if cell in assignment:
                digit_low = digit_high = assignment[cell]
            else:
                digit_low, digit_high = 1, 9

            low = low * 10 + digit_low
            high = high * 10 + digit_high

        return low, high

    def _arrow_bounds(self, assignment):
        """Smallest and largest possible shaft sums."""
        low = 0
        high = 0

        for cell in self.arrow_cells:
            if cell in assignment:
                low += assignment[cell]
                high += assignment[cell]
            else:
                low += 1
                high += 9

        return low, high

    def is_satisfied(self, assignment):
        circle_low, circle_high = self._circle_bounds(assignment)
        arrow_low, arrow_high = self._arrow_bounds(assignment)

        # The possible ranges must overlap. For complete
        # assignments both ranges collapse to one value,
        # making this an exact equality test.
        return (
            circle_low <= arrow_high
            and circle_high >= arrow_low
        )

    def _find_supports(self, domains):
        """
        Compute supported values with forward/backward
        dynamic programming over shaft sums.

        Returns None when no valid assignment exists.
        """
        circle = self.circle_cells
        arrow = self.arrow_cells
        n = len(arrow)

        # Positional digits are independent, so the number
        # bounds come from per-cell domain extremes.
        min_circle = 0
        max_circle = 0

        for cell in circle:
            min_circle = min_circle * 10 + min(domains[cell])
            max_circle = max_circle * 10 + max(domains[cell])

        min_sum = sum(min(domains[cell]) for cell in arrow)
        max_sum = sum(max(domains[cell]) for cell in arrow)

        if min_circle > max_sum or max_circle < min_sum:
            return None

        max_target = min(max_circle, max_sum)

        # Minimum remaining sum after each shaft position,
        # used to prune unreachable partial sums.
        suffix_min = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix_min[i] = suffix_min[i + 1] + min(domains[arrow[i]])

        # Forward pass: partial sums of arrow[:i].
        forward = [{0}]

        for i, cell in enumerate(arrow):
            bound = max_target - suffix_min[i + 1]
            step = set()

            for partial in forward[-1]:
                for value in domains[cell]:
                    total = partial + value

                    if total <= bound:
                        step.add(total)

            if not step:
                return None

            forward.append(step)

        # Backward pass: sums achievable by arrow[i:].
        backward = [set() for _ in range(n)] + [{0}]

        for i in range(n - 1, -1, -1):
            step = set()

            for partial in backward[i + 1]:
                for value in domains[arrow[i]]:
                    total = partial + value

                    if total <= max_target:
                        step.add(total)

            backward[i] = step

        reachable = forward[n]

        # Match circle numbers against reachable sums and
        # collect circle supports in one pass.
        targets = set()
        supports = {cell: set() for cell in self.variables}

        for combo in product(*(sorted(domains[cell]) for cell in circle)):
            number = 0

            for digit in combo:
                number = number * 10 + digit

            if number in reachable:
                targets.add(number)

                for cell, digit in zip(circle, combo):
                    supports[cell].add(digit)

        if not targets:
            return None

        # Shaft supports: value v in cell i is supported
        # when prefix + v + suffix hits a target.
        for i, cell in enumerate(arrow):
            needed = {
                target - suffix
                for target in targets
                for suffix in backward[i + 1]
            }

            for value in domains[cell]:
                if any(
                    prefix + value in needed
                    for prefix in forward[i]
                ):
                    supports[cell].add(value)

            if not supports[cell]:
                return None

        return supports

    def propagate(self, domains):
        key = tuple(
            frozenset(domains[var])
            for var in self.variables
        )

        if key in self._support_cache:
            cached = self._support_cache[key]

            if cached is None:
                raise ValueError(
                    "Arrow has no valid assignments"
                )

            supports = {
                var: set(values)
                for var, values in zip(self.variables, cached)
            }

        else:
            supports = self._find_supports(domains)

            # Detect contradictions before mutating domains.
            if supports is None:
                self._support_cache[key] = None
                raise ValueError(
                    "Arrow has no valid assignments"
                )

            self._support_cache[key] = tuple(
                frozenset(supports[var])
                for var in self.variables
            )

        changed = False

        for var in self.variables:
            retained = domains[var] & supports[var]

            if not retained:
                raise ValueError(
                    "Arrow has no valid assignments"
                )

            if retained != domains[var]:
                domains[var] = retained
                changed = True

        return changed


class KropkiConstraint(Constraint):
    """
    Kropki dot between two orthogonally adjacent cells.

    White dot: the digits differ by exactly 1.
    Black dot: one digit is exactly twice the other.

    Note that the pair (1, 2) satisfies both dot types.
    """

    DOT_TYPES = ("white", "black")

    def __init__(self, cell_a, cell_b, dot_type):
        if cell_a == cell_b:
            raise ValueError(
                "KropkiConstraint requires two distinct cells"
            )

        if dot_type not in self.DOT_TYPES:
            raise ValueError(
                f"Invalid Kropki dot type: {dot_type!r}"
            )

        super().__init__((cell_a, cell_b))

        self.dot_type = dot_type

    def _matches(self, a, b):
        if self.dot_type == "white":
            return abs(a - b) == 1

        return a == 2 * b or b == 2 * a

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return self._matches(assignment[a], assignment[b])

    def propagate(self, domains):
        a, b = self.variables

        domain_a = domains[a]
        domain_b = domains[b]

        if not domain_a or not domain_b:
            raise ValueError("Empty domain")

        supported_a = {
            x for x in domain_a
            if any(self._matches(x, y) for y in domain_b)
        }

        supported_b = {
            y for y in domain_b
            if any(self._matches(x, y) for x in domain_a)
        }

        if not supported_a or not supported_b:
            raise ValueError(
                "KropkiConstraint contradiction"
            )

        changed = (
            supported_a != domain_a
            or supported_b != domain_b
        )

        if changed:
            domains[a] = supported_a
            domains[b] = supported_b

        return changed


class NegativeKropkiConstraint(Constraint):
    """
    Negative Kropki constraint for an orthogonally
    adjacent cell pair without a dot.

    Neither Kropki relationship may hold: the digits
    must not be consecutive and must not be in a
    1:2 ratio.
    """

    def __init__(self, cell_a, cell_b):
        if cell_a == cell_b:
            raise ValueError(
                "NegativeKropkiConstraint requires "
                "two distinct cells"
            )

        super().__init__((cell_a, cell_b))

    @staticmethod
    def _matches(a, b):
        return (
            abs(a - b) != 1
            and a != 2 * b
            and b != 2 * a
        )

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return self._matches(assignment[a], assignment[b])

    def propagate(self, domains):
        a, b = self.variables

        domain_a = domains[a]
        domain_b = domains[b]

        if not domain_a or not domain_b:
            raise ValueError("Empty domain")

        supported_a = {
            x for x in domain_a
            if any(self._matches(x, y) for y in domain_b)
        }

        supported_b = {
            y for y in domain_b
            if any(self._matches(x, y) for x in domain_a)
        }

        if not supported_a or not supported_b:
            raise ValueError(
                "NegativeKropkiConstraint contradiction"
            )

        changed = (
            supported_a != domain_a
            or supported_b != domain_b
        )

        if changed:
            domains[a] = supported_a
            domains[b] = supported_b

        return changed


def _propagate_binary_relation(
    domains, cell_a, cell_b, relation, name
):
    """
    Enforce bidirectional arc consistency for a binary
    relation between two cells.

    Removes values with no supporting partner in the
    other cell's domain. Raises ValueError when either
    cell loses every candidate.
    """
    domain_a = domains[cell_a]
    domain_b = domains[cell_b]

    if not domain_a or not domain_b:
        raise ValueError("Empty domain")

    supported_a = {
        x for x in domain_a
        if any(relation(x, y) for y in domain_b)
    }

    supported_b = {
        y for y in domain_b
        if any(relation(x, y) for x in domain_a)
    }

    if not supported_a or not supported_b:
        raise ValueError(f"{name} contradiction")

    changed = (
        supported_a != domain_a
        or supported_b != domain_b
    )

    if changed:
        domains[cell_a] = supported_a
        domains[cell_b] = supported_b

    return changed


class InequalityConstraint(Constraint):
    """
    Inequality between two cells.

    With operator "<", cell_a's digit must be strictly
    less than cell_b's digit; with ">", strictly
    greater. The cells need not be adjacent.
    """

    OPERATORS = ("<", ">")

    def __init__(self, cell_a, cell_b, operator):
        if cell_a == cell_b:
            raise ValueError(
                "InequalityConstraint requires two distinct cells"
            )

        if operator not in self.OPERATORS:
            raise ValueError(
                f"Invalid inequality operator: {operator!r}"
            )

        super().__init__((cell_a, cell_b))

        self.operator = operator

    def _matches(self, a, b):
        if self.operator == "<":
            return a < b

        return a > b

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return self._matches(assignment[a], assignment[b])

    def propagate(self, domains):
        a, b = self.variables

        return _propagate_binary_relation(
            domains, a, b, self._matches,
            "InequalityConstraint",
        )


class XVConstraint(Constraint):
    """
    XV marker between two orthogonally adjacent cells.

    V: the digits sum to 5.
    X: the digits sum to 10.
    """

    MARKERS = {"V": 5, "X": 10}

    def __init__(self, cell_a, cell_b, marker):
        if cell_a == cell_b:
            raise ValueError(
                "XVConstraint requires two distinct cells"
            )

        if marker not in self.MARKERS:
            raise ValueError(
                f"Invalid XV marker: {marker!r}"
            )

        super().__init__((cell_a, cell_b))

        self.marker = marker
        self.target_sum = self.MARKERS[marker]

    def _matches(self, a, b):
        return a + b == self.target_sum

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return self._matches(assignment[a], assignment[b])

    def propagate(self, domains):
        a, b = self.variables

        return _propagate_binary_relation(
            domains, a, b, self._matches, "XVConstraint",
        )


class NegativeXVConstraint(Constraint):
    """
    Negative XV constraint for an unmarked orthogonally
    adjacent pair: the digits must sum to neither 5
    nor 10.
    """

    def __init__(self, cell_a, cell_b):
        if cell_a == cell_b:
            raise ValueError(
                "NegativeXVConstraint requires two distinct cells"
            )

        super().__init__((cell_a, cell_b))

    @staticmethod
    def _matches(a, b):
        return a + b != 5 and a + b != 10

    def is_satisfied(self, assignment):
        a, b = self.variables

        if a not in assignment or b not in assignment:
            return True

        return self._matches(assignment[a], assignment[b])

    def propagate(self, domains):
        a, b = self.variables

        return _propagate_binary_relation(
            domains, a, b, self._matches,
            "NegativeXVConstraint",
        )


class ParityConstraint(Constraint):
    """
    Unary parity constraint for one cell.

    Odd cells contain 1, 3, 5, 7, or 9.
    Even cells contain 2, 4, 6, or 8.
    """

    PARITIES = {
        "odd": frozenset({1, 3, 5, 7, 9}),
        "even": frozenset({2, 4, 6, 8}),
    }

    def __init__(self, cell, parity):
        if parity not in self.PARITIES:
            raise ValueError(
                f"Invalid parity: {parity!r}"
            )

        super().__init__((cell,))

        self.parity = parity
        self.allowed = set(self.PARITIES[parity])

    def is_satisfied(self, assignment):
        cell = self.variables[0]

        if cell not in assignment:
            return True

        return assignment[cell] in self.allowed

    def propagate(self, domains):
        cell = self.variables[0]

        allowed = domains[cell] & self.allowed

        if not allowed:
            raise ValueError(
                "ParityConstraint contradiction"
            )

        if allowed != domains[cell]:
            domains[cell] = allowed
            return True

        return False


class BetweenLineConstraint(Constraint):
    """
    Between Line.

    The first and last cells are endpoints; every
    interior digit must lie strictly between the two
    endpoint values, in either endpoint order.

    Interior digits may repeat unless other constraints
    forbid it.
    """

    def __init__(self, cells):
        cells = tuple(cells)

        if len(cells) < 3:
            raise ValueError(
                "A Between Line needs at least three cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A Between Line cannot repeat a cell."
            )

        super().__init__(cells)

        self.endpoints = (cells[0], cells[-1])
        self.interior = cells[1:-1]

    def is_satisfied(self, assignment):
        end_a, end_b = self.endpoints

        interior_values = [
            assignment[cell]
            for cell in self.interior
            if cell in assignment
        ]

        options_a = (
            (assignment[end_a],)
            if end_a in assignment
            else range(1, 10)
        )

        options_b = (
            (assignment[end_b],)
            if end_b in assignment
            else range(1, 10)
        )

        # Some endpoint pairing must leave every assigned
        # interior digit strictly between the endpoints.
        for value_a in options_a:
            for value_b in options_b:
                low, high = sorted((value_a, value_b))

                if all(
                    low < value < high
                    for value in interior_values
                ):
                    return True

        return False

    def propagate(self, domains):
        end_a, end_b = self.endpoints

        supports = {cell: set() for cell in self.variables}

        for value_a in domains[end_a]:
            for value_b in domains[end_b]:
                low, high = sorted((value_a, value_b))

                if high - low < 2:
                    continue

                # Every interior cell needs a candidate
                # strictly inside the interval.
                if any(
                    not any(
                        low < value < high
                        for value in domains[cell]
                    )
                    for cell in self.interior
                ):
                    continue

                supports[end_a].add(value_a)
                supports[end_b].add(value_b)

                for cell in self.interior:
                    supports[cell].update(
                        value
                        for value in domains[cell]
                        if low < value < high
                    )

        # Detect contradictions before mutating domains.
        if any(not supports[cell] for cell in self.variables):
            raise ValueError(
                "BetweenLineConstraint contradiction"
            )

        changed = False

        for cell in self.variables:
            if supports[cell] != domains[cell]:
                domains[cell] = supports[cell]
                changed = True

        return changed


class LittleKillerConstraint(Constraint):
    """
    Little Killer diagonal.

    The digits along the diagonal sum to the clue.
    Digits may repeat when standard Sudoku allows it;
    no all-different rule is imposed.
    """

    def __init__(self, cells, target_sum):
        cells = tuple(cells)

        if not cells:
            raise ValueError(
                "A Little Killer clue needs at least one cell."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A Little Killer diagonal cannot repeat a cell."
            )

        if not isinstance(target_sum, int):
            raise ValueError(
                "Little Killer target sum must be an integer"
            )

        n = len(cells)

        if not n <= target_sum <= 9 * n:
            raise ValueError(
                "Little Killer target sum is impossible "
                "for the diagonal length"
            )

        super().__init__(cells)

        self.target_sum = target_sum

        # Cache domain-state-dependent propagation results.
        self._support_cache = {}

    def is_satisfied(self, assignment):
        low = 0
        high = 0

        for cell in self.variables:
            if cell in assignment:
                low += assignment[cell]
                high += assignment[cell]
            else:
                low += 1
                high += 9

        return low <= self.target_sum <= high

    def _find_supports(self, domains):
        """
        Forward/backward sum DP, as in ArrowConstraint
        but with one fixed target.

        Returns None when no valid assignment exists.
        """
        cells = self.variables
        n = len(cells)
        target = self.target_sum

        suffix_min = [0] * (n + 1)
        suffix_max = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            domain = domains[cells[i]]
            suffix_min[i] = suffix_min[i + 1] + min(domain)
            suffix_max[i] = suffix_max[i + 1] + max(domain)

        if not suffix_min[0] <= target <= suffix_max[0]:
            return None

        # Forward pass, keeping only completable sums.
        forward = [{0}]

        for i, cell in enumerate(cells):
            step = {
                total
                for partial in forward[-1]
                for value in domains[cell]
                for total in (partial + value,)
                if (
                    total + suffix_min[i + 1] <= target
                    <= total + suffix_max[i + 1]
                )
            }

            if not step:
                return None

            forward.append(step)

        # Backward pass: sums achievable by cells[i:].
        backward = [set() for _ in range(n)] + [{0}]

        for i in range(n - 1, -1, -1):
            backward[i] = {
                partial + value
                for partial in backward[i + 1]
                for value in domains[cells[i]]
                if partial + value <= target
            }

        supports = {}

        for i, cell in enumerate(cells):
            needed = {
                target - suffix
                for suffix in backward[i + 1]
            }

            supported = {
                value
                for value in domains[cell]
                if any(
                    prefix + value in needed
                    for prefix in forward[i]
                )
            }

            if not supported:
                return None

            supports[cell] = supported

        return supports

    def propagate(self, domains):
        key = tuple(
            frozenset(domains[var])
            for var in self.variables
        )

        if key in self._support_cache:
            cached = self._support_cache[key]

            if cached is None:
                raise ValueError(
                    "Little Killer has no valid assignments"
                )

            supports = {
                var: set(values)
                for var, values in zip(self.variables, cached)
            }

        else:
            supports = self._find_supports(domains)

            # Detect contradictions before mutating.
            if supports is None:
                self._support_cache[key] = None
                raise ValueError(
                    "Little Killer has no valid assignments"
                )

            self._support_cache[key] = tuple(
                frozenset(supports[var])
                for var in self.variables
            )

        changed = False

        for var in self.variables:
            retained = domains[var] & supports[var]

            if not retained:
                raise ValueError(
                    "Little Killer has no valid assignments"
                )

            if retained != domains[var]:
                domains[var] = retained
                changed = True

        return changed


def generate_knight_pairs():
    """
    Generate every unique pair of cells connected
    by a chess knight's move on a 9x9 Sudoku grid.
    """
    offsets = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1),
    ]

    pairs = set()

    for r in range(9):
        for c in range(9):
            for dr, dc in offsets:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < 9 and 0 <= nc < 9:
                    a = (r, c)
                    b = (nr, nc)

                    pairs.add(tuple(sorted((a, b))))

    return sorted(pairs)

def generate_king_pairs():
    """
    Return all unique diagonally adjacent cell pairs.

    Horizontal and vertical king moves are already
    covered by standard Sudoku row/column constraints.
    """
    offsets = [
        (-1, -1), (-1, 1),
        (1, -1), (1, 1),
    ]

    pairs = set()

    for r in range(9):
        for c in range(9):
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc

                if 0 <= nr < 9 and 0 <= nc < 9:
                    a = (r, c)
                    b = (nr, nc)

                    pairs.add(tuple(sorted((a, b))))

    return sorted(pairs)

def generate_orthogonal_pairs():
    """
    Return every unique pair of orthogonally
    adjacent cells in a 9x9 Sudoku grid.
    """
    pairs = []

    for r in range(9):
        for c in range(9):

            # Right neighbor
            if c + 1 < 9:
                pairs.append((
                    (r, c),
                    (r, c + 1)
                ))

            # Bottom neighbor
            if r + 1 < 9:
                pairs.append((
                    (r, c),
                    (r + 1, c)
                ))

    return pairs
