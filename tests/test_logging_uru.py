from __future__ import annotations

from pathlib import Path

from app.core import logging_uru


def test_resolve_log_level_returns_debug_when_debug_enabled() -> None:
    assert logging_uru.resolve_log_level("INFO", debug=True) == "DEBUG"


def test_resolve_log_level_uses_configured_level_when_debug_disabled() -> None:
    assert logging_uru.resolve_log_level("warning", debug=False) == "WARNING"


def test_should_enable_diagnose_only_in_debug_mode() -> None:
    assert logging_uru.should_enable_diagnose(debug=True) is True
    assert logging_uru.should_enable_diagnose(debug=False) is False


def test_build_log_file_paths_returns_expected_daily_filenames() -> None:
    run_log_path, error_log_path = logging_uru.build_log_file_paths(
        project_root=Path("/tmp/demo-project"),
        date_text="2026-06-15",
    )

    assert run_log_path == Path("/tmp/demo-project/logs/app_run/app_run_2026-06-15.log")
    assert error_log_path == Path(
        "/tmp/demo-project/logs/app_error/app_error_2026-06-15.log"
    )
