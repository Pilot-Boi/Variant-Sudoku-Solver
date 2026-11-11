
"""Read-only audit of all controlled Sudoku datasets."""

import json
from collections import Counter, defaultdict

from benchmarks.run_controlled_benchmarks import (
    DATASETS,
    CLUE_VARIANTS,
    CLUE_COUNTS,
    build_puzzle,
    get_conditions,
    prepare_cases,
    reference_assignment,
)
from sudoku.validator import validate_solution


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def audit(experiment, path):
    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    records = data["experiments"]
    cases = prepare_cases(experiment, records)

    check(records, f"{experiment}: empty dataset")

    ids = [record["id"] for record in records]
    check(
        len(ids) == len(set(ids)),
        f"{experiment}: duplicate record IDs",
    )


    expected_cases = 300
    
    check(
        len(cases) == expected_cases,
        f"{experiment}: expected {expected_cases} cases, "
        f"found {len(cases)}",
    )

    if experiment == "givens":
        conditions = [
            condition
            for case in cases
            for condition, _ in get_conditions(experiment, case)
        ]

        assert len(conditions) == 525, (
            f"givens: expected 525 benchmark configurations, "
            f"found {len(conditions)}"
        )
    shared_clues = defaultdict(list)

    if experiment in CLUE_VARIANTS:
        counts = Counter(record["clue_count"] for record in records)

        check(
            all(counts[n] == 300 for n in CLUE_COUNTS),
            f"{experiment}: incorrect clue-count distribution",
        )

        by_base = defaultdict(dict)

        for record in records:
            check(
                record["variant"] == experiment,
                f"{experiment}: variant mismatch",
            )

            base_id = record["base_id"]
            count = record["clue_count"]

            check(
                count not in by_base[base_id],
                f"{experiment}: duplicate clue count for {base_id}",
            )

            check(
                len(record["clues"]) == count,
                f"{experiment}: incorrect clue count for {base_id}",
            )

            by_base[base_id][count] = record

        check(
            len(by_base) == 300,
            f"{experiment}: expected 300 unique base IDs",
        )

        for base_id, versions in by_base.items():
            check(
                set(versions) == set(CLUE_COUNTS),
                f"{experiment}: missing clue levels for {base_id}",
            )

            full = versions[6]["clues"]

            for count in CLUE_COUNTS:
                check(
                    versions[count]["clues"] == full[:count],
                    f"{experiment}: non-nested clues for {base_id}",
                )

                check(
                    versions[count]["puzzle"] == versions[6]["puzzle"],
                    f"{experiment}: puzzle mismatch for {base_id}",
                )

                check(
                    versions[count]["solution"] == versions[6]["solution"],
                    f"{experiment}: solution mismatch for {base_id}",
                )

        for case in cases:
            key = (
                case["group"],
                case["grid_index"],
                case["pattern_index"],
            )
            shared_clues[key].append(case)

    # Check every selected condition against the reference solution.
    checked = 0

    for case in cases:
        actual_givens = sum(
            value != 0
            for row in case["puzzle"]
            for value in row
        )

        check(
            actual_givens == case["given_count"],
            f"{experiment}: givens mismatch in {case['id']}",
        )

        reference = reference_assignment(case)

        for condition in (
            ["standard"]
            if experiment == "givens"
            else (
                ["standard", *[
                    f"{experiment}_{n}" for n in CLUE_COUNTS
                ]]
                if experiment in CLUE_VARIANTS
                else [
                    "standard",
                    "thermometer_2",
                    "thermometer_4",
                    "thermometer_6",
                ]
            )
        ):
            puzzle = build_puzzle(case, condition)
            errors = validate_solution(puzzle, reference)

            check(
                not errors,
                f"{experiment}: {case['id']} / {condition}: {errors}",
            )
            checked += 1

        if experiment == "givens":
            for variant in ("diagonal", "anti_knight", "anti_king"):
                if case["reference_rules"].get(variant, False):
                    puzzle = build_puzzle(case, variant)
                    errors = validate_solution(puzzle, reference)
                    check(
                        not errors,
                        f"{experiment}: {case['id']} / {variant}: "
                        f"{errors}",
                    )
                    checked += 1

    if experiment in CLUE_VARIANTS:
        check(
            len(shared_clues) == 100,
            f"{experiment}: expected 100 shared clue sets, "
            f"found {len(shared_clues)}",
        )

        for key, group in shared_clues.items():
            check(
                sorted(case["given_count"] for case in group)
                == [20, 25, 30],
                f"{experiment}: incorrect givens levels for {key}",
            )

            first = group[0]

            for case in group[1:]:
                check(
                    case["clues"] == first["clues"],
                    f"{experiment}: clues differ across givens for {key}",
                )
                check(
                    case["solution"] == first["solution"],
                    f"{experiment}: reference grid mismatch for {key}",
                )

    return len(records), len(cases), checked


def main():
    print("========== DATASET INTEGRITY AUDIT ==========")

    failed = []

    for experiment, path in DATASETS.items():
        try:
            records, cases, checked = audit(experiment, path)

            print(
                f"PASS {experiment:18} "
                f"{records:5} records | "
                f"{cases:3} cases | "
                f"{checked:4} reference checks"
            )

        except Exception as exc:
            failed.append(experiment)
            print(f"FAIL {experiment}: {type(exc).__name__}: {exc}")

    if failed:
        raise SystemExit(
            f"\nAUDIT FAILED: {', '.join(failed)}"
        )

    print("\nALL DATASETS PASSED")


if __name__ == "__main__":
    main()