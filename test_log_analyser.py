from log_analyser import analyze_log


def test_counts_each_log_level(tmp_path):
    log_path = tmp_path / "counts.log"
    log_path.write_text(
        "INFO started\nWARNING slow\nERROR failed\nDEBUG details\nERROR again\n",
        encoding="utf-8",
    )

    counts, _ = analyze_log(log_path)

    assert counts["ERROR"] == 2
    assert counts["WARNING"] == 1
    assert counts["INFO"] == 1
    assert counts["DEBUG"] == 1


def test_collects_error_lines(tmp_path):
    log_path = tmp_path / "errors.log"
    log_path.write_text("INFO started\nERROR failed\nERROR timed out\n", encoding="utf-8")

    _, error_lines = analyze_log(log_path)

    assert error_lines == ["ERROR failed", "ERROR timed out"]


def test_empty_file_has_zero_counts_and_no_errors(tmp_path):
    log_path = tmp_path / "empty.log"
    log_path.write_text("", encoding="utf-8")

    counts, error_lines = analyze_log(log_path)

    assert all(counts[level] == 0 for level in ("ERROR", "WARNING", "INFO", "DEBUG"))
    assert error_lines == []


def test_missing_file_raises_file_not_found_error(tmp_path):
    import pytest

    log_path = tmp_path / "missing.log"

    with pytest.raises(FileNotFoundError):
        analyze_log(log_path)