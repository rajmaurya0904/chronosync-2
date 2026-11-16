"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import chronosync_2


def test_version_is_set() -> None:
    assert chronosync_2.__version__
