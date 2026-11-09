"""
Metadata for benchmark puzzles featured on
Cracking the Cryptic (CTC).

Entries are keyed by the puzzle module's exact NAME
constant so metadata can be matched to discovered
benchmark puzzles.

To register a new CTC puzzle, add one dictionary entry
with the fields below. Omit unknown fields rather than
inventing values; missing fields appear blank in the
benchmark output.

Note: the video duration measures the published video,
not the human's exact active solving time. Ratios
derived from it are video-to-solver duration ratios,
not literal human solving speeds.
"""

CTC_METADATA = {
    "Center Focus — DedaKosta": {
        "catalogue_id": 9118,
        "title": "Center Focus",
        "setter": "DedaKosta",
        "human_solver": "Mark",
        "video_date": "2026-09-12",
        "video_duration": "02:15:39",
        "video_seconds": 8139,
    },
}


def get_ctc_metadata(puzzle_name):
    """Return the CTC metadata dict for a puzzle, or None."""
    return CTC_METADATA.get(puzzle_name)


def duration_to_seconds(duration):
    """
    Convert a "H:MM:SS" or "MM:SS" duration string
    to total seconds.
    """
    parts = duration.split(":")

    if not 2 <= len(parts) <= 3:
        raise ValueError(
            f"Invalid duration format: {duration!r}"
        )

    values = [int(part) for part in parts]

    seconds = 0

    for value in values:
        seconds = seconds * 60 + value

    return seconds


def seconds_to_duration(seconds):
    """Format whole seconds as "H:MM:SS" or "M:SS"."""
    minutes, second = divmod(int(seconds), 60)
    hours, minute = divmod(minutes, 60)

    if hours:
        return f"{hours}:{minute:02d}:{second:02d}"

    return f"{minute}:{second:02d}"
